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