def accumulate(op, initial, sequence):
    if not len(sequence):
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1::]))

class Cons:
    
    def __init__(self, x, y):
        self.car = x
        self.cdr = y
        
    def __str__(self):
        return '({}, {})'.format(self.car,  self.cdr)
    
    
def map_(p, sequence):
    return accumulate(lambda x, y: Cons(p(x), y), 'nil', sequence)

def append_(sequence1, sequence2):
    return accumulate(Cons, sequence2, sequence1)

def length_(sequence):
    return accumulate(lambda x, y: y + 1, 0, sequence)

print(map_(lambda x: x + 1, [1, 2, 3]))
print(append_([1, 2, 3], [4, 5, 6]))
print(length_([1, 2, 3, 4, 5, 6, 7]))