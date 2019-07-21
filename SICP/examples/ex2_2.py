class MakeSegment:
    
    def __init__(self, x, y):
        if x == int(x):
            x = int(x)
        if y == int(y):
            y = int(y)        
        self.x_point = x 
        self.y_point = y
        
    def __str__(self):
        return "[x: {0}|y: {1}]".format(self.x_point, self.y_point)
    
def midpoint_segment(p1, p2):
    return MakeSegment((p1.x_point + p2.x_point) / 2, (p1.y_point + p2.y_point) / 2)
    
    
tt = MakeSegment(10, 3)
tr = MakeSegment(1, 23)
ne = midpoint_segment(tt, tr)
#print(ne)