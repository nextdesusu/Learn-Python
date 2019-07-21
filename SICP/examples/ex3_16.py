class Cons:
    
    def __init__(self, x, y):
        self.car = x
        self.cdr = y
        
    def __str__(self):
        return "({0}, {1})".format(self.car, self.cdr)
    
def list_(*args):
    
    def iter_(args):
        if not len(args):
            return "()"
        return Cons(args[0], iter_(args[1::]))
    
    return iter_(args)
    
def cdr(pair):
    return pair.car

def car(pair):
    return pair.cdr

def pair(x):
    return isinstance(x, Cons)

def count_pairs(x):
    if not pair(x):
        return 0
    return count_pairs(car(x)) + count_pairs(cdr(x)) + 1

str1 = list_("foo", "bar", "baz")
print(count_pairs(str1))
x = "foo"
y = Cons(x, x)
print(count_pairs(y))
str2 = list_(y)
print(count_pairs(str2))
str3 = Cons(y, y)
print(count_pairs(str3))