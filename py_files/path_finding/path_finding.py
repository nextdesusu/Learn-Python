from random import randint, choice
import math
import os
import time
import collections.abc

clear_console = lambda: os.system('cls')
VICTORY_STATUS = False
ROOM_WIDTH = 30
ROOM_HEIGHT = 30
MAX_ROOMS = 5
MIN_SIZE = 2
MAX_SIZE = 6
P_START = [4, 4]
G_POS = [10, 23]

class Queue:
    
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()
    
    def __str__(self):
        return str(self.elements)

def heuristic_for_ai(actor, goal):
    x1, y1 = actor.x, actor.y
    x2, y2 = goal.x, goal.y
    return abs(x1 - x2) + abs(y1 - y2)

def search(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal: 
            break           

        for next_ in graph.neighbors(current):
            if next_ not in came_from:
                frontier.put(next_)
                came_from[next_] = current

    current = goal 
    path = list()
    path.append(current)
    while current != start: 
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

class Tile:
    
    def __init__(self, blocked):
        self.blocked = blocked
        
    def __str__(self):
        if self.blocked:
            return "#"
        return "."
        
class Rect:
    
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        
    def center(self):
        return ((self.x1 + self.x2) // 2, (self.y1 + self.y2) // 2)
    
    def intersect(self, other):
        return self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1
    
class Object:
    
    def __init__(self, map_):
        x, y = map_.get_actor_coords
        map_.set_coords(x, y, self)
        self.x = x
        self.y = y
        self.map_ = map_ 
        self.blocked = True
        
    @property
    def get_pos(self):
        return self.x, self.y    
        
    def move(self, dx, dy):       
        if not self.map_.is_blocked(self.x + dx, self.y + dy):
            reset_tile = Tile(False)
            old_x = self.x
            old_y = self.y
            self.x += dx
            self.y += dy
            self.map_.set_coords(self.x, self.y, self)
            self.map_.set_coords(old_x, old_y, reset_tile)
    
    def __str__(self):
        return "@"
            
class Goal:
    
    def __init__(self, map_):
        x, y = map_.get_goal_coords
        map_.set_coords(x, y, self)
        self.x = x
        self.y = y
        self.map_ = map_
        self.blocked = False
        self.picked = False
    
    def change_pos(self):
        self.x, self.y = self.map_.gen_new_goal_pos()
        self.map_.set_coords(self.x, self.y, self)
        self.picked = False
    
    @property
    def get_pos(self):
        return self.x, self.y
        
    def __str__(self):
        return "*"
    
class AI:
    
    def __init__(self, map_, actor, goal):
        self.map_ = map_
        self.actor = actor
        self.goal = goal
        self.moves = self.recompute_moves()
        #print(self.moves)
        
    def recompute_moves(self):
        self.stage = 0
        return search(self.map_, self.actor.get_pos, self.goal.get_pos)
    
    def get_closer(self):
        '''
        actor_x, actor_y = self.actor.get_pos
        goal_x, goal_y = self.goal.get_pos
        dx = goal_x - actor_x
        dy = goal_y - actor_y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        '''
        recompute = False
        actor_x, actor_y = self.actor.get_pos
        if not self.stage == len(self.moves):
            new_x, new_y = self.moves[self.stage]
            dx, dy = new_x - actor_x, new_y - actor_y
            self.actor.move(dx, dy)
            self.stage += 1
        else:
            self.goal.picked = True
            self.moves = self.recompute_moves()
        
class Map:
    
    def __init__(self, height, width, max_rooms, min_size, max_size):
        self.height = height
        self.width = width      
        self.max_rooms = max_rooms
        self.min_size = min_size
        self.max_size = max_size
        self.__passable = []
        self.__map = self.make_map()
        
    def is_blocked(self, x, y):
        return self.__map[x][y].blocked
    
    def set_coords(self, x, y, obj):
        self.__map[x][y] = obj
        
    def what_object(self, x, y):
        return self.__map[x][y]
    
    @property
    def get_actor_coords(self):
        try:
            return self.player_x, self.player_y
        except:
            print("Coords dont assigned for player")
            
    @property
    def get_goal_coords(self):
        try:
            return self.goal_x, self.goal_y
        except:
            print("Coords dont assigned for goal")
            
    def gen_new_goal_pos(self):
        self.goal_x, self.goal_y = choice(self.__passable)
        return self.goal_x, self.goal_y
    
    def create_h_tunnel(self, map_, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.__passable.append((x, y))
            map_[x][y].blocked = False

    def create_v_tunnel(self, map_, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.__passable.append((x, y))
            map_[x][y].blocked = False    

    def create_room(self, map_, room):
        for x in range(room.x1, room.x2 + 1):
            for y in range(room.y1, room.y2 + 1):
                self.__passable.append((x, y))
                map_[x][y].blocked = False

    def create_rooms(self, map_):
        
        def intersect_wall(room):
            return False
        
        rooms = []
        num_rooms = 0
        created = False
        while not num_rooms == self.max_rooms:       
            w = randint(self.min_size, self.max_size)
            h = randint(self.min_size, self.max_size)
            x = randint(2, self.width - w - 1)
            y = randint(2, self.height - h - 1)            
            new_room = Rect(x, y, w, h)
            failed = False
            for other_room in rooms:
                if new_room.intersect(other_room) or intersect_wall(other_room):
                    failed = True
                    break
            if not failed:
                self.create_room(map_, new_room) 
                (new_x, new_y) = new_room.center()
                if num_rooms == 0:
                    self.player_x = new_x
                    self.player_y = new_y                
                else:
                    if num_rooms == self.max_rooms - 1:
                        self.goal_x = new_x
                        self.goal_y = new_y                         
                    #all rooms after the first:
                    #connect it to the previous room with a tunnel

                    #center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms-1].center()

                    #draw a coin (random number that is either 0 or 1)
                    if randint(0, 2) == 1:
                        #first move horizontally, then vertically
                        self.create_h_tunnel(map_, prev_x, new_x, prev_y)
                        self.create_v_tunnel(map_, prev_y, new_y, new_x)
                    else:
                        #first move vertically, then horizontally
                        self.create_v_tunnel(map_, prev_y, new_y, prev_x)
                        self.create_h_tunnel(map_, prev_x, new_x, new_y)

                        #finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1
                
    def in_bounds(self, indexes):
        x, y = indexes
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, indexes):
        i, j = indexes
        return not self.__map[i][j].blocked
    
    def neighbors(self, indexes):
        x, y = indexes
        results = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0:
            results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results    

    def make_map(self):
        map_ = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        self.create_rooms(map_)
        return map_
    
    def show_map(self):
        for col in self.__map:
            for elem in col:
                print(elem, end = " ")
            print()
    
def main():
    MAP = Map(ROOM_WIDTH, ROOM_HEIGHT, MAX_ROOMS, MIN_SIZE, MAX_SIZE)
    actor = Object(MAP)
    goal = Goal(MAP)
    ai = AI(MAP, actor, goal)
    
    def move_actor(key):
        if key.upper() == "U":
            actor.move(-1, 0)
        elif key.upper() == "D":
            actor.move(1, 0)
        elif key.upper() == "L":
            actor.move(0, -1)    
        elif key.upper() == "R":
            actor.move(0, 1)
        elif key.upper() == "UL":
            actor.move(-1, -1)        
        elif key.upper() == "DR":
            actor.move(1, 1)
        elif key.upper() == "DL":
            actor.move(1, -1)
        elif key.upper() == "UR":
            actor.move(-1, 1)
        elif key.upper() == "A":
            ai.get_closer()
    
    while 1:
        if goal.picked:
            goal.change_pos()
        clear_console()
        MAP.show_map()
        ai.get_closer()
        time.sleep(0.1)
        #move_actor(input())
        
if __name__ == "__main__":
    main()