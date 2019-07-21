def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

#print(gcd(50, 130))

class Complex:
    
    def __init__(self, real, imag = 0):
        self.real = real
        self.imag = imag
        
    def __str__(self):
        return '{0} + {1}i'.format(self.real, self.imag)
    
class Rational:
    
    def __init__(self, n, m):
        self.n = n
        if m == 0:
            raise 1 / 0
        self.m = m
    
    @property
    def equate(self):
        return self.n / self.m
    
    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational((self.n + other.n) / gcd(self.n + other.n, self.m + other.m),
                            (self.m + other.m) / gcd(self.n + other.n, self.m + other.m))
        
    def __str__(self):
        return '{0} / {1}'.format(self.n, self.m)

def raise_(num):
    if isinstance(num, int):
        return Rational(num, 1)
    if isinstance(num, Rational):
        return float(num.equate)
    if isinstance(num, float):
        return Complex(num, 0)  
    
a = 1
print(a)
a = raise_(a)
print(a)
a = raise_(a)
print(a)
a = raise_(a)
print(a)