def pair(elem, index):
    
    def dispatch(key):
        if key == index:
            return elem
    
    return dispatch

def my_list(elem):
    return pair(elem, 0)
    
def ran(start, end):
    while start <= end:
        yield start
        start += 1
        
b = ran(1, 10)
num = next(b)
while num != 10:
    num = next(b)
    print(num)
        