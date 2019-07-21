average = lambda x, y: (x + y) / 2

def sqrt_improve(guess, x):
    return average(guess, x / guess)

def stream_map(proc, stream):
    elem = next(stream)
    while elem:
        yield proc(elem)
        elem = next(stream)  

def sqrt_stream(x):
    
    def guesses():
        yield 1
        for elem in stream_map(lambda guess: sqrt_improve(guess, x), guesses()):
            yield elem
    
    return guesses()

def stream_limit(stream, tolerance):
    
    def good_enough(x, y):
        return abs(x - y) < tolerance
    
    prev_elem = next(stream)
    current_elem = next(stream)
    
    while current_elem and not good_enough(prev_elem, current_elem):
        
        prev_elem = next(stream)
        current_elem = next(stream) 
        
    return current_elem

def sqrt(x, tolerance):
    return stream_limit(sqrt_stream(x), tolerance)

print(sqrt(9, 0.0000000001))