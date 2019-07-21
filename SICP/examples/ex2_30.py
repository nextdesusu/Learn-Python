def square_tree(tree):
    
    for index in range(len(tree)):
        if isinstance(tree[index], list):
            square_tree(tree[index])
        else:
            tree[index] *= tree[index]
            
    return tree

def square_tree_map(list_):
    
    def checker(elem):
        if isinstance(elem, list):
            return list(map(checker, elem))
        return elem * elem
        
    return list(map(checker, list_))

l = [1, [2, [3, 4], 5, [6, 7]]]
print(square_tree(l))
d = [1, [2, [3, 4], 5, [6, 7]]]
print(square_tree_map(d))
