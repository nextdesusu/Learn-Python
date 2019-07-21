def integers():
    n = 1
    while True:
        yield n
        n += 1
        
def scale_stream(stream, factor):
    call = next(stream)
    while call:
        yield call * factor
        call = next(stream)
        
for num in scale_stream(integers(), 5):
    print(num)