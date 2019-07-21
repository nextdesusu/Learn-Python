equal = lambda x, y: x == y
null = lambda x: not x

def element_of_set(x, set_):
    if null(set_):
        return False
    if x == set_[0]:
        return True
    if x < set_[0]:
        return False
    return element_of_set(x, set_[1::])

def intersection_set(set1, set2):
    res = []
    while not null(set1) and not null(set2):
        x1 = set1[0]
        x2 = set2[0]
        if x1 == x2:
            res.append(x1)
            set1 = set1[1::]
            set2 = set2[1::]
        if x1 < x2:
            set1 = set1[1::]
        if x2 < x1:
            set2 = set2[1::]
    return res

def adjoin_set(x, set_):
    if element_of_set(x, set_):
        return set_
    if x < set_[0]:
        set_.insert(0, x)
    return set_

def union_sets(set1, set2):
    res = []
    ended = False
    while not ended:
        if null(set1):
            res.extend(set2)
            break
        if null(set2):
            res.extend(set1)
            break
        x1 = set1[0]
        x2 = set2[0]
        if x1 == x2:
            res.append(x1)
            set1 = set1[1::]
            set2 = set2[1::]
        if x1 < x2:
            res.append(x1)
            set1 = set1[1::]
        if x2 < x1:
            res.append(x2)
            set2 = set2[1::]
    return res

print(union_sets([8, 9, 10, 13, 19, 20], [8, 10, 11, 12, 14]))
    