def filter(predicate, sequence):
    for num in sequence:
        if predicate(num):
            yield num
            
def accumulate(op, initial, sequence):
    if not len(sequence):
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1::]))

def enumerate_interval(low, high):
    while low <= high:
        yield low
        low += 1
        
def enumerate_tree(list_):
    for elem1 in list_:
        if isinstance(elem1, list):
            for elem2 in enumerate_tree(elem1):
                yield elem2
        else:
            yield elem1  
            
even = lambda x: x % 2 == 0
odd = lambda x: x % 2 != 0
plus = lambda x, y: x + y
mul = lambda x, y: x * y
square = lambda x: x * x

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [1, 2, 3, 4, 5]
d = [1, [2, [3, [4, [5]]]]]
c = [1, [2, [3, 4]], 5]

def sum_odd_squares(tree):
    return accumulate(plus, 0, list(map(square, filter(odd, list(enumerate_tree(tree))))))

def product_of_squares_of_odd_elements(squence):
    return accumulate(mul, 1, list(map(square, filter(odd, squence))))

print(sum_odd_squares(c))

print(product_of_squares_of_odd_elements(b))
