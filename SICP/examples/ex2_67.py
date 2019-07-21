class S:
    
    def __init__(self, state):
        self.state = state
        
    def __repr__(self):
        return self.state

def weight(elem):
    return elem[2]

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

def zero(num):
    if num == 1 or num == '1':
        return False
    return int(num) == 0 or int(num[0]) == 0

def make_leaf(left, right):
    s = S('leaf')
    return [s, left, right]

def decode(bits, tree):
    state = tree
    res = [] 
    for bit in bits:
        state = state[int(bit)]
        if leaf(state):
            res.append(state[1])
        if zero(bit):
            state = tree
    return res

def make_tree(pairs):
    for i in range(len(pairs)):
        pairs[i] = make_leaf(pairs[i][0], pairs[i][1])
    res = [pairs[0], []]
    
    for pair in pairs[1::]:
        res = adjoin(pair, res)
    return res
    
sample_tree = make_tree([['A', 3], ['B', 2], ['D', 1], ['C', 1]])
seq = [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
print(seq)
print(decode(seq, sample_tree))
