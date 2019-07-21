def deep_reverse(list_):
    reverse = lambda list_: list_[::-1]
    list_ = reverse(list_)
    for index in range(len(list_)):
        if type(list_[index]) == type([]):
            list_[index] = deep_reverse(list_[index])
    return list_
    
    
a = [1, 2, 3, [1, 2, 3], [1, 2, 3], 4]
b = [1, 2, 3]
c = [1, 2, [1, 2, [1, 2]]]
d = [[], [], []]
e = [1, 2, 3, [], []]
print("Before:", a)
a = deep_reverse(a)
print("After:", a)
print("Before:", b)
b = deep_reverse(b)
print("After:", b)
print("Before:", c)
c = deep_reverse(c)
print("After:", c)
print("Before:", d)
d = deep_reverse(d)
print("After:", d)
print("Before:", e)
e = deep_reverse(e)
print("After:", e)