from random import choice

def amb(*args):
    return choice(args)

def amb_with_cond(items, cond):
    item = amb(*items)
    while not cond(item):
        item = choice(items)
    item = items.pop(items.index(item))
    return item

def is_distinct(items):
    set_ = set(items)
    return len(set_) == len(items)

def multiple_dwelling():
    
    def amb_(items):
        item = amb(*items)
        item = items.pop(items.index(item))
        return item    
    
    places = [1, 2, 3, 4, 5]
    b = amb_(places)
    e = amb_(places)
    j = amb_(places)
    k = amb_(places)
    m = amb_(places)
    conds = [((k == 2 and b != 3) or (k != 2 and b == 3)), ((e == 1 and j != 2) or (e != 1 and j == 2)),
             ((j == 3 and e != 5) or (j != 3 and e == 5)), ((k == 2 and m != 4) or (k != 2 and m == 4)),
             ((m == 4 and b != 1) or (m != 4 and b == 1))]
    for cond in conds:
        if not cond:
            return
    return 'Betty', b, 'Etel', e, 'Joan', j, 'Kitty', k, 'Mary', m
    

def count():
    call = multiple_dwelling()
    while not call:
        call = multiple_dwelling()
    print(call)
    
count()