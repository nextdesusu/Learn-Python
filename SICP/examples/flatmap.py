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

def accumulate(op, initial, sequence):
    if sequence == 'nil':
        return initial
    return op(sequence.car, accumulate(op, initial, sequence.cdr))

#(define (flatmap proc seq)
#     (accumulate append nil (map proc seq)))

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

def flatmap(proc, seq):
    return accumulate(append, 'nil', map_(proc, seq))

def prime_sum(pair):
    if isinstance(pair.car, Cons) and isinstance(pair.cadr, Cons):
        return 'nil'
    prime = lambda x: x % 2 == 0
    return prime(pair.car + pair.cadr)

def make_pair_sum(pair):
    return list_(pair.car, pair.cdr)

def filter_(proc, seq):
    if seq == 'nil':
        return seq
    if proc(seq.car):
        return Cons(seq.car, filter_(proc, seq.cdr))
    return filter_(proc, seq.cdr)

#(define (make-pair-sum pair)
#    (list (car pair) (cadr pair) (+ (car pair) (cadr pair))))

def null_(pair):
    if pair == 'nil':
        return True
    if pair.car == '()':
        return True
    return False

#def prime_sum_pairs(n):
    #return map_(make_pair_sum, filter_(prime_sum, map_(lambda i: map_(lambda j:, list_(i, j)))))
    
def clue_lists(*seq):
    if len(seq) <= 1:
        return seq[0]
    length = len(seq)
    index = 0
    
    def creator(index, state, *seq):
        if state.cdr == 'nil':           
            index += 1
            if index == length:
                return state     
            return Cons(state.car, creator(index, seq[index], *seq))
        return Cons(state.car, creator(index, state.cdr, *seq))

    return creator(index, seq[index], *seq)    

def remove_old(elem, seq):
    if seq == 'nil':
        return 'nil'
    if seq.car == elem:
        return remove(elem, seq.cdr)
    return Cons(seq.car, remove(elem, seq.cdr))

def remove_(item, sequence):
    return filter_(lambda x: not x == item, sequence)

#(define (prime-sum-pairs n)
#    (map make-pair-sum
#        (filter prime-sum?
#            (flatmap
#                (lambda (i)
#                    (map (lambda (j) (list i j))
#                        (enumerate-interval 1 (- i 1))))
#                (enumerate-interval 1 n)))))

#(define (prime-sum-pairs n)
#    (map make-pair-sum (filter prime-sum? (flatmap (lambda (i) (map (lambda (j) (list i j)) (enumerate-interval 1 (- i 1)))) (enumerate-interval 1 n)))))

def permutations(s):
    if null_(s):
        return Cons()
    return flatmap(lambda x: map_(lambda p: Cons(x, p), permutations(remove_(x, s))), s)

def prime_sum_pairs_(n):
    return accumulate(append, 'nil', map_(lambda i: map_(lambda j: list_(i, j), enumerate_interval(1, i - 1)), enumerate_interval(1, n)))

def prime_sum_pairs(n):
    return map_(make_pair_sum, filter_(prime_sum, flatmap(lambda i: map_(lambda j: list_(i, j), enumerate_interval(1, i - 1)), enumerate_interval(1, n))))

#(accumulate append
#nil
#(map (lambda (i)
#(map (lambda (j) (list i j))
#(enumerate-interval 1 (- i 1))))
#(enumerate-interval 1 n)))

print('s', prime_sum_pairs_(6))
print('p', prime_sum_pairs(6))

a = list_(1, 2, 3)
b = list_('a', 'b')
c = list_(2, 3, 4, 6, 6, 7)
d = list_('a', 'b', 'c')
g = Cons()
#print(permutations(a))
#print(remove_(6, c))
#print(clue_lists(a, c))
#print(map_(lambda x: x + 2, a, c, a))
#print(filter_(lambda x: x % 2 == 0, c))
#print(g)
#print(d.cadr)
#print(enumerate_interval(1, 10))