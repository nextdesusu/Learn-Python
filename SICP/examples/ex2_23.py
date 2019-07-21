from scheme_list import car, cdr, list_

def for_each(list_, f):
    state = list_
    while not state == 'nil':
        f(car(state))
        state = cdr(state)
    return True #Don't really need it
        
for_each(list_(1, 2, 3, 4, 5), print)