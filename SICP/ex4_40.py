from random import choice

def amb(*args):
    return choice(args)

def amb_with_cond(items, cond):
    item = choice(items)
    while not cond(item):
        item = choice(items)
    item = items.pop(items.index(item))
    return item

def is_distinct(items):
    set_ = set(items)
    return len(set_) == len(items)

def multiple_dwelling():
    levels = [1, 2, 3, 4, 5]
    baker = amb_with_cond(levels, lambda x: not x == 5)
    cooper = amb_with_cond(levels, lambda x: not x == 1)
    fletcher = amb_with_cond(levels, lambda x: not x == 5 or x == 1)
    miller = amb_with_cond(levels, lambda x: x)
    smith = amb_with_cond(levels, lambda x: x)
    conds = [miller > cooper, not abs(smith - fletcher) == 1, not abs(fletcher - cooper) == 1, is_distinct([baker, cooper, fletcher, miller, smith])]
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