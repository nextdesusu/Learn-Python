from scheme_list import *

my_list_p = [1, 4, 6, 2, 6, 10, 3]
my_list_s = list_(1, 4, 1, 5, 6, 10, 2)

def get_last_p(list_):
    return list_[len(list_) - 1]

def get_last_s(list_):
    return get_by_index(list_, list_size(list_) - 1)


print("python:", get_last_p(my_list_p))
print("scheme:", get_last_s(my_list_s))
