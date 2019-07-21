class Interval:
    
    def __init__(self, lb, ub):
        self.lower_bound = lb
        self.upper_bound = ub
        
    def __str__(self):
        return "[{}|{}]".format(self.lower_bound, self.upper_bound)
    
def make_center_width(c, w):
    return Interval(c - w, c + w)

def center(i):
    return (i.lower_bound + i.upper_bound) / 2

def width(i):
    return (i.upper_bound - i.lower_bound) / 2

def percent(i):
    difference = (i.upper_bound - i.lower_bound) / 2
    m_val = i.lower_bound + difference
    return (difference / m_val) * 100

def make_center_percent(i, p):
    return Interval(i - (i / 100) * p, i + (i / 100) * p)

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

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = make_interval(1, 1)
    return div_interval(one, add_interval(div_interval(one, r1), div_interval(one, r2)))

a = make_center_percent(10, 2)
b = make_center_percent(12, 4)

#print(par1(a, b))
#print(par2(a, b))