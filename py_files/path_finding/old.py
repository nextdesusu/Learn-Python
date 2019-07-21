from random import choice, randint

class Tile:
    
    def __init__(self, blocked):
        self.blocked = blocked
        
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
        

break_symbol = "#"
player_symbol = "*"
can_pass_symbol = "-"
goal_symbol = "$"
randomizer_functions = (lambda x: x % 2 != 0, lambda x: x % 3 != 0)

def create_map(pointX, pointY, width, height):
    if pointX == 0 or pointX == width - 1 or pointY == 0 or pointY == height - 1 or pointX >= width or pointY >= height:
        raise Exception("cannot assigtn pointX: {}, pointY: {}".format(pointX, pointY))
    
    randX, randY = randint(1, width - 2), randint(1, height - 2)
    randomWay1 = randint(1, width - 2) 
    
    def is_goal_pos(i, j):
        return i == randX and j == randY
    
    def is_player_pos(i, j):
        return i == pointX and j == pointY
    
    def can_pass_pos(i, j):
        return (not is_player_pos(i, j)) and (not is_goal_pos(i, j)) and (i < width - 1 and j < height - 1) and (i != 0 and j != 0)
        
    def assign_elem(i, j):
        if is_player_pos(i, j):
            return player_symbol
        elif is_goal_pos(i, j):
            return goal_symbol
        elif can_pass_pos(i, j):
            return can_pass_symbol
        else:
            return break_symbol
        
    choosen_func = choice(randomizer_functions)
    map_ = [[assign_elem(i, j) for i in range(width)] for j in range(height)]
    '''
    print("before")
    show_map(map_)
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if choosen_func(i) and not is_player_pos(i, j) and not is_goal_pos(i, j):
                map_[i][j] = break_symbol
    
    print("after")
    show_map(map_)
    '''
    return map_

def find_player(map_):
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == player_symbol:
                return i, j
    raise Exception("player not found")

def find_goal(map_):
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == goal_symbol:
                return i, j
    raise Exception("goal not found")

def show_map(map_):
    print("player in:", find_player(map_), "goal_in:", find_goal(map_))
    for set_ in map_:
        for elem in set_:
            print(elem, end = " ")
        print()
    print()
        
def move(map_, previousX, previousY, nowX, nowY):
    if map_[nowX][nowY] != break_symbol:
        map_[previousX][previousY] = can_pass_symbol
        map_[nowX][nowY] = player_symbol
    else:
        return "cant move"
    
def move_to_direction(key):
    now_player_coords = find_player(map_)
    if key == "U":     
        return move(map_, now_player_coords[0], now_player_coords[1], now_player_coords[0] - 1, now_player_coords[1]) 
    elif key == "D":     
        return move(map_, now_player_coords[0], now_player_coords[1], now_player_coords[0] + 1, now_player_coords[1])
    elif key == "R":     
        return move(map_, now_player_coords[0], now_player_coords[1], now_player_coords[0], now_player_coords[1] + 1)
    elif key == "L":     
        return move(map_, now_player_coords[0], now_player_coords[1], now_player_coords[0], now_player_coords[1] - 1)    
    
map_width = 19
map_height = 19
playerX = randint(1, map_width - 2)
playerY = randint(1, map_height - 2)
map_ = create_map(playerX, playerY, map_width, map_height)

show_map(map_)
move_to_direction("U")
show_map(map_)
move_to_direction("D")
show_map(map_)
move_to_direction("L")
show_map(map_)