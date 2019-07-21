from scheme_list import print_list, list_, cons, car, cdr

def square_list1(list_):
    if list_ == 'nil':
        return 'nil'
    return cons(car(list_) * car(list_), square_list1(cdr(list_)))

print(print_list(square_list1(list_(1, 2, 3, 4, 5))))

def square_list2(items):
    return map(lambda x: x * x, items)

for num in square_list2([1, 2, 3, 4, 5]):
    print(num, end = " ")

        