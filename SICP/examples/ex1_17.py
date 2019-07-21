def square(num):

    def iterator(num, state, counter):
        if counter == 0:
            return state
        state += num
        return iterator(num, state, counter - 1)        
    
    return iterator(num, 0, num)

def fast_expt(b, n):

    def even(num):
        return num % 2 == 0   
        
    def f_expt(a, b, n):
        if n == 0:
            return a
        if even(n):
            return f_expt(a, square(b), (n/2))
        return f_expt((a * b), b, (n-1))
        
        
    return f_expt(1, b, n)


def expt(b, n):
    
    def even(num):
        return num % 2 == 0         
    
    def double(num):
        return num + num
    
    def mult(num1, num2):
    
        def iterator(num1, num2, state):
            if num2 == 0:
                return state
            state += num1
            return iterator(num1, num2 - 1, state)
    
        return iterator(num1, num2, 0)
            
    def halve(n):
        
        def change(arg):
            if arg:
                return False
            return True     
    
        def iterator(act, num, end, dash): 
            if act == end:
                return num
            if dash:
                dash = change(dash)
                return iterator(act + 1, num + 1, end, dash)
            dash = change(dash)
            return iterator(act + 1, num, end, dash)
            
       
        return iterator(0, 0, n, False)
    
        
    def f_expt(a, b, n):
        if n == 0:
            return a
        if even(n):
            return f_expt(a, square(b), halve(n))
        return f_expt(mult(a, b), b, (n-1))
    
    return f_expt(1, b, n)

def fast_expt(b, n):
    
    def even(num):
        return num % 2 == 0 
        
    def double(num):
        return num + num
    
    def halve(num):
        return num / 2       
            
    def f_expt(a, b, n):
        if n == 0:
            return a
        if even(n):
            return f_expt(a, square(b), halve(n))
        return f_expt((a * b), b, (n-1))
            
    return f_expt(1, b, n)

def my_expt(b, n):
    
    double = lambda x: x + x
    
    def halve(n):

        def change(arg):
            if arg:
                return False
            return True     

        def iterator(act, num, end, dash): 
            if act == end:
                return num
            if dash:
                dash = change(dash)
                return iterator(act + 1, num + 1, end, dash)
            dash = change(dash)
            return iterator(act + 1, num, end, dash)


        return iterator(0, 0, n, False)
    
    def even(num):
        return num == double(halve(num))
    
    def f_expt(b, n):
        if n == 0:
            return 1
        if n == 1:
            return b
        if even(n):
            return double(f_expt(b, halve(n)))
        else:
            return b + f_expt(b, n - 1)
    
    return f_expt(b, n)    

print(fast_expt(5, 3))
print(expt(5, 3))
print(my_expt(5, 3))
    


    