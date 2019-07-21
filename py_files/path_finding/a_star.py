from queue import Queue

map_ = [[False for i in range(10)] for j in range(10)]
start = map_[0][0]
frontier = Queue()
frontier.put(start )
came_from = {}
came_from[start] = None

goal = map_[6][6]

while not frontier.empty():
    current = frontier.get()

    if current == goal: 
        break           

    for next_ in graph.neighbors(current):
        if next_ not in came_from:
            frontier.put(next_)
            came_from[next_] = current