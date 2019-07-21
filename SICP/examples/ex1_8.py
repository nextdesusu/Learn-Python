def qbrt(x):
    qube = lambda x: x * x * x
    square = lambda x: x * x
    
    def qbrt_iter(guess, x):
        
        def good_enough(guess, x):
            return abs(qube(guess) - x) < 0.001
        
        def improve(guess, x):
            return ((x / square(guess)) + 2 * guess) / 3
        
        if good_enough(guess, x):
            return guess
        
        return qbrt_iter(improve(guess, x), x)
    
    return qbrt_iter(1, x)

print(qbrt(125))
    
    