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

def key(pair):
    return pair[0]

def lookup(given_key, set_of_records):
    if not set_of_records:
        return 'Not in base'
    if given_key == key(entry(set_of_records)):
        return entry(set_of_records)
    if given_key > key(entry(set_of_records)):
        return lookup(given_key, right_branch(set_of_records))
    if given_key < key(entry(set_of_records)):
        return lookup(given_key, left_branch(set_of_records))
    

tree = []
set_ = [5, [1, 2], [3, 4]]
print(lookup(3, set_))