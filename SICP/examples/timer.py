import time

work_times = {}

def timer(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        work_times[func.__name__ + "(" + str(args[0]) +  ")"] = end - start
        
    
    return wrapper

def show():
    for key in work_times.keys():
        print(key, " => ", work_times[key], "ms")