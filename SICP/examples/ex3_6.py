class Rand:
    
    def rand_update(self, x):
        a, b, m = 27, 26, 127
        return ((a * x) + b) % m    
    
    def __init__(self, num):
        self.state = num
        
    def generate(self):
        self.state = self.rand_update(self.state)
        return self.state
    
    def reset(self, n):
        self.state = n
    
    def __call__(self):
        return self.state
    
rand1 = Rand(-100)