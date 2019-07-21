all_delayed = dict()

def stream_map(proc, stream):
    elem = next(stream)
    while elem:
        yield proc(elem)
        elem = next(stream) 

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

def delay(some):
    
    class Delayed:
        
        def __init__(self, obj):
            self.delayed = obj
            
        def grab(self, func):
            all_delayed[self.delayed] = func
            
        def force(self):
            return all_delayed[self.delayed]
    
    return Delayed(some)

def force(some):
    return some.force()

def integral(delayed_integrand, initial_value, dt):
    
    def int_():
        yield initial_value
        integrand = force(delayed_integrand)
        for elem in add_streams(scale_stream(integrand, dt), int()):
            yield elem
            
    return int_()

def solve(f, y0, dt):
    delayed_dy = delay('dy')
    y = integral(delayed_dy, y0, dt)
    dy = stream_map(f, y)
    delayed_dy.grab(dy)
    return y
    
for i in solve(lambda x: x, 1, 0.001):
    print(i)