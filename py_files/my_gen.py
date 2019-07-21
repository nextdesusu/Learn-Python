class generator:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    
    def __call__(self):
        if self.start == self.end:
            return None        
        res = self.start
        self.start += self.step
        return res
    
                
        
new_gen = generator(0, 10, 1)

print(new_gen())
print(new_gen())
print(new_gen())
print(new_gen())
print(new_gen())
print(new_gen())
        