class Accumulator:
    
    def __init__(self, start):
        self.state = start
        
    def __str__(self):
        return str(self.state)
    
    def __call__(self, amount):
        self.state += amount

def make_accumulator(start):
    return Accumulator(start)

def keeper(val):
    return lambda: val

def make_accumulator_(val = None):
    if val:
        return val
    else:
        return keeper(val)

b = keeper(3)
print(b())

A = make_accumulator(5)
print(A)
A(5)
print(A)
A(5)
print(A)
'''
def make_accumulator_(start):
    state = start
    state = lambda amount: state + amount
    return state

A =  make_accumulator_(5)
print(A(5))
print(A(5))
'''

A = make_accumulator_(5,)
print('new', A())