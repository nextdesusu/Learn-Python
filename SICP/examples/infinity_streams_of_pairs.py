from random import randint

def scale_stream(stream, factor):
    call = next(stream)
    while call:
        yield call * factor
        call = next(stream)
        
def add_streams(s1, s2):
    elem1, elem2 = next(s1), next(s2)
    while elem1 and elem2:
        yield elem1 + elem2
        elem1, elem2 = next(s1), next(s2)
        
def stream_filter(pred, stream):
    elem = next(stream)
    while elem:
        if pred(elem):
            yield elem
        elem = next(stream)

def stream_map(proc, stream):
    elem = next(stream)
    while elem:
        yield proc(elem)
        elem = next(stream)  

def integers():
    n = 1
    while True:
        yield n
        n += 1
        
def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def interleave(s1, s2):
    yield next(s1)
    for elem in interleave(s2, s1):
        yield elem
        
def pairs(s, t):
    next_s, next_t = next(s), next(t)
    yield next_s, next_t
    for elem in interleave(stream_map(lambda x: (next_s, x), t), pairs(s, t)):
        yield elem

#for pair in pairs(integers(), integers()):
#    print(pair)

#for num in stream_filter(lambda pair: is_prime(pair[0] + pair[1]), pairs(integers(), integers())):
#    print(num)

def all_pairs(s, t):
    next_s, next_t = next(s), next(t)
    yield next_s, next_t
    for elem in interleave(interleave(stream_map(lambda x: (next_s, x), t), all_pairs(s, t)), stream_map(lambda x: (next_t, x), s)):
        yield elem
        
#for pair in all_pairs(integers(), integers()):
#    print(pair)

def hugo_pairs(s, t):
    for elem in interleave(stream_map(lambda x: (next(s), x), t), hugo_pairs(s, t)):
        yield elem
        
#for pair in hugo_pairs(integers(), integers()):
#    print(pair)
    
def triples(s, t, m):
    next_s, next_t, next_m = next(s), next(t), next(m)
    yield next_s, next_t, next_m
    for elem in interleave(stream_map(), triples(s, t, m)):
        yield elem 
        
def merge(s1, s2):
    next_s1, next_s2 = next(s1), next(s2)
    while next_s1 and next_s2:
        if next_s1 < next_s2:
            yield next_s1
            next_s1 = next(s1)
        elif next_s1 > next_s2:
            yield next_s2
            next_s2 = next(s2)
        else:
            yield next_s1
            next_s1, next_s2 = next(s1), next(s2)
            

def merge_weighted(s1, s2, weight):
    next_s1, next_s2 = next(s1), next(s2)
    while next_s1 and next_s2:
        if weight(next_s1) < weight(next_s2):
            yield next_s1
            next_s1 = next(s1)
        elif weight(next_s1) < weight(next_s2):
            yield next_s2
            next_s2 = next(s2)
        elif weight(next_s1) and weight(next_s2):
            yield next_s1
            next_s1, next_s2 = next(s1), next(s2)            
        else:
            next_s1, next_s2 = next(s1), next(s2)
            
def random_pairs():
    while True:
        yield (randint(1, 10001), randint(1, 10001))
        
def weight_func(x):
    dels = (2, 3, 5)
    for del_ in dels:
        if x % del_== 0:
            return False
    return True

def Ramajan_numbers():
    
    memory = dict()
    ramajan_nums = []
    
    cube = lambda x: x * x * x
    
    sum_cubes = lambda pair: cube(pair[0]) + cube(pair[1])   
    
    def unique_pairs():
        j = 0
        while True:
            for i in range(0, j + 1):
                yield i, j
            j += 1    
            
    for pair in unique_pairs():
        cube_sum = sum_cubes(pair)
        if not cube_sum in memory:
            memory[cube_sum] = True
        else:
            ramajan_nums.append(cube_sum)
            print(ramajan_nums)
            
#Ramajan_numbers()

def integral(integrand, initial_value, dt):
    
    def int_():
        yield initial_value
        for elem in add_streams(scale_stream(integrand, dt), int_()):
            yield elem
            
    return int_()

for num in integral(integers(), 1, 5):
    print(num)
    