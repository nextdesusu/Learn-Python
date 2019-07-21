def Averager_(a, b, c):
    forget_value(c)
    average = (get_value(a) + get_value(b)) / 2
    set_value(c, average)

def Averager(a, b, c):
    u = make_connector()
    v = make_connector()
    #I have to call this 2 procs somehow
    Adder(a, b, u)
    Mulitpier(c, v, u)
    #-----------------------------------
    constant(2, v)
    return  "ok"