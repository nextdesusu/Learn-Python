from copy import deepcopy

def get_sign(elem):
    if elem < 0:
        return '-'
    else:
        return '+'
    
def change_sign(num):
    return -num

def change_sign_of_all_terms(all_terms):
    res = []
    for elem in all_terms:
        res.append([change_sign(elem[0]), elem[1]])
    return res
    
def negate_poly(poly):
    return make_poly(poly.variable, change_sign_of_all_terms(poly.get_terms()))
     
def has_coeffs(term_list):
    if isinstance(term_list[0], int):
        return False
    return len(term_list[0]) == 2

def add(x, y):
    print('add', x, y)
    return x + y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def the_empty_term_list():
    return []

def is_empty_term_list(term_list):
    return not term_list

def first_term(term_list):
    return term_list[0]

def rest_terms(term_list):
    return term_list[1::]

def order(term):
    return term[0]

def coeff(term):
    return term[1]

def make_term(order, coeff):
    return [order, coeff]

class Polynomial:
    
    def __init__(self, variable, term_list):
        if not isinstance(variable, str):
            raise Exception("Wrong variable format CREATION")        
        self.variable = variable
        if not isinstance(term_list, list):
            raise Exception("Wrong term-list format CREATION type of terms is " + str(type(term_list)))
        if has_coeffs(term_list):
            self.term_list = term_list
        else:
            coeffs = range(len(term_list) - 1, -1, -1)
            self.term_list = list(map(lambda x, y: [x, y], term_list, coeffs))
        print('new poly', self.term_list)
        
    def is_empty(self):
        return not self.term_list
        
    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            raise Exception("Not polynomial")
        if not len(self.term_list) == len(other.term_list):
            return False
        if not self.variable == other.variable:
            return False
        for index in range(len(self.term_list)):
            if not self.term_list[index] == other.term_list[index]:
                return False
        return True
    
    def get_terms(self):
        return deepcopy(self.term_list)
        
    def __str__(self):
        str_ = ''
        for pair in self.term_list:
            term, coeff = pair[0], pair[1]
            if term == 0:
                pass
            elif coeff == 0:
                str_ += "{}{}".format(get_sign(term), abs(term))
            elif coeff == 1:
                str_ += "{}{}{}".format(get_sign(term), abs(term), self.variable)                
            else:
                str_ += "{}{}{}^{}".format(get_sign(term), abs(term), self.variable, coeff)
        return str_
    
    def __repr__(self):
        return str(self)
        
def make_poly(variable, term_list):
    return Polynomial(variable, term_list)

def variable(p):
    if isinstance(p, Polynomial):
        return p.variable
    else:
        raise Exception("Not polynomial VARIABLE")
    
def same_variable(p1, p2):
    return p1 == p2

def term_list(p):
    if isinstance(p, Polynomial):
        return p.get_terms()
    else:
        raise Exception("Not polynomial TERM-LIST")

def add_poly(p1, p2):
    if same_variable(variable(p1), variable(p2)):
        #print('start')
        return make_poly(variable(p1),
                         add_terms(term_list(p1),
                                   term_list(p2)))
    error_text = "Polynomials from different variables -- ADD-POLY, {}".format(list((p1, p2)))
    raise Exception(error_text)

def sub_poly(p1, p2):
    return add_poly(p1, negate_poly(p2))

def mul_poly(p1, p2):
    if same_variable(variable(p1), variable(p2)):
        return make_poly(variable(p1),
                         mul_terms(term_list(p1),
                                   term_list(p2)))
    error_text = "Polynomials from different variables -- MUL-POLY, {}".format(list((p1, p2)))
    raise Exception(error_text)

def adjoin_term(term, term_list):
    if not coeff(term):
        return term_list
    res = deepcopy(term_list)
    res.insert(0, term)
    return res

def add_terms(L1, L2):
    if is_empty_term_list(L1):
        return L2
    elif is_empty_term_list(L2):
        return L1
    else:
        #t1, t2 type is list not Polynomial
        t1, t2 = first_term(L1), first_term(L2)
        #print('t1', t1, 't2', t2)
        if order(t1) > order(t2):
            return adjoin_term(t1, add_terms(rest_terms(L1), L2))
        elif order(t1) < order(t2):
            return adjoin_term(t2, add_terms(rest_terms(L1), L2))
        else:
            return adjoin_term(make_term(order(t1),
                                         add(coeff(t1), coeff(t2))),
                               add_terms(rest_terms(L1), rest_terms(L2)))
        
def mul_term_by_all_terms(t1, L):
    if is_empty_term_list(L):
        return the_empty_term_list()
    t2 = first_term(L)
    return adjoin_term(make_term(order(t1) + order(t2),
                        mul(coeff(t1), coeff(t2))),
                        mul_term_by_all_terms(t1, rest_terms(L)))
        
def mul_terms(L1, L2):
    if is_empty_term_list(L1):
        return the_empty_term_list()
    return add_terms(mul_term_by_all_terms(first_term(L1), L2),
                     mul_terms(rest_terms(L1), L2))

def div_terms(L1, L2):
    if is_empty_term_list(L1):
        return [the_empty_term_list(), the_empty_term_list]
    t1, t2 = first_term(L1), first_term(L2)
    if order(t2) > order(t1):
        return [the_empty_term_list, L1]
    new_c = div(coeff(t1), coeff(t2))
    new_o = (order(t1) - order(t2))
    rest_of_result = div_terms(add_terms(rest_terms(L1),
                                         change_sign_of_all_terms(mul_term_by_all_terms(make_term(new_o, new_c)))),
                               rest_terms(L2))
    return [adjoin_term(make_term(new_c, new_o), rest_of_result[0])]

a = Polynomial('x', [3, 2, 2])
b = Polynomial('x', [5, 4, 1])
print(sub_poly(a, b))
#print(add_poly(a, b))