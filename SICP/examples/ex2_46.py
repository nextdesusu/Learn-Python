class Vector:
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise Exception('Not a vector')
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise Exception('Not a vector')
        
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        else:
            raise Exception('Not a number')        
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
a = Vector(2, 3)
b = Vector(1, 5)
print(a * 3.1)