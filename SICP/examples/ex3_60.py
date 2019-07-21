def integrate_series(series):
    del_ = 1
    elem = next(series)
    while elem:
        yield elem * 1 / del_
        del_ += 1
        elem = next(series)
        
def exp_series():
    yield 1
    series = integrate_series(exp_series())
    elem = next(series)
    while elem:
        yield elem
        elem = next(series)

def scale_stream(stream, factor):
    call = next(stream)
    while call:
        yield call * factor
        call = next(stream)
        
def sine_stream():
    yield 0
    series = integrate_series(cosine_stream())
    elem = next(series)
    while elem:
        yield elem
        elem = next(series)

def cosine_stream():
    yield 1
    series = integrate_series(scale_stream(cosine_stream(), -1))
    elem = next(series)
    while elem:
        yield elem
        elem = next(series)    

def add_streams(s1, s2):
    s1next, s2next = next(s1), next(s2)
    while s1next and s2next:
        yield s1next + s2next
        s1next, s2next = next(s1), next(s2)
        
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

def integers():
    n = 1
    while True:
        yield n
        n += 1
        
sin2x = next(mul_stream(sine_stream(), sine_stream()))
cos2x = next(mul_stream(cosine_stream(), cosine_stream()))
print(sin2x + cos2x)
#sin2x + cos2x = 1