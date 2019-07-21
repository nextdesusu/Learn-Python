def scale_tree(list_, factor):
    for index1 in range(len(list_)):
        if isinstance(list_[index1], list):
            scale_tree(list_[index1], factor)
        else:
            list_[index1] *= factor
    return list_

def scale_tree_map(list_, factor):
    
    def checker(elem):
        if isinstance(elem, list):
            return list(map(checker, elem))
        return elem * factor
        
    return list(map(checker, list_)) 

l = [1, [2, [3, 4], 5, [6, 7]]]
print(scale_tree(l, 10))
d = [1, [2, [3, 4], 5, [6, 7]]]
print(scale_tree_map(d, 10))


