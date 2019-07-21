def mult(num1, num2):
    
    even = lambda x: x % 2 == 0
    double = lambda x: x + x
    halve = lambda x: x / 2
    
    def iterator(num1, num2, memory):
        if num2 == 0:
            return 0
        if num2 == 1:
            return num1 + memory
        if even(num2):
            return iterator(double(num1), halve(num2), memory)
        return iterator(num1, num2 - 1, memory + num1)
        
    
    return iterator(num1, num2, 0)

for i in range(1, 10):
    for j in range(1, 10):
        print(mult(i, j) == i * j)
