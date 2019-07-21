def leaf(obj):
    return obj[0] == 'leaf'

def make_leaf(symbol, weight):
    return ['leaf', symbol, weight]

def weight(obj):
    if leaf(obj):
        return obj[2]

def adjoin_set(x, set_):
    if not set_:
        return x
    if weight(x) < weight(set_[0]):
        return [x, set_]
    else:
        return [set_[0], adjoin_set(x, set_[1])]
    
def make_hoffman(pairs):
    for i in range(len(pairs)):
        if not leaf(pairs[i]):
            pairs[i] = make_leaf(pairs[i][0], pairs[i][1])
    return pairs

seq = [['A', 4], ['B', 2], ['C', 1], ['D', 1]]
b = adjoin_set(['leaf', 'C', 1], [['leaf', 'G', 6], ['leaf', 'D', 1], ['leaf', 'A', 3]])
print(b)
#print(make_hoffman(seq))