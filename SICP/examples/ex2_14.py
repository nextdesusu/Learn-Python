from Interval import*

i1 = make_center_percent(10, 10)
i2 = make_center_percent(10, 50)
i3 = make_interval(3, 10)
i4 = mul_interval(i1, i3)
i5 = add_interval(i2, i4)

i5_div_i3p1 = par1(i5, i3)
print("par1:", i5_div_i3p1, percent(i5_div_i3p1), "%")
i5_div_i3p2 = par2(i5, i3)
print("par2:", i5_div_i3p2, percent(i5_div_i3p2), "%")

i2_div_i4p1 = par1(i2, i4)
print("par1:", i2_div_i4p1, percent(i2_div_i4p1), "%")
i2_div_i4p2 = par2(i2, i4)
print("par2:", i2_div_i4p2, percent(i2_div_i4p2), "%")
