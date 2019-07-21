def power(num, pow_):
    result = 1
    while pow_ > 0:
        if pow_ % 2 == 1:
            result *= num
            pow_ -= 1
        num *= num
        pow_ /= 2
    return result

print(power(2, 8))