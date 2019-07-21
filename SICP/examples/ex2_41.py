def flatmap(func, seq):
    res = []
    for elem1 in seq:
        if isinstance(elem1, list):
            for elem2 in flatmap(func, elem1):
                res.append(elem2)
        else:
            res.append(func(elem1))
    return res

def accumulate(op, initial, sequence):
    if not len(sequence):
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1::]))

def unique_pairs(n):
    return flatmap(lambda i: map_(lambda j: list_(i, j), enumerate_interval(1, i - 1)), enumerate_interval(1, n))

def map_(func, seq):
    return list(map(func, seq))

def checker(seq, s):
    
    def all_int(seq):
        if isinstance(seq, int):
            return False
        for elem in seq:
            if not isinstance(elem, int):
                return False
        return True
    
    if all_int(seq):
        if accumulate(lambda x, y: x + y, 0, seq) == s:
            return seq
    
    return False


    
def triples(n, s):
    return flatmap(lambda i: map_(lambda j: map_(lambda k: checker([i, j, k], s), list(range(1, j))), list(range(1, i))), list(range(1, n + 1)))

print(triples(5, 8))
