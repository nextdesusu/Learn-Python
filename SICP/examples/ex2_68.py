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

#SEQ = code_tree([['A', 3], ['B', 2], ['D', 1], ['C', 1]])
#print(SEQ)
#print(adjoin(['G', 1], [['A', 3], [['B', 2], [['D', 1], [['C', 1], []]]]]))
#print(adjoin(['G', 2], [['A', 3], [['B', 2], [['D', 1], [['C', 1], []]]]]))

def zero(num):
    return int(num) == 0 or int(num[0]) == 0

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

def decode(bits, tree):
    res = [] 
    state = tree
    for bit in bits:
        state = state[int(bit)]
        if leaf(state):
            res.append(state[1])
        if zero(bit):
            state = tree
    return res

def encode(message, tree):
    res = []
    for letter in message:
        finded = False
        state = tree
        while not finded:
            if letter == symbol(state[0]):
                res.append('0')
                finded = True
            else:
                res.append('1')
                state = state[1]
    return res
    
sample_tree = make_tree([['A', 3], ['B', 2], ['D', 1], ['C', 1]])
print(sample_tree)

#['0', '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0']
#['A', 'D', 'A', 'B', 'B', 'C']
print(encode(['A', 'D', 'A', 'B', 'B', 'C'], sample_tree))


