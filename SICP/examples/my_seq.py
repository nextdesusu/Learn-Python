import numpy

numpy.array

class seq:
    
    def __init__(self, *args):
        self._args = tuple(args)
        
    def __setitem__(self, key, item):
        self._args = list(self._args)
        self._args[key] = item
        return seq(self._args)
    
    def __getitem__(self, key):
        return self._args[key]
    
    def __str__(self):
        str_ = ''
        for index, elem in enumerate(self._args):
            if not index == len(self._args) - 1:
                str_ += str(elem) + ', '
            else:
                str_ += str(elem)
        return "$" + str_ + "$"
    
class Cons:
    
    def __init__(self, car = '()', cdr = '()'):
        self.car = car
        self.cdr = cdr
    
    def __str__(self):
        return '({}, {})'.format(self.car, self.cdr)
    
class List:
    
    def __init__(self, *args):
        self.List_ = self._create_list(args)
        
    def _create_list(self, args):
        
        def iter_(seq):
            if not seq:
                return '()'
            return Cons(seq[0], iter_(seq[1::]))
            
        return iter_(args)
    
    def __str__(self):
        return str(self.List_)
            
    
b = List(1, 2, 4, 1, 2, 4)
print(b)
