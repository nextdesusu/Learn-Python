equal = lambda x, y: x == y
null = lambda x: not x

def element_of_set_(x, set_):
    return x in set_

def element_of_set(x, set_):
    if null(set_):
        return False
    if equal(x, set_[0]):
        return True
    return element_of_set(x, set_[1::])

def adjoin_set(x, set_):
    set_.append(x)
    return set_

def union_set_(set1, set2):
    for new_elem in set2:
        set1.append(new_elem)
    return set1

def intersection_set_(set1, set2):
    res = []
    for elem in set1:
        if element_of_set_(elem, set2):
            res.append(elem)
    return res