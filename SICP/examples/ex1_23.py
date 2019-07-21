import time

work_times = {}

def timer(func):
    
    def wrapper(arg):
        start = time.time()
        func(arg)
        end = time.time()
        work_times[func.__name__ + "(" + str(arg) + ")"] = end - start
        
    
    return wrapper

@timer
def smallest_divisor_old(n):
            
    square = lambda x: x * x
    divides = lambda a, b: b % a == 0
           
    def find_divisor(n, test_divisor):
        if square(test_divisor) > n:
            return n
        if divides(test_divisor, n):
            return test_divisor
        else:
            return find_divisor(n, test_divisor + 1)
            
    return find_divisor(n, 2)

@timer
def smallest_divisor(n):
    
    square = lambda x: x * x
    divides = lambda a, b: b % a == 0
    
    def next_(test_divisor):
        if test_divisor > 2:
            return test_divisor + 2
        return test_divisor + 1
    
    def find_divisor(n, test_divisor):
        if square(test_divisor) > n:
            return n
        if divides(test_divisor, n):
            return test_divisor
        else:
            return find_divisor(n, next_(test_divisor))
    
    return find_divisor(n, 2)

test_list = [1009, 1013, 1019, 10007, 10009, 10037, 100003, 100019, 100043, 1000003, 1000033, 1000037]

#sad but at 100019 python reach the maximum of recursion depth in smallest_divisor_old

for num in test_list:
    smallest_divisor_old(num)
for num in test_list:
    smallest_divisor(num)
for key in work_times.keys():
    print(str(key) + " => " + str(work_times[key]))