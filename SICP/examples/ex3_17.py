class Cons:
    
    def __init__(self, x, y):
        self.car = x
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

def pair(x):
    return isinstance(x, Cons)

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

a = list_(1, 2, 4, 6, 7)
print(count_pairs(a))