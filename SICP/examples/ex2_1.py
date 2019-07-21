from rational_nums import make_rat

one_third = make_rat(1, 3)
one_third_ = make_rat(1, 3)
one_half = make_rat(1, 2)

def mul_rat_new(x, y):
    return make_rat((x.numer * y.numer), (x.denom * y.denom))

print(mul_rat_new(one_third, one_third_))

