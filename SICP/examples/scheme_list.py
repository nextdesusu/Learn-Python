def cons(a, b):
    
    def dispatch(i):
        if i == 0:
            return a
        if i == 1:
            return b
        else:
            raise Exception("Out of range of cons")
        
    return dispatch

def car(f):
    return f(0)

def cdr(f):
    return f(1)

def print_list(list_):
    res = str(car(list_)) + ", "
    state = cdr(list_)
    while not state == "nil":
        res += str(car(state))+ ", "
        state = cdr(state)
    print("(" + res + ")")

def list_(*args):
    
    size = len(args) - 1
    
    def iter_(num):
        if num == size:
            return cons(args[num], "nil")
        return cons(args[num], iter_(num + 1))
    
    if size > 0:
        return iter_(0)

def get_by_index(list_, index):
    state = list_
    for i in range(index):
        state = cdr(state)
        if state == "nil":
            raise Exception("Index out of range")        
    return car(state)

def get_by_value(list_, val):
    state = list_
    counter = 0
    while not car(state) == val:
        state = cdr(state)
        if state == "nil":
            error_text = "this list don't contain: " + str(val)
            raise Exception(error_text)
        counter += 1
    return counter

def list_size(list_):
    counter = 0
    state = list_
    while not state == "nil":
        state = cdr(state)
        counter += 1
    return counter

def get_last(list_):
    return get_by_index(list_, list_size(list_) - 1)

def push(list_, elem):
    return cons(elem, list_)
    
def reverse(listobj):
    new_list = cons(car(listobj), 'nil')
    state = listobj
    while not cdr(state) == 'nil':
        state = cdr(state)
        new_list = push(new_list, car(state))
    return new_list

def square_list(list_):
    if not cdr(list_) == 'nil':
        return cons(car(list_) * car(list_), square_list1(cdr(list_)))
    return cons(car(list_) * car(list_), 'nil')
        
def glue_lists(list1, list2):

    def iter_(list1, list2, actual, condition):
        if condition and cdr(actual) == 'nil':
            return cons(car(actual), 'nil')
        if cdr(actual) == 'nil':
            return cons(car(actual), iter_(list1, list2, list2, True))
        return cons(car(actual), iter_(list1, list2, cdr(actual), condition))
        
    return iter_(list1, list2, list1, False)

def append(list_, elem):
    if cdr(list_) == 'nil':
        return cons(car(list_), cons(elem, 'nil'))
    return cons(car(list_), append(cdr(list_), elem))
    
a = cons(1, cons(2, cons(3, (cons(4, "nil")))))
b = list_(3, 4, 6, 6, 23, 55)
c = list_("lol", "kek", 3)
d = cons(19, b)

a = glue_lists(a, c)
#print_list(append(b, 5))
#print_list(glue_lists(a, a))



#print(print_list(d))
#print(print_list(reverse(a)))

#print(print_list(reverse(a)))
#print(get_by_index(a, 3))
#print(get_by_index(b, 4))
#print(get_by_value(b, 3))
#print(list_size(a))
#print("*" * 25)
#print(get_by_index(c, 2))
#print(get_by_index(c, 0))
#print(get_by_value(c, "kek"))
#assert get_by_value(b, 3) == 0
#assert get_by_value(c, "kek") == 1
