def square_of_2_max(a, b, c):
    if a > b < c:
        return a * a + c * c
    if b > a < c:
        return b * b + c * c
    else:
        return a * a + b * b 
        
    
print(square_of_2_max(3, 10, 6))