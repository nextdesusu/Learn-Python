def func_tree(tree):
    
    def iter_(tree, func):
        for index in range(len(tree)):
            if isinstance(tree[index], list):
                iter_(tree[index], func)
            else:
                tree[index] = func(tree[index])
        return tree
            
    return lambda func: iter_(tree, func)

def func_tree_map(list_):

    def mapper(func):
        def checker(elem):
            if isinstance(elem, list):
                return list(map(checker, elem))
            return func(elem)
        return checker
            
    return lambda func: list(map(mapper(func), list_))


def func_tree_map_(func):
        
    def checker(elem):
        if isinstance(elem, list):
            return list(map(checker, elem))
        return func(elem)
                    
    return lambda list_: list(map(checker, list_))

l = [1, [2, [3, 4], 5, [6, 7]]]
print(func_tree(l)(lambda x: x - 1))
d = [1, [2, [3, 4], 5, [6, 7]]]
print(func_tree_map(d)(lambda x: x / 2))
n = [1, [2, [3, 4], 5, [6, 7]]]
print(func_tree_map_(lambda x: x - 1)(n))
