import time

class Counter:
    num = 0
    
    def inc(self):
        self.num += 1
        
    def __str__(self):
        return str(self.num) + "."
    
counter = Counter()

def tested_func(func):
    
    def wrapper(*args):
        print(counter, "called", func.__name__, "with args", args)
        if None in args:
            raise Exception("None in args of " + func.__name__)
        called = func(*args)
        print("result of", func.__name__, "=", called)
        counter.inc()
        if called is None:
            return func.__name__ + " done"
        else:
            return called
        
    return wrapper

def tested_func(func):
    
    def wrapper(*args):
        return func(*args)
    
    return wrapper

def not_none(func):
    
    def wrapper(*args):
        call = func(*args)
        #if call is None:
        #    raise Exception("None args: " + str(args))
        return call
    
    return wrapper

@tested_func
def null(x):
    if not isinstance(x, list):
        raise Exception("not list its " + str(type(x)) + " " + str(x))
    return not len(x)

class Agenda:
    
    def __init__(self):
        self.segments = []
        
    @property
    def current_time(self):
        if self.is_empty():
            return 0
        return self.segments[0][0]
    
    def check_for_times(self, time_):
        for index, elem in enumerate(self.segments):
            if time_ == elem[0]:
                return index
            
    def add_action(self, time_, action):
        index = self.check_for_times(time_) 
        if index is None:
            self.segments.insert(0, [time_, action])
        else:
            self.segments[index].append(action)
            
    def is_empty(self):
        return not len(self.segments)
    
    def __str__(self):
        return "<t{}, {}>".format(self.current_time, self.segments)
    
    def first_item(self):
        if not self.is_empty():
            return self.segments[0]
        
    def pop_first_item(self):
        if not self.is_empty():
            self.segments.pop(0)
    
    def __repr__(self):
        return "$" + str(self) + "$"    

@tested_func  
def make_agenda():
    return Agenda()

@tested_func
def is_empty(agenda):
    return agenda.is_empty()

@tested_func
def first_agenda_item(agenda):
    return agenda.first_item()

@tested_func
def pop_first_agenda_item(agenda):
    agenda.pop_first_item()

@tested_func
def question_mark(t, action):
    start = time.time()
    while time.time() - start < t:
        pass
    action()

@tested_func   
def current_time(agenda):
    return agenda.current_time

@tested_func   
def add_to_agenda(time_, action, agenda):
    agenda.add_action(time_, action)
    
@tested_func    
def after_delay(delay, action):
    add_to_agenda(delay + current_time(the_agenda), action, the_agenda)
    
@tested_func
def call_each(procedures):
    for procedure in procedures:
        procedure()
    return "done"

class Wire:
    
    def __init__(self):
        self.signal_value = 0
        self.action_procedures = []
        
    def set_my_signal(self, val):
        if not self.signal_value == val:
            self.signal_value = val
            call_each(self.action_procedures)
        return (self, val)
    
    def accept_action_procedure(self, proc):
        self.action_procedures.insert(0, proc)
        proc()
        
    def __str__(self):
        return "Wire val: {}, actions: {}".format(self.signal_value, self.action_procedures)
    
    def __repr__(self):
        return "$" + str(self) + "$"    
        
class Probe:
    
    def __init__(self, name, wire):
        self.name = name
        self.wire = wire
        
    @property    
    def signal_value(self):
        return self.wire.signal_value
        
    def set_my_signal(self, val):
        print("*******" + str(self.name) + "*******")
        print("old value:", self.wire.signal_value)
        print("time:", current_time(the_agenda))
        call = self.wire.set_my_signal(val)
        print("new value:", val)
        print("*" * (14 + len(self.name)))
        return call
        
    @not_none
    def accept_action_procedure(self, proc):
        self.wire.accept_action_procedure(proc)
        
    def __str__(self):
        return "<Probed " + str(self.wire) + ">"
    
    def __repr__(self):
        return "$" + str(self) + "$"

@tested_func        
def make_wire():
    return Wire()

@tested_func
def add_action(obj, action):
    obj.accept_action_procedure(action)

#this bastard
@tested_func
def set_signal(s, new_s):
    return s.set_my_signal(new_s)
    
@tested_func
def get_signal(s):
    return s.signal_value

@tested_func
def logical_not(s):
    if s == 0:
        return 1
    elif s == 1:
        return 0
    else:
        raise Exception("Signal is not correct")

@tested_func
def logical_and(s1, s2):
    if s1 == 1 and s2 == 1:
        return 1
    else:
        return 0
    
@tested_func
def logical_or(s1, s2):
    if s1 == 1 or s2 == 1:
        return 1
    return 0

@tested_func
def inverter(input_, output_):
    
    def invert_input():
        new_value = logical_not(get_signal(input_))
        return after_delay(inverter_delay, set_signal(output_, new_value))
    
    add_action(input_, invert_input)
    return "done"

@tested_func
def and_gate(a1, a2, output_):
    
    def and_action_procedure():
        new_value = logical_and(get_signal(a1), get_signal(a2))
        return after_delay(and_gate_delay, set_signal(output_, new_value))
    
    add_action(a1, and_action_procedure)
    add_action(a2, and_action_procedure)
    return "done"

@tested_func
def or_gate(o1, o2, output_):
    
    def or_action_procedure():
        new_value = logical_or(get_signal(o1), get_signal(o2))
        return after_delay(or_gate_delay, set_signal(output_, new_value))
        
    add_action(o1, or_action_procedure)
    add_action(o2, or_action_procedure)
    return 'ok'

'''
@tested_func
def or_gate_(o1, o2, output_):
    c1, c2, c3 = make_wire(), make_wire(), make_wire()
    inverter(a1, c1)
    inverter(a2, c2)
    and_gate(c1, c2, c3)
    inverter(c3, output_)
    return 'ok'
'''

@tested_func 
def make_wire():
    return Wire()

@tested_func
def half_ader(a, b, s, c):
    d, e = make_wire(), make_wire()
    or_gate(a, b, d)
    and_gate(a, b, c)
    inverter(c, e)
    and_gate(d, e, s)
    print("ok")
    return 'ok'

@tested_func
def full_adder(a, b, c_in, sum_, s_out):
    s = make_wire()
    c1 = make_wire()
    c2 = make_wire()
    half_adder(b, c_in, s, c1)
    half_adder(a, s, sum_, c2)
    or_gate = c1, c2, c_out
    return 'ok'

@tested_func
def ripple_carry_adder(Ak, Bk, Sk, C):
    
    def iter_(A, B, S, c_in, c_out):
        if null(A):
            return S
        full_adder(car(A), car(B), c_in, car(S), c_out)
        return iter_(cdr(A), cdr(B), cdr(S), c_out, make_wire())
    
    return iter_(Ak, Bk, Sk, C, make_wire())
    
def propogate():
    while not is_empty(the_agenda):
        print(the_agenda)
        call = first_agenda_item(the_agenda)[1::]
        if isinstance(call, list):
            for proc in call:
                #set_signal(proc[0], proc[1])
                pass
        pop_first_agenda_item(the_agenda)
        
inverter_delay = 2
and_gate_delay = 3
or_gate_delay = 5
the_agenda = make_agenda()

print(the_agenda)
input_1 = make_wire()
input_2 = make_wire()
sum_ = make_wire()
carry = make_wire()
sum_ = Probe("sum", sum_)
carry = Probe("carry", carry)
half_ader(input_1, input_2, sum_, carry)

print(the_agenda)
set_signal(input_1, 1)
propogate()

