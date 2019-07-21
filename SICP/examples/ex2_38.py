#(define (fold-left op initial sequence)
#    (define (iter result rest)
#         (if (null? rest)
#              result
#              (iter (op result (car rest))(cdr rest))))
#                   (cdr rest))))
#    (iter initial sequence))

class Cons:
    
    def __init__(self, x, y):
        self.car = x
        self.cdr = y
        
    def __str__(self):
        if self.cdr == 'nil':
            return '({})'.format(self.car)
        return '({}, {})'.format(self.car,  self.cdr)
    
def fold_left(op, initial, sequence):
    
    def iter_(result, rest):
        if rest == 'nil':
            return result
        return iter_(op(result, rest.car), rest.cdr)
    
    return iter_(initial, sequence)

def fold_right(op, initial, sequence):
    if sequence == 'nil':
        return initial
    return op(sequence.car, fold_right(op, initial, sequence.cdr))

a = Cons(1, Cons(2, Cons(3, 'nil')))
div = lambda x, y: x / y

print(fold_left(div, 1, a))
print(fold_right(div, 1, a))

def list_(*seq):
    
    def creator(index, *seq):
        if index == len(seq):
            return 'nil'
        return Cons(seq[index], creator(index + 1, *seq))
    
    return creator(0, *seq)
        
print(fold_right(list_, 'nil', list_(1, 2, 3)))
print(fold_left(list_, 'nil', list_(1, 2, 3)))