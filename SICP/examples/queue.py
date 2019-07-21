class Cons:
    
    def __init__(self, x, y):
        self.car = x
        self.cdr = y
        
    def set_car(self, x):
        self.car = x    
        
    def set_cdr(self, y):
        self.cdr = y
        
    def __str__(self):
        return "({0}, {1})".format(self.car, self.cdr)
    
def list_(*args):
    
    def iter_(args):
        if not len(args):
            return "()"
        return Cons(args[0], iter_(args[1::]))
    
    return iter_(args)
    
def car(pair):
    return pair.car

def cdr(pair):
    return pair.cdr

def set_cdr(pair, new):
    pair.set_cdr(new)
    
def set_car(pair, new):
    pair.set_car(new)    

def pair(x):
    return isinstance(x, Cons)

def last_pair(x):
    state = x
    while True:
        if pair(cdr(state)):
            state = cdr(state)
        else:
            return state

def count_pairs_old(x):
    if not pair(x):
        return 0
    return count_pairs(car(x)) + count_pairs(cdr(x)) + 1

def count_pairs(x):
    state = x
    counter = 0
    while pair(state):
        if pair(car(state)):
            counter += count_pairs(car(state))
        counter += 1
        state = cdr(state)
    return counter

def make_cycle(x):
    set_cdr(last_pair(x), x)
    return x

def is_infinity(x):
    first_elem = car(x)
    set_car(x, "#stop")
    state = cdr(x)
    while pair(state):
        if car(state) == "#stop":
            set_car(x, first_elem)
            return True
        else:
            state = cdr(state)
    set_car(x, first_elem)
    return False

def front_ptr(queue):
    return car(queue)

def rear_ptr(queue):
    return cdr(queue)

def set_front_ptr(queue, item):
    set_car(queue, item)

def set_rear_ptr(queue, item):
    set_cdr(queue, item)

def empty_queue(queue):
    return front_ptr(queue) == "()" and rear_ptr(queue) == "()" 

def make_queue():
    return Cons("()", "()")

def front_queue(queue):
    if empty_queue(queue):
        raise Exception("EMPTY QUEUE")
    return car(front_ptr(queue))

def insert_queue(queue, item):
    new_pair = Cons(item, "()")
    if empty_queue(queue):
        set_front_ptr(queue, new_pair)
        set_rear_ptr(queue, new_pair)
    else:
        set_cdr(rear_ptr(queue), new_pair)
        set_rear_ptr(queue, new_pair)
    return queue

def delete_queue(queue):
    if empty_queue(queue):
        raise Exception("Called with empty stack" + str(queue))
    else:
        set_front_ptr(queue, cdr(front_ptr(queue)))
    return queue
    
a = make_queue()
print(a)
insert_queue(a, 5)
print(a)
insert_queue(a, 4)
print(a)
insert_queue(a, 3)
print(a)
insert_queue(a, 2)
print(a)
delete_queue(a)
print(a)