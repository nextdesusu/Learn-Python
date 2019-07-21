def same_parity(*args):
    res = []
    for num in args:
        if num % 2 == 0:
            res.append(num)
    return res

print(same_parity(2, 5, 2, 5, 3, 23, 5, 32, 33, 6))