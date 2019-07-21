from math import sqrt
from random import randint

def random(y):
    return randint(0, y)

def rand_update(x):
    a, b, m = 27, 26, 127
    return ((a * x) + b) % m

def random_init():
    #2 ** 32
    return rand_update(2 ** 12)

def random_in_range(low, high):
    range_ = high - low
    return low + random(range_)

class Rand:
    
    def __init__(self):
        self.state = random_init()
        
    def generate(self):
        self.state = rand_update(self.state)
        return self.state
    
    def reset(self, n):
        self.state = n
    
    def __call__(self):
        return self.state

rand = Rand()

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b% a
    return a + b

def random_gcd_test(trials, initial_x):
    
    def iter_(trials_remaining, trials_passed, x):
        x1 = rand_update(x)
        x2 = rand_update(x1)
        if trials_remaining == 0:
            return trials_passed / trials
        elif gcd(x1, x2) == 1:
            return iter_(trials_remaining - 1, trials_passed + 1, x2)
        else:
            return iter_(trials_remaining - 1, trials_passed, x2)
        
    return iter_(trials, 0, initial_x)

def estimate_pi(trials):
    return sqrt(6 / random_gcd_test(trials, random_init()))

def estimate_pi(trials):
    return sqrt(6 / monte_carlo(trials, cesaro_test))

def cesaro_test():
    return gcd(rand.generate(), rand.generate()) == 1

def monte_carlo(trials, expiriment):
    
    def iter_(trials_remaining, trials_passed):
        if trials_remaining == 0:
            return trials_passed / trials
        elif expiriment():
            return iter_(trials_remaining - 1, trials_passed + 1)
        else:
            return iter_(trials_remaining - 1, trials_passed)
        
    return iter_(trials, 0)

def Predicate(x, y):
    return (x - 5) ** 2 + (y - 7) ** 2 <= 3 ** 2

def estimate_integral(P, x1, x2, y1, y2, trials):
    square = x1 * x2 * y1 * y2
    
    def expirement():
        return P(random_in_range(x1, x2), random_in_range(y1, y2))
    
    return monte_carlo(trials, expirement)

def pi_approx():
    return (estimate_integral(Predicate, 2.0, 8.0, 4.0, 10.0, 500) * 36) / 9
