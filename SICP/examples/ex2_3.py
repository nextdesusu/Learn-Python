from ex2_2 import *

class Rectangle:
    
    def __init__(self, a, b, c, d):
        self.x_point = a
        self.y_point = b
        self.z_point = c
        self.d_point = d
        
    def square(self):
        return self.x_point * self.y_point
    
    def perimetr(self):
        return (self.x_point + self.y_point) * 2
        
    def __str__(self):
        return "|a: {}, b: {}, c: {}, d: {}|".format(self.x_point, self.y_point, self.z_point, self.d_point)
    
q = Rectangle(2, 2, 2, 2)
d = Rectangle(1, 5, 2, 2)

print(midpoint_segment(tr, d))
