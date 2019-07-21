from Interval import Interval

def percent(i):
    difference = (i.upper_bound - i.lower_bound) / 2
    m_val = i.lower_bound + difference
    return (difference / m_val) * 100

def make_center_percent(i, p):
    return Interval(i - (i / 100) * p, i + (i / 100) * p)

b = make_center_percent(12, 50)
print(b)
print(percent(b))
