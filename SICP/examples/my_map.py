def map_(f, items):
    for num in items:
        yield f(num)
        
l = [1, 2, 3, 4, 5]
f = lambda x: x * x

for val in map_(f, l):
    print(val)