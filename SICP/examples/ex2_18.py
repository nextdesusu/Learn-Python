def reverse_p(list_):
    return list_[::-1]

def push(list_, elem):
    return cons(elem, list_)
    
def reverse_s(listobj):
    new_list = cons(car(listobj), 'nil')
    state = listobj
    while not cdr(state) == 'nil':
        state = cdr(state)
        new_list = push(new_list, car(state))
    return new_list