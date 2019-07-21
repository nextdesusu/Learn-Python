def scale_stream(stream, factor):
    call = next(stream)
    while call:
        yield call * factor
        call = next(stream)
        
def mul_stream(s1, s2):
    currents1, currents2 = next(s1), next(s2)
    yield currents1 * currents2
    for elem in add_streams(scale_stream(s2, currents1), mul_stream(s1, s2)):
        yield elem

def reciprocal_series(series):
    yield 1
    yield next(scale_stream(mul_stream(series, reciprocal_series(series)), -1))
    
def integers():
    n = 1
    while 1:
        yield n
        n += 1

for i in reciprocal_series(integers()):
    print(i)