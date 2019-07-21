def variable(e):
    return isinstance(e, S)

def same_variable(v1, v2):
    if variable(v1) and variable(v2):
        return v1 == v2
    return False

def sum_(e):
    if isinstance(e, Exp):
        return e.operator == '+'
    return False

def addend(e):
    return e.start

def augend(e):
    return e.end

def make_sum(a1, a2):
    return Exp([a1, '+', a2])

def product(e):
    if isinstance(e, Exp):
        return e.operator == '*'
    return False

def multiplier(e):
    return e.start

def multiplicand(e):
    return e.end

def make_product(m1, m2):
    return Exp([a1, '*', a2])

def number(e):
    return isinstance(e, S)

def deriv(exp, var_):
    if number(exp):
        return 0
    elif variable(exp):
        if same_variable(exp, var_):
            return 1
        return 0
    elif sum_(exp):
        return make_sum(deriv(addend(exp), var_), deriv(augend(exp), var_))
    elif product(exp):
        return make_sum(make_product(multiplier(exp), deriv(multiplicand(exp), var_)), make_product(deriv(multiplier(exp), var_), multiplicand(exp)))
    else:
        error_text = "undefined expression -- DERIV " + str(exp)
        raise Exception(error_text)
    
    class S:
        
        def __init__(self, name, value):
            self.name = name
            self.value = value
            
        def quote(self):
            return self.name
            
        def __str__(self):
            return self.value
        
        def __add__(self, other):
            return self.value + other
        
        def __sub__(self, other):
            return self.value - other
        
        def __mul__(self, other):
            return self.value * other
        
        def __truediv__(self, other):
            return self.value / other
        
        def __eq__(self, other):
            return self.value == other.value
    
    class Exp:
        
        def __init__(self, seq):
            self.exp = seq
            self.start = self.exp[0]
            self.operator = self.exp[1]
            self.end = self.exp[2]
            
        def execute(self):
            res = ''
            for elem in self.exp:
                if isinstance(elem, S):
                    res += str(elem.value)
                else:
                    res += str(elem)
            return eval(res)
                
        def __str__(self):
            s = ''
            for elem in self.exp:
                if isinstance(elem, S):
                    s += str(elem.quote())
                else:
                    s += str(elem)
                s += ' '
            return s


print(deriv(Exp(['x','+', 3]), 'x'))