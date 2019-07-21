def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, (a % b))

class Rational_number:
    
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    def __str__(self):
        return "{0}/{1}".format(self.numer, self.denom)
    
class cons:
    
    def __init__(self, car, cdr):
        self.car = car
        self.cdr = cdr
        
    def __str__(self):
        return "({0}, {1})".format(self.car, self.cdr)  
    
def make_rat(n, d):
    if d == 0:
        raise (1 / 0) #Your denom == 0
    
    def sign(num, den):
        if num < 0 or den < 0:
            return -1
        if num == 0:
            return 0
        else:
            return 1
    
    s = sign(n, d)
    g = gcd(abs(n), abs(d)) 
    numer = (abs(n) / g) * s
    denom = abs(d) / g
    if denom == int(denom):
        denom = int(denom)
    if numer == int(numer):
        numer = int(numer)       
    return Rational_number(numer, denom)
    
def add_rat(x, y):
    return make_rat(((x.numer * y.denom) + (y.numer * x.denom)), (x.denom * y.denom))

def sub_rat(x, y):
    return make_rat(((x.numer * y.denom) - (y.numer * x.denom)), (x.denom * y.denom))

def mul_rat(x, y):
    return make_rat((x.numer * y.numer), (x.denom * y.denom))

def div_rat(x, y):
    return make_rat((x.numer * y.denom), (x.denom * y.numer))

def equal_rat(x, y):
    return (x.numer * y.denom) == (y.numer * x.denom)

#one_half = make_rat(1, 2)
#one_third = make_rat(1, 3)

#print(add_rat(one_half, one_third))
#print(mul_rat(one_half, one_third))
#print(add_rat(one_third, one_third))