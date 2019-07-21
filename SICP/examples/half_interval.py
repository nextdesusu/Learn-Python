from math import sin

def half_interval_method(f, a, b):
    
    negative = lambda x: x < 0
    positive = lambda x: x > 0    
    
    def search(f, neg_point, pos_point):
    
        average = lambda x, y: (x / 2) + (y / 2)
        close_enough = lambda x, y: abs(x - y) < 0.001
    
        midpoint = average(neg_point, pos_point)
    
        if close_enough(neg_point, pos_point):
            return midpoint
    
        test_value = f(midpoint)
    
        if positive(test_value):
            return search(f, neg_point, midpoint)
        if negative(test_value):
            return search(f, midpoint, pos_point)
        else:
            return midpoint    
    
    a_value = f(a)
    b_value = f(b)
    if negative(a_value) and positive(b_value):
        return search(f, a, b)
    if negative(b_value) and positive(a_value):
        return search(f, b, a)
    else:
        raise Exception("Not different signs between a and b")
    
    
    
print(half_interval_method(sin, 2, 4))
print(half_interval_method(lambda x: (x * x * x) - 2 * x - 3, 1, 2))
