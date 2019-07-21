null = lambda x: not x

def element_of_set(x, set_):
    if null(set_):
        return False
    if x == set_[0]:
        return True
    if x < set_[0]:
        return False
    return element_of_set(x, set_[1::])

def adjoin_set(x, set_):
    if x < set_[0]:
        set_.insert(0, x)
    return set_

print(adjoin_set(9, [10, 11, 12]))