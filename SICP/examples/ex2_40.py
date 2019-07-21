class Cons:
    car = '()'
    cdr = 'nil'
    
    def __init__(self, x = '()', y = 'nil'):
        self.pre = x
        self.post = y
        
    @property
    def car(self):
        if self.pre == 'nil':
            return '()'
        return self.pre
    
    @property
    def cdr(self):
        return self.post    
    
    @property
    def cadr(self):
        try:
            return self.cdr.car
        except AttributeError:
            error_message = "cadr: attempt to get car of " + str(self.cdr) + " [cadr]"
            raise Exception(error_message)
        
    def __str__(self):
        if self.cdr == 'nil':
            return '({})'.format(self.car) 
        if self.car == 'nil':
            return '()'
        return '({}, {})'.format(self.car,  self.cdr)
    
def list_(*seq):
            
    def creator(index, *seq):
        if index == len(seq):
            return 'nil'
        return Cons(seq[index], creator(index + 1, *seq))
            
    return creator(0, *seq)

def enumerate_interval(start, end):
    if start >= end:
        return Cons(start, 'nil')
    return Cons(start, enumerate_interval(start + 1, end))

def append(seq, elem):
    if seq == 'nil':
        return Cons(elem, 'nil')    
    return Cons(seq.car, append(seq.cdr, elem))

def map_(proc, *seq):
    if len(seq) == 1:
        seq = seq[0]
    else:
        seq = clue_lists(*seq)
    def creator(proc, seq):
        if seq == 'nil':
            return seq
        return Cons(proc(seq.car), creator(proc, seq.cdr))
    
    return creator(proc, seq)

def accumulate(op, initial, sequence):
    if sequence == 'nil':
        return initial
    return op(sequence.car, accumulate(op, initial, sequence.cdr))

#(define (unique-pairs n)
#
#  (flatmap (lambda (i) (map (lambda (j) (list i j))
#
#                            (enumerate-interval 1 (- i 1))))
#
#           (enumerate-interval 1 n)))

def flatmap(proc, seq):
    return accumulate(append, 'nil', map_(proc, seq))

def unique_pairs_(n):
    return flatmap(lambda i: map_(lambda j: list_(i, j), enumerate_interval(1, i - 1)), enumerate_interval(1, n))

def flatmap(func, seq):
    res = []
    for elem1 in seq:
        if isinstance(elem1, list):
            for elem2 in flatmap(func, elem1):
                res.append(elem2)
        else:
            res.append(func(elem1))
    return res    

def map_(func, seq):
    return list(map(func, seq))

def unique_pairs(n):
    return flatmap(lambda i: map_(lambda j: [i, j], list(range(1, i))), list(range(1, n))) 

print(unique_pairs(5))