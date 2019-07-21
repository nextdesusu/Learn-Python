from math import log

class Counter:
    
    def __init__(self, start):
        self.count = start
    
    def inc(self):
        self.count += 1
        
    def __str__(self):
        return str(self.count)

counter1 = Counter(0)
counter2 = Counter(0)


def fixed_point(f, first_guess, count):
    tolerance = 0.00001
    close_enough = lambda v1, v2: abs(v1 - v2) < tolerance
    
    def try_(guess):
        count.inc()
        print("{0} of {1} = {2}".format("next", f.__name__, f(guess)))
        next_ = f(guess)
        if close_enough(guess, next_):
            return next_
        return try_(next_)
    
    return try_(first_guess)

l = lambda x: log(1000) / log(x)
average = lambda x, y: (x + y) / 2
l_av = lambda x: average(log(1000) / log(x), x)

print(fixed_point(l, 2, counter1), counter1)
print(fixed_point(l_av, 2, counter2), counter2) #More than 3 times faster
    
