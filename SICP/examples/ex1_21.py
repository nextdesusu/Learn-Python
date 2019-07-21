def smallest_divisor(n):
    
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

prime = lambda x: smallest_divisor(x) == x

print(smallest_divisor(199))
print(smallest_divisor(1999))
print(smallest_divisor(19999))