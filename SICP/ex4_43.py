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
    
    class Father:
        
        def __init__(self, name, daughter, yacht):
            self.name = name
            self.daughter = daughter
            self.yacht = yacht
        
        def __str__(self):
            return "{}: <d|{}, y|{}>".format(self.name, self.daughter, self.yacht)
        
        def __repr__(self):
            return str(self)
    
    def amb_(items):
        item = amb(*items)
        item = items.pop(items.index(item))
        return item
    
    def father_of(name, fathers):
        for father in fathers:
            if father.daughter == name:
                return father
        raise Exception("No such father")
    
    daughters = ["Habriella", "Lorna", "Rosalinda", "Melissa", "Mary"]
    yachts = daughters[:]
    m = Father("Moor", amb_(daughters), amb_(yachts))
    d = Father("Downing", amb_(daughters), amb_(yachts))
    h = Father("Holl", amb_(daughters), amb_(yachts))
    b = Father("Barnacle", amb_(daughters), amb_(yachts))
    p = Father("Parker", amb_(daughters), amb_(yachts))
    fathers = [m, d, h, b, p]
    conds = [m.daughter == "Mary", b.yacht == "Habriella", m.yacht == "Lorna",
             h.yacht == "Rosalinda", d.yacht == "Melissa", b.daughter == "Melissa", father_of("Habriella", fathers).yacht == p.daughter]
    for cond in conds:
        if cond is False:
            return
    return fathers

def count():
    call = multiple_dwelling()
    while not call:
        call = multiple_dwelling()
    print(call)
    
count()