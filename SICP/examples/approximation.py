def average(x, y):
    return (x + y) / 2

def sqrt_improve(guess, x):
    return average(guess, x / guess)

def sqrt_stream(x):
    
    def guesses():
        yield 1
        for elem in stream_map(lambda guess: sqrt_improve(guess, x), guesses()):
            yield elem
    
    return guesses()

def stream_map(proc, stream):
    elem = next(stream)
    while elem:
        yield proc(elem)
        elem = next(stream)  
        
#for i in sqrt_stream(2):
#    print(i)

'''
def partial_sums(stream):
    
    def get_part_sums(stream, n):
        sum_src = stream
        sum_ = next(sum_src)
        for i in range(n):
            if i % 2 == 0:
                sum_ = next(sum_src)
            else:
                sum_ -= next(sum_src)
        return sum_
    
    n = 0
    while 1:
        yield get_part_sums(stream, n)
        n += 1
'''
        
def partial_sums(stream):
    accum = 0
    elem = next(stream)
    while elem:
        accum += elem
        yield accum
        elem = next(stream)

def scale_stream(stream, factor):
    call = next(stream)
    while call:
        yield call * factor
        call = next(stream)

def pi_summands(n):
    yield 1 / n
    for elem in stream_map(lambda x: -x, pi_summands(n + 2)):
        yield elem
        
def pi_stream(n):
    return scale_stream(partial_sums(pi_summands(n)), 4)
    
def stream_ref(stream, n):
    elem = next(stream)
    for i in range(n):
        elem = next(stream)
    return elem      

square = lambda x: x * x
    
def euler_transform(s):
    s0 = next(s)
    s1 = next(s)
    s2 = next(s) 
    yield s2 - (square(s2 - s1) / (s0 + (-2 * s1) + s2))
    for elem in euler_transform(s):
        yield elem
        
def make_tableau(transform, s):
    yield next(s)
    for elem in make_tableau(transform, transform(s)):
        yield elem
        
def accelerated_sequence(transform, s):
    return stream_map(lambda x: x, make_tableau(transform, s))

#for i in accelerated_sequence(euler_transform, pi_stream(1)):
#    print(i)

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


def l2_summands(n):
    yield 1 / n
    for elem in stream_map(lambda x: -x, l2_summands(n + 1)):
        yield elem

def l2():
    return partial_sums(l2_summands(1))   

print(sqrt(4, 0.0000000001))        
for elem in accelerated_sequence(euler_transform, l2()):
    print(elem)
    