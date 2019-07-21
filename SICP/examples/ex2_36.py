def accumulate(op, initial, sequence):
    if not len(sequence):
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1::]))

class Cons:
    
    def __init__(self, x, y):
        self.car = x
        self.cdr = y
        
    def __str__(self):
        if self.cdr == 'nil':
            return '({})'.format(self.car)
        return '({}, {})'.format(self.car,  self.cdr)

#(define (accumulate-n op init seqs)
#    (if (null? (car seqs))
#    nil
#    (cons (accumulate op init (??))
#    (accumulate-n op init (??)))))

def accumulate_n(op, init, seqs):
    if not len(seqs[0]):
        return 'nil'
    return Cons(accumulate(op, init, list(map(lambda x: x[0], seqs))), accumulate_n(op, init, list(map(lambda x: x[1::], seqs))))
            

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print(accumulate_n(lambda x, y: x + y, 0, a))