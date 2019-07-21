class recursion():
    __slots__ = ["func"]
        
    "Can call other methods inside..."
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        while callable(result):
            result = result()
        return result

    def call(self, *args, **kwargs):
        return lambda: self.func(*args, **kwargs)
    
#Can be used to optimise recursion by transforming it in to cycle
#If you want to use it you have to import it by writing: import rec
#and then use as a decorator: @rec.recursion
    
