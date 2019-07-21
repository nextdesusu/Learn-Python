equal = lambda x, y: x == y
null = lambda x: not x

def element_of_set(x, set_):
    if null(set_):
        return False
    if equal(x, set_[0]):
        return True
    return element_of_set(x, set_[1::])

def element_of_set_(x, set_):
    return x in set_

def adjoin_set(x, set_):
    if element_of_set(x, set_):
        return set_
    else:
        set_.append(x)
    return set_

def adjoin_set_(x, set_):
    if element_of_set_(x, set_):
        return set_
    else:
        set_.append(x)
    return set_

def intersection_set(set1, set2):
    res = []
    if null(set1) or null(set2):
        return []
    if element_of_set(set1[0], set2):
        res.append(set1[0])
        res.append(intersection_set(set1[1::], set2))
        return res
    else:
        return intersection_set(set1[1::], set2)
    
def intersection_set_(set1, set2):
    res = []
    for elem in set1:
        if element_of_set_(elem, set2):
            res.append(elem)
    return res

print(intersection_set_([1, 2, 3], [1, 2, 6]))
