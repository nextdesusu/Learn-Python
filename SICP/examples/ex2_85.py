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
        if real == int(real):
            self.real = int(real)
        else:
            self.real = real
        if imag == int(imag):
            self.imag = int(imag)
        else:
            self.imag = imag
            
    def take_first_elem(self):
        return self.real
             
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
        
    def __str__(self):
        return '{0} + {1}i'.format(self.real, self.imag)
    
class Rational:
    
    def __init__(self, n, m):
        if m == 0:
            raise 1 / 0        
        if n == int(n):
            self.n = int(n)
        else:
            self.n = n
        if m == int(m):
            self.m = int(m)
        else:
            self.m = m
            
    @property
    def equate(self):
        return self.n / self.m    
            
    def __int__(self):
        if self.m == 1:
            return self.n
        else:
            raise Exception('cant turn in to int')
        
    def __float__(self):
        return float(self.equate)
        
    def __eq__(self, other):
        return self.n == other.n and self.m == other.m   
    
    def take_first_elem(self):
        return self.n    
    
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
    
def project(num):  
    if isinstance(num, Rational):
        return int(num.take_first_elem())
    if isinstance(num, float):
        return Rational(num, 1)     
    if isinstance(num, Complex):
        return float(num.take_first_elem())

def drop(num):
    if raise_(project(num)) == num:
        return project(num)
    else:
        raise Exception("can't be dropped")
    
a = Complex(3, 0)
print('res', a, type(a))
a = drop(a)
print('res', a, type(a))
a = drop(a)
print('res', a, type(a))
a = drop(a)
print('res', a, type(a))