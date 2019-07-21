class Memoize:
    
    def __init__(self, func):
        self.calls = dict()
        self.func = func
        
    def __call__(self, arg):
        call_try = self.calls.get(arg, "$#nonefalse#&")
        if call_try != "$#nonefalse#&":
            return call_try
        else:
            res = self.func(arg)
            self.calls[arg] = res
            return res
        
    def look(self):
        return self.calls
    
@Memoize    
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_non_memoized(n):
    if n < 2:
        return n
    return fib_non_memoized(n - 1) + fib_non_memoized(n - 2)
    
print(fib.look())
print(fib(5))
print(fib(7))
print(fib(20))
print(fib(200))
print('memoized', fib(529))
print("non memoized", fib_non_memoized(200))


