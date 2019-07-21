operators_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

def parse_exp(exp):
    return operators_dict[exp[1]](exp[0], exp[2])

calc = [10, '/', 5]
print(parse_exp(calc))