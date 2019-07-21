null = lambda x: x is None

def entry(tree):
    try:
        return tree[0]
    except:
        return None
    
def left_branch(tree):
    try:
        return tree[1][0]
    except:
        return None

def right_branch(tree):
    try:
        return tree[1][1][0]
    except:
        return None
    
def make_tree(entry, left, right):
    return list((entry, left, right))

def element_of_set(x, set_):
    if null(set_):
        return False
    if x == entry(set_):
        return True
    if x < entry(set_):
        return element_of_set(x, left_branch(set_))
    if x > entry(set_):
        return element_of_set(x, right_branch(set_))

def adjoin_set(x, set_):
    if null(set_):
        return make_tree(x, [], [])
    if x == entry(set_):
        return set_
    if x < entry(set_):
        return make_tree(entry(set_), adjoin_set(x, left_branch(set_)), right_branch(set_))
    if x > entry(set_):
        return make_tree(entry(set_), left_branch(set_), adjoin_set(x, right_branch(set_)))  
    
set_ = [5, [1, 2], [3, 4]]
    

    