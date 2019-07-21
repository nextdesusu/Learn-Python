def mul_stream(s1, s2):
    currents1, currents2 = next(s1), next(s2)
    yield currents1 * currents2
    for elem in add_streams(scale_stream(s2, currents1), mul_stream(s1, s2)):
        yield elem

def scale_stream(stream, factor):
    call = next(stream)
    while call:
        yield call / factor
        call = next(stream)
        
def div_streams(s1, s2):
    c = next(s2)
    if c == 0:
        raise 1 /0
    yield scale_stream(mul_series(s1, reciprocal_series(scale_stream(s2, 1 / c))), 1 / c)
        
def integers():
    n = 1
    while 1:
        yield n
        n += 1

def twos():
    while 1:
        yield 2

for i in div_streams(integers(), twos()):
    print(i)
        