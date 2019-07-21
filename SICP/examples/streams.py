done = 'done'

class cons:
    
    def __init__(self, x, y = '()'):
        self.car = x
        self.cdr = y
        
    def set_car(self, x):
        self.car = x
        
    def set_cdr(self, y):
        self.cdr = y
        
    def is_null(self):
        return self.cdr == '()'
        
    def __str__(self):
        return "({}, {})".format(self.car, self.cdr)
    
def car(cons):
    return cons.car

def cdr(cons):
    return cons.cdr

def set_car(cons, x):
    return cons.set_car(x)

def set_cdr(cons, y):
    return cons.set_cdr(y)

def stream_null(cons_stream):
    return cons_stream.is_null()

def stream_ref(s, n):
    if n == 0:
        return stream_car(s)
    return stream_ref(stream_cdr(s), n - 1)

def stream_map(proc, s):
    if stream_null(s):
        return the_empty_stream()
    return cons_stream(proc(stream_car(s)), stream_map(proc, stream_cdr(s)))

def stream_for_each(proc, s):
    if stream_null(s):
        return done
    proc(stream_car(s))
    return stream_for_each(proc, stream_cdr(s))

def display_stream(s):
    return stream_for_each(display_line, s)

def display_line(x):
    print()
    print(x, end = '')
    
def cons_stream(a, b):
    return cons(a, delay(b))

def stream_car(stream):
    return car(stream)

def stream_cdr(stream):
    return force(cdr(stream))

def stream_enumerate_interval(low, high):
    if low > high:
        return the_empty_stream()
    return cons_stream(low, stream_enumerate_interval(low + 1), high)

def the_empty_stream():
    return '()'

def stream_filter(pred, stream):
    if stream_null(stream):
        return the_empty_stream()
    elif pred(stream_car(stream)):
        return cons_stream(stream_car(stream),
                           stream_filter(pred,
                                         stream_cdr(stream)))
    else:
        return stream_filter(pred, stream_cdr(stream))

class MEM:
    memory = dict()
    
    def __call__(self, func):
        if not func in self.memory:
            self.memory[func] = func
        return self.memory[func]
    
    def mem(self, func):
        self.memory[func] = func
    
memo_proc = MEM()

def force(delayed_object):
    return delayed_object()

def delay(exp):
    return memo_proc(exp)

def stream_map(proc, s):
    if stream_null(s):
        return the_empty_stream()
    return cons_stream(proc(stream_car(s)), stream_map(proc, stream_cdr(s)))

def apply(proc, list_):
    while not cdr(list_) == '()':
        proc(car(list_))

def stream_map(proc, *argsreams):
    if stream_null(argstreams[0]):
        return the_empty_stream()
    return cons_stream(apply(proc, map_(stream_car, argstreams)),
                       apply(stream_map(cons, proc(map_(stream_cdr, argstreams)))))

def integers_starting_from(n):
    return cons_stream(n, integers_starting_from(n + 1))

def divisible(x, y):
    return x % y == 0

def no_sevens():
    return stream_filter(lambda x: not divisible(x, 7), integers)

def fib_gen(a, b):
    return cons_stream(a, fib_gen(b, a + b))

def fib_gen(a, b):
    yield cons_stream(a, fib_gen(b, a + b))

def integers_starting_from(n):
    yield cons_stream(n, integers_starting_from(n + 1))
    
def stream_ref(s, n):
    if n == 0:
        return stream_car(s)
    return stream_ref(stream_cdr(s), n - 1)

def stream_car(stream):
    return car(next(stream))

def stream_cdr(stream):
    print('call', stream)
    return cdr(next(stream))

def sieve(stream):
    yield cons_stream(stream_car(stream), sieve(stream_filter(lambda x: divisible(x, stream_car(stream)), stream_cdr(stream))))
'''
integers = integers_starting_from(1)
fibs = fib_gen(0, 1)
primes = sieve(integers_starting_from(2))
print(stream_ref(primes, 10))
'''
def add_streams(s1, s2):
    return stream_map(lambda x, y: x + y, s1, s2)

def ones_():
    yield cons_stream(1, ones)
    
ones = ones_()
print(stream_ref(ones, 9))

integers = cons_stream(1, add_streams(ones, integers))


def intsfrom(n):
    while True:
        yield n
        n += 1

def sieve(ilist):
    p = next(ilist)
    yield p
    for q in sieve(n for n in ilist if n % p != 0):
        yield q


def stream_ref(stream, n):
    for i, elem in enumerate(stream):
        if i == n:
            return elem