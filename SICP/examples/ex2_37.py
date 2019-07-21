def accumulate_n(op, init, seqs):
    if not len(seqs[0]):
        return 'nil'
    return Cons(accumulate(op, init, list(map(lambda x: x[0], seqs))), accumulate_n(op, init, list(map(lambda x: x[1::], seqs))))

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
    
def to_list(cons):
    res = []
    while not cons == 'nil':
        if isinstance(cons.car, Cons):
            res.append(to_list(cons.car))
        else:
            res.append(cons.car)
        cons = cons.cdr
    return res
    
#(define (dot-product v w)
#    (accumulate + 0 (map * v w)))

m1 = [[1, 2, 3, 4],
      [4, 5, 6, 6],
      [6, 7, 8, 9]]

m2 = [[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]]

m3 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

v1 = [1, 2, 3]
v2 = [2, 2, 2]
v3 = [1, 1, 1]
v4 = [[1, 2, 3, 4]]

mul = lambda x, y: x * y
plus = lambda x, y: x + y


def dot_product(v, w):
    return accumulate(plus, 0, list(map(mul, v, w)))

def matrix_vector(m, v):
    return list(map(lambda x: dot_product(x, v), m))

def transpose(mat): #I need to use cons because accumulate_n use it too but it can be transformed to list by to_list(Cons)
    return accumulate_n(Cons, 'nil', mat)

def matrix_mul_matrix(m, n):
    cols = to_list(transpose(n))
    return list(map(lambda x: matrix_vector(cols, x), m))


#(define (matrix-*-matrix m n)
#    (let ((cols (transpose n)))
#        (map (??) m)))


#print(dot_product(v1, v3))
#print(matrix_vector(m3, v1))
#print(transpose(m3))
#print(to_list(transpose(m3)))
mat1 = [[1, 2],
        [3, 4]]
mat2 = [[4, 3],
        [2, 1]]
mat3 = [[1, 1],
        [2, 2]]
mat4 = [[3, 3],
        [4, 4]]

print(matrix_mul_matrix(mat3, mat4))