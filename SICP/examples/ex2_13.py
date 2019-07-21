import Interval as i

a = i.make_center_percent(10, 2)
b = i.make_center_percent(12, 4)
c = i.mul_interval(a, b)
a_p = i.percent(a)
b_p = i.percent(b)
c_p = i.percent(c)

def percent_of_two(i1, i2):
    return i.percent(i1) + i.percent(i2)


print(percent_of_two(a, b))
print(c_p)