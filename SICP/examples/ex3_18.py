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

no_inf_list = list_(1, 2, 3)
inf_list = list_(1, 2, 3)
inf_list = make_cycle(inf_list)
print(is_infinity(no_inf_list))
print(is_infinity(inf_list))
#print(inf_list)