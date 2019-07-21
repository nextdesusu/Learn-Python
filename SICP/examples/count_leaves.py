def inner_lists_counter(list_):

    def count_leaves(list_, counter):
        if not len(list_):
            return counter
        if type(list_[0]) == type([]):
            return count_leaves(list_[1::], counter) + count_leaves(list_[0], counter) + 1
        return count_leaves(list_[1::], counter)
    
    return count_leaves(list_, 0)
    
    
a = [1, 2, 4, [], [1, [1, []]]]
b = [12, [123], [1, []]]
c = [123, [213]]
d = [[[[[]]]]]
e = [1, [2, [3, 4]]]

print(inner_lists_counter(e))
print(e)