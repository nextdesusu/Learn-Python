def f_rec(n):
    if n < 3:
        return n
    return f_rec(n-1) + f_rec(n-2) + f_rec(n-3)

def f_iter(n):
    if n < 3:
        return n
    num1 = 2
    num2 = 1
    num3 = 0
    num = 0
    for i in range(1, n):
        num = num1 + num2 + num3
        num3 = num2
        num2 = num1
        num1 = num
    return num2

def show(num):
    for i in range(num):
        print("rec: ", f_rec(i))
        print("iter: ", f_iter(i))
        print("differrence: ", f_rec(i) - f_iter(i))
        if f_rec(i) - f_iter(i) != 0:
            print("NOT EQUAL")
            break

show(10)
    