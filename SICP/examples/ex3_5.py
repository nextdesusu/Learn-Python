from random import randint

def random(y):
    return randint(0, y)

def random_in_range(low, high):
    range_ = high - low
    return low + random(range_)

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

print(pi_approx())