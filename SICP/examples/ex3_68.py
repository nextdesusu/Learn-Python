def integers():
    n = 1
    while True:
        yield n
        n += 1
        
def stream_map(proc, stream):
    elem = next(stream)
    while elem:
        yield proc(elem)
        elem = next(stream)  

def interleave(s1, s2):
    yield next(s1)
    for elem in interleave(s2, s1):
        yield elem

def hugo_pairs(s, t):
    next(t)
    for elem in interleave(stream_map(lambda x: (next(s), x), t), hugo_pairs(s, t)):
        yield elem
        
for pair in hugo_pairs(integers(), integers()):
    print(pair)