import time
from functools import reduce
import array

def func(num):
    
    def inc(num):
        return num + 1

    def dec(num):
        return num - 1
    
    return inc(num) + dec(num)

def show(text):
    print(text, end = " ")
    
    def nums(num):
        print(num)
    
    return nums

def ret(func, num):
    func(num)

def kek(arg):
    print(arg)

def timer(func):
    def decorate(*args, **kwargs):
        print("start")
        start = time.time()
        print("result", func(*args, *kwargs))
        end = time.time()
        print("end")
        print("{}: {}, {}".format("Time after launch of " + func.__name__, end - start, "seconds"))
    return decorate

@timer
def incrementator(num):
    res = 0
    for i in range(num):
        res += i
    return res

incrementator(1000000)

l = [1, 2, 3, 4, 5]


for num in filter(lambda x: x % 2 == 0, l):
    print(num)