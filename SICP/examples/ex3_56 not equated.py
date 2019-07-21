def integers():
    n = 1
    while 1:
        yield n
        n += 1

def scale_stream(stream, factor):
    call = next(stream)
    while call:
        yield call * factor
        call = next(stream)
        
def merge(s1, s2):
    s1next, s2next = next(s1), next(s2)
    while s1next and s2next:
        if s1next < s2next:
            yield s1next
            yield merge(next(s1), s2)
        elif s1next > s2next:
            yield s2next
            yield merge(s1, next(s2))
        else:
            yield merge(next(s1), next(s2))

def S():
    yield 1
    while 1:
        yield next(merge(merge(scale_stream(call, 2), scale_stream(call, 3)), scale_stream(call, 5)))

for i in S():
    print(i)
    