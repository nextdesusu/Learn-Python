def f(n):
    keeper[0] *= n
    return keeper[0]

keeper = [1]
print(f(0) + f(1))
#Reset keeper
keeper = [1]
print(f(1) + f(0))