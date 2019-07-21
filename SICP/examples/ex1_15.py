class Counter:
    
    def __init__(self, start):
        self.state = start
        
    def inc(self):
        self.state += 1
        
    def show(self):
        print(self.state)
        
counter = Counter(0)

def cube(x):
    return x * x * x

def p(x):
    counter.inc()
    return (3 * x) - (4 * cube(x))

def sine(angle):
    if not abs(angle) > 0.1:
        return angle
    return p(sine(angle / 3.0))

    


print(sine(12.15))
counter.show()