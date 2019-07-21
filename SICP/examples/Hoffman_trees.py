class S:
    
    def __init__(self):
        self.state = 'leaf'
        
    def __repr__(self):
        return self.state

s = S()

def make_leaf(symbol, weight):
    return [s, symbol, weight]

def leaf(obj):
    return isinstance(obj[0], S)
    
def symbol_leaf(x):
    return x[1]

def weight_leaf(x):
    return x[2]
    
def left_branch(tree):
    return tree[0]

def right_branch(tree):
    return tree[1]
    
def symbols(tree):
    if leaf(tree):
        return list(symbol_leaf(tree))
    else:
        return tree[1][1][0]

def weight(tree):
    if leaf(tree):
        return weight_leaf(tree)
    else:
        return tree[3]
    
def append_(e1, e2):
    res = e1
    if isinstance(e2, list) and e2:
        res.append(e2[0])
    else:
        res.append(e2)
    return res

def make_code_tree(left, right):
    print(weight(left), weight(right))
    return list((left, right, append_(symbols(left), symbols(right)), weight(left) + weight(right)))

def choose_branch(bit, branch):
    if bit == 0:
        return left_branch(branch)
    if bit == 1:
        return right_branch(branch)
    else:
        raise ValueError('bad bit -- CHOOSE-BRANCH" bit')

def cons(e1, e2):
    res = e1[:]
    res.insert(0, e2[:])
    return res

def decode(bits, tree):
    
    def decode_1(bits, current_branch):
        if not bits:
            return []
        next_branch = choose_branch(bits[0], current_branch)
        if leaf(next_branch):
            return [symbol_leaf(next_branch), decode_1(bits[1::], tree)]
        
    return decode_1(bits, tree)

def adjoin_set(x, set_):
    if not set_:
        return [x]
    if weight(x) < weight(set_[0]):
        return cons(x, set_)
    else:
        return cons(set_[0], adjoin_set(x, set_[1::]))

def make_leaf_set(pairs):
    
    for i in range(len(pairs)):
        pairs[i] = make_leaf(pairs[i][0], pairs[i][1])
    
    def iter_(pairs):
        if not pairs:
            return []
        pair = pairs[0]
        el = iter_(pairs[1::])
    
        return adjoin_set(pair, pairs)
    
    return iter_(pairs[::-1])
        
#exmp = [[['leaf', 'A', 4], [['leaf', 'C', 1], []]], [[[], ['leaf', 'D', 1]], ['leaf', 'B', 2]]]
#print([[[['leaf', 'A', 4], 'leaf', 'D', 1], 'leaf', 'C', 1], 'leaf', 'B', 2][0])
#((A 4) (B 2) (C 1) (D 1))
#result = make_leaf_set([['A', 4], ['B', 2], ['C', 1], ['D', 1]])
#print(decode([0, 1], result))
#print('r', result)

def sample_tree():
    return make_code_tree(make_leaf("A", 4), make_code_tree(make_leaf("B", 2), make_code_tree(make_leaf("D", 1), (make_leaf("C", 1)))))

t = sample_tree()
print(t)