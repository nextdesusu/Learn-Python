def Nil(f):
    return lambda x: x

def One(f):
    return lambda x: f(x)

def Two(f):
    return lambda x: f(f(x))

def PlusOne(x):
    return x + 1

b = Nil(0)(0)
print(b)
c = One(PlusOne)(0)
d = Two(PlusOne)(0)
print(d)