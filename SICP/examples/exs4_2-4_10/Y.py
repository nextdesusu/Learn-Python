'''
proc_1 = lambda n: lambda fact: fact(fact, n)
proc_2 = lambda ft, k: k if k == 1 else k * ft(ft, k - 1)
print(proc_1(5)(proc_2))
'''

for n in range(1, 10):
    print('fact n =', n, '=>', (lambda proc: lambda num: proc(proc, num))(lambda ft, k: k if k == 1 else k * ft(ft, k - 1))(n))
    print('fib n =',n , '=>', (lambda proc: lambda num: proc(proc, num))(lambda ft, k: k if k < 2 else ft(ft, k - 1) + ft(ft, k - 2))(n))