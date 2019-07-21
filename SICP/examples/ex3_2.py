class Counter:
    
    def __init__(self, func, calls = 0):
        self.func = func
        self.calls = calls
        
    def __call__(self, arg):
        self.calls += 1
        res = self.func(arg)
        if callable(res):
            return res
        else:
            return Counter(res, self.calls)
        
    def show_res(self):
        return self.func
        
    def how_many_calls(self):
        return self.calls
    
@Counter
def iter_(times):
    if times == 1:
        return 'kek'
    return iter_(times - 1)

#monitored_func = make_monitored(iter_(10))
#print(monitored_func("how-many-calls?"))
#monitored_func = monitored_func.call(10)
print(iter_(122).how_many_calls())
