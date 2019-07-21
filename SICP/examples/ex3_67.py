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

def all_pairs(s, t):
    next_s, next_t = next(s), next(t)
    yield next_s, next_t
    for elem in interleave(interleave(stream_map(lambda x: (next_s, x), t), all_pairs(s, t)), stream_map(lambda x: (next_t, x), s)):
        yield elem
        
for pair in all_pairs(integers(), integers()):
    print(pair)