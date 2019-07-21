def fringed(list_):
    res = []
    for elem1 in list_:
        if isinstance(elem1, list):
            for elem2 in fringed(elem1):
                res.append(elem2)
        else:
            res.append(elem1)
    return res

l = [1, 2, 3, [1, 2, 3], 4, [1, 2, 3], [1, 2, [1, 2, 3]], 5]
d = [1, [2, [3, [4, [5]]]]]

print(fringed(l))
print(fringed(d))
        
        