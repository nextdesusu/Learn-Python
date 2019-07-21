def element_of_set_(x, set_):
    return x in set_

def union_set_(set1, set2):
    res = []
    for elem in set1:
        res.append(elem)
    for new_elem in set2:
        if not element_of_set_(new_elem, res):
            res.append(new_elem)
    return res
