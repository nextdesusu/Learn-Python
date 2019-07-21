def integers():
    n = 1
    while True:
        yield n
        n += 1

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
        
for i in cosine_stream():
    print(i)