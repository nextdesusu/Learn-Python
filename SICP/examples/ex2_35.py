def accumulate(op, initial, sequence):
    if not len(sequence):
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1::]))

def inner_lists_counter(list_):

    def count_leaves(list_, counter):
        if not len(list_):
            return counter
        if type(list_[0]) == type([]):
            return count_leaves(list_[1::], counter) + count_leaves(list_[0], counter) + 1
        return count_leaves(list_[1::], counter)
    
    return count_leaves(list_, 0)

def count_leaves(sequence):
    
    def checker(list_):
        if isinstance(list_, list):
            return count_leaves(list_)
        return 0
   
    return accumulate(lambda x, y: x + y, 1, list(map(checker, sequence)))
    


a = [1, 2, 4, [], [1, [1, []]]]
b = [12, [123], [1, []]]
c = [123, [213]]
d = [[[[[]]]]]
e = [1, [2, [3, 4]]]

def shorterer(list_):
    if isinstance(list_, list):
        return list_[1::]
    return list_

print(inner_lists_counter(e))
print(count_leaves(e))