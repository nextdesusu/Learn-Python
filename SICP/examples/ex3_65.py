def partial_sums(stream):
    accum = 0
    elem = next(stream)
    while elem:
        accum += elem
        yield accum
        elem = next(stream)

def stream_map(proc, stream):
    elem = next(stream)
    while elem:
        yield proc(elem)
        elem = next(stream)  

def l2_summands(n):
    yield 1 / n
    for elem in stream_map(lambda x: -x, l2_summands(n + 1)):
        yield elem

def l2():
    return partial_sums(l2_summands(1))   
        
for elem in l2():
    print(elem)