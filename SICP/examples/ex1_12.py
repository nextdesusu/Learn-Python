def build(size):
    shift = size + size // 2 + 1
    rec_triangle(1, size, shift)

def rec_triangle(n, m, shift):
    for i in range(shift):
        print(end = " ")
    for i in range(1, n +  1):
        print(i, end = " ")
    for i in range(n - 1, 0, -1):
        print(i, end = " ")
    print("")
    if n < m:
        rec_triangle(n+1, m, shift  - 2)

#build(10)

def new_build(size):
    
    def printer(size, shift, minus):
        if not minus < 0:
            st = ''
            for s in range(shift):
                st += " " 
            for num1 in range(size - minus, 1, -1):
                st += str(num1)
            for num2 in range(1, size - minus + 1):
                st += str(num2)
            print(st)
            if type(shift / 10) == type(1):
                return printer(size, shift, minus - 1)
            return printer(size, shift - 1, minus - 1)
    
    return printer(size, size, size - 1)

new_build(6)
    

        