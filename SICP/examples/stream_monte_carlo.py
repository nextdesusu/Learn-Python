from random import randint
from math import sqrt

def stream_map(proc, stream):
    next_ = next(stream)
    while next_:
        yield proc(next_)
        next_ = next(stream)

def gcd(x, y): 

    while(y): 
        x, y = y, x % y 

    return x 

def random_numbers():
    while True:
        yield randint(1, 1001)
        
def cesaro_stream():
    return map_succesive_pairs(lambda r1, r2: gcd(r1, r2) == 1, random_numbers())
        
def map_succesive_pairs(f, s):
    call1, call2 = next(s), next(s)
    while call1 and call2: 
        yield f(call1, call2)
        call1, call2 = next(s), next(s)

def monte_carlo(experiment_stream, passed, failed):
    
    def next_(passed, failed):
        yield passed / (passed + failed)
        for elem in monte_carlo(experiment_stream, passed, failed):
            yield elem
            
    if next(experiment_stream):
        return next_(passed + 1, failed)
    else:
        return next_(passed, failed + 1)
    
def monte_carlo(experiment_stream):
    next_ = next(experiment_stream)
    passed = 0
    failed = 0
    while True:
        if next_:
            passed += 1
        else:
            failed += 1
        yield passed / (passed + failed)
        next_ = next(experiment_stream)
    
def pi():
    return stream_map(lambda p: sqrt(6 / p), monte_carlo(cesaro_stream()))
        
for num in pi():
    print(num)
