from random import choice

def amb(*args):
    return choice(args)

def is_distinct(items):
    set_ = set(items)
    return len(set_) == len(items)

def multiple_dwelling():
    baker = amb(1, 2, 3, 4, 5)
    cooper = amb(1, 2, 3, 4, 5)
    fletcher = amb(1, 2, 3, 4, 5)
    miller = amb(1, 2, 3, 4, 5)
    smith = amb(1, 2, 3, 4, 5)
    conds = [not baker == 5, not cooper == 1, not fletcher == 5, not fletcher == 1, miller > cooper,
             not abs(smith - fletcher) == 1, not abs(fletcher - cooper) == 1, is_distinct([baker, cooper, fletcher, miller, smith]),]
    for cond in conds:
        if not cond:
            return
    return 'baker', baker, 'cooper', cooper, 'fletcher', fletcher, 'miller', miller, 'smith', smith

def count():
    call = multiple_dwelling()
    while not call:
        call = multiple_dwelling()
    print(call)
    
count()