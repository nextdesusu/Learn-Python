import time
inverter_delay = 0.3
and_gate_delay = 0.5
or_gate_delay = 0.5

def add_action(obj, action):
    pass

def set_signal(s, new_s):
    return new_s

def get_signal(s):
    return s

def after_delay(t, action):
    start = time.time()
    while time.time() - start < t:
        pass
    action()

def logical_not(s):
    if s == 0:
        return 1
    elif s == 1:
        return 0
    else:
        raise Exception("Signal is not correct")
    
def logical_and(s1, s2):
    if s1 == 1 and s2 == 1:
        return 1
    else:
        return 0
    
def logical_or(s1, s2):
    if s1 == 1 or s2 == 1:
        return 1
    return 0

def inverter(input_, output_):
    
    def invert_input():
        new_value = logical_not(get_signal(input_))
        after_delay(inverter_delay, set_signal(output, new_value))
    
    add_action(input_, invert_input())
    return 'ok'

def and_gate(a1, a2, output_):
    
    def and_action_procedure():
        new_value = logical_and(get_signal(a1), get_signal(a2))
        after_delay(and_gate_delay, set_signal(output_, new_value))
    
    add_action(a1, and_action_procedure())
    add_action(a2, and_action_procedure())
    return 'ok'

def or_gate(o1, o2, output_):
    
    def or_action_procedure():
        new_value = logical_or(get_signal((o1), get_signal(o2)))
        after_delay(or_gate_delay, set_signal(ouput_, new_value))
        
    add_action(o1, or_action_procedure)
    add_action(o2, or_action_procedure)
    return 'ok'

def or_gate_(o1, o2, output_):
    c1, c2, c3 = make_wire(), make_wire(), make_wire()
    inverter(a1, c1)
    inverter(a2, c2)
    and_gate(c1, c2, c3)
    inverter(c3, output_)
    return 'ok'
        
def make_wire():
    return

a = make_wire()
b = make_wire()
c = make_wire()
d = make_wire()
e = make_wire()
s = make_wire()
'''
or_gate = a, b, d
and_gate = a, b, c
inverter(c, e)
'''
def half_ader(a, b, s, c):
    d, e = make_wire(), make_wire()
    or_gate = a, b, d
    and_gate = a, b, c
    inverter = c, e
    and_gate = d, e, s
    return 'ok'

def full_adder(a, b, c_in, sum_, s_out):
    s = make_wire()
    c1 = make_wire()
    c2 = make_wire()
    half_adder(b, c_in, s, c1)
    half_adder(a, s, sum_, c2)
    or_gate = c1, c2, c_out
    return 'ok'