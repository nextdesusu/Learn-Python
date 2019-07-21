class Interval:
    
    def __init__(self, lb, ub):
        self.lower_bound = lb
        self.upper_bound = ub
        
    def __str__(self):
        return "[{}|{}]".format(self.lower_bound, self.upper_bound)
    
def make_interval(x, y):
    return Interval(x, y)

def add_interval(x, y):
    return make_interval((x.lower_bound + y.lower_bound), (x.upper_bound + y.upper_bound))

def sub_interval(x, y):
    return make_interval((x.lower_bound - y.upper_bound), (x.upper_bound -  y.lower_bound))

def mul_interval(x, y):
    p1 = x.lower_bound * y.lower_bound
    p2 = x.lower_bound * y.upper_bound
    p3 = x.upper_bound * y.lower_bound
    p4 = x.upper_bound * y.upper_bound
    print(p1, p2, p3, p4)
    print("max: ", max(p1, p2, p3, p4), "min: ", min(p1, p2, p3, p4))
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def mul_interval_sp(x, y):
    
    if x.upper_bound < y.upper_bound:
        p_m = x.upper_bound * y.upper_bound
        p_s = x.lower_bound * y.lower_bound
        
    return make_interval(p_m, p_s)




def div_interval(x, y):
    if (y.upper_bound + y.lower_bound) == abs(y.upper_bound + y.lower_bound) and y.upper_bound != 0 and y.lower_bound != 0:
        return mul_interval(x, make_interval((1 / y.upper_bound), (1 / y.lower_bound)))
    raise 1/0

def width_interval(x):
    return abs(x.upper_bound - x.lower_bound) / 2

def check(int1, int2):
    print("Interval1: ", width_interval(int1), "Interval2: ", width_interval(int2))
    print("Add: ", width_interval(add_interval(int1, int2)), width_interval(int1) + width_interval(int2))
    print("Sub: ", width_interval(sub_interval(int1, int2)), width_interval(int1) - width_interval(int2))
    print("Mul: ", width_interval(mul_interval(int1, int2)), width_interval(int1) * width_interval(int2))
    print("Div: ", width_interval(div_interval(int1, int2)), width_interval(int1) / width_interval(int2))

b = make_interval(2, 10)
b_1 =make_interval(3, 4)
c = make_interval(3, 12)
c_1 = make_interval(2, 8)
d = make_interval(-12, 3)
#print(width_interval(mul_interval(b, d)))
#check(b, c)
print(width_interval(mul_interval_sp(b_1, c_1)))

#2.11 not eaquted