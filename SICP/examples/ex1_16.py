def expt(b, n):
    a = 1
    
    def even(num):
        return num % 2 == 0    
    
    def square(num):
        return num * num 
    
    while n > 0:
        if even(n):
            a *= square(b)
            n -= 2
        else:
            a *= b
            n -= 1
        
    return a

def fast_expt(b, n):

    def even(num):
        return num % 2 == 0 
    
    def square(num):
        return num * num     
        
    def f_expt(a, b, n):
        if n == 0:
            return a
        if even(n):
            return f_expt(a, square(b), (n/2))
        return f_expt((a * b), b, (n-1))
        
        
    return f_expt(1, b, n)

print(fast_expt(3, 5))




