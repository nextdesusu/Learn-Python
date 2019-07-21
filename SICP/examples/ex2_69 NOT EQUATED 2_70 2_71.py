class S:
    
    def __init__(self, state):
        self.state = state
        
    def __repr__(self):
        return self.state

def weight(elem):
    return elem[2]

def symbol(elem):
    return elem[1]

def adjoin(elem, seq):
    
    res = []
    state = res
    
    def iter_(elem, rest, state):
        if not rest:
            state.append(elem)
            state.append([])
            return res
        if weight(elem) > weight(rest[0]):
            state.append(elem)
            state.append(rest)
            return res
        else:
            state.append(rest[0])
            state.append([])
            state = state[1]
            return iter_(elem, rest[1], state)
            
    return iter_(elem, seq, state)

def leaf(obj):
    return isinstance(obj[0], S)

def make_leaf(left, right):
    s = S('leaf')
    return [s, left, right]

def make_tree(pairs):
    for i in range(len(pairs)):
        pairs[i] = make_leaf(pairs[i][0], pairs[i][1])
    res = [pairs[0], []]
    
    for pair in pairs[1::]:
        res = adjoin(pair, res)
    return res

def succesive_merge(tree):
    
    for i in range(len(tree)):
        tree[i] = make_leaf(tree[i][0], tree[i][1])
    res = [pairs[0], []]
    
    for pair in pairs[1::]:
        res = adjoin(pair, res)
    return res

def make_code_tree(left, right):
    return list((left, right, append_(symbols(left), symbols(right)), weight(left) + weight(right)))

#ÄÅĞÅÂÎ ÄÎËÆÍÎ ÂÅÒÂÈÒÜÑß
#make_tree == succesive_merge