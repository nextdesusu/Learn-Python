def r(arg):
    yield 1
    yield 2
    yield 3
        
        
for i in map(lambda x : x * x, r(0)):
    print(i)
    
l = [1, 3, 5, 7, 9]
        
my_gen = (i for i in l if i < 7)

print(my_gen)

for num in my_gen:
    print(num)
    
def inf_gen(start):
    while 1:
        yield inf_gen(start + 1).__next__
    
for num in inf_gen(0):
    print(num)
    