def square(x):
    return x * x

def average(x, y):
    return (x + y) / 2

def better_good_enough(guess, prev_guess):
    return abs((guess - prev_guess) / prev_guess) < 0.001

def improve(guess, x):
    return average(guess, x / guess)

def better_sqrt_iter(guess, prev_guess, x):   
    if better_good_enough(guess, prev_guess):
        return guess
    else:
        return better_sqrt_iter(improve(guess, x), guess, x)
    
def my_sqrt(x):
    return better_sqrt_iter(1, 0.5, x)
    
print("result", my_sqrt(4))