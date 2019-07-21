def for_each_except(exception, procedure, list_):
    for elem in list_:
        if not elem == exception:
            procedure(elem)
            
################################################### Constraint ###################################################
def if_not_constraint(func):
    
    def wrapper(arg):
        if isinstance(arg, Constraint):
            return func(arg)
        raise Exception("wrong type in {}, type is: {}".format(func.__name__, type(arg)))
    
    return wrapper

class Constraint:
    
    value = False
    informant = False
    constraints = []
    
    def has_value(self):
        return not self.informant
    
    def get_value(self):
        return self.value
    
    def set_my_value(self, newval, setter):
        if not self.has_value():
            self.value = newval
            self.informant = setter
            for_each_except(setter,
                            inform_about_value,
                            self.constraints)
        elif not self.value == newval:
            raise Exception("Contradiction" + str(list((self.value, newval))))
        else:
            return "ignored"
    
    def forget_my_value(self, retractor):
        if retractor == self.informant:
            self.informant = False
            for_each_except(retractor,
                            inform_about_no_value,
                            constraints)
            return "ignored"
        
    def connect(self, new_constraint):
        if not memq(new_constraint, self.constraints):
            self.constraint.insert(0, new_constraint)
        if self.has_value():
            inform_about_value(new_constraint)
        return "done"

@if_not_constraint    
def has_value(constraint):
    return constraint.has_value()

@if_not_constraint 
def set_value(constraint, new_val, informant):
    return constraint.set_my_value(new_val, informant)

@if_not_constraint 
def get_value(constraint):
    return constraint.get_value()

@if_not_constraint 
def forget_value(constraint, refuser):
    return constraint.forget_my_value(refuser)

@if_not_constraint
def connect(constraint, new_constraint):
    return constraint.connetct(new_constraint)

################################################### Constraint ###################################################

################################################### Adder ###################################################
class Adder:
    
    def __init__(self, a1, a2, sum_):
        self.a1 = a1
        self.a2 = a2
        self.sum_ = sum_
        
    def connect_if_called(self, me):
        connect(self.a1, me)
        connect(self.a2, me)
        connect(self.sum_, me)
        
    def process_new_value(self, me):
        self.connect_if_called(me)
        if has_value(self.a1) and has_value(self.a2):
            set_value(self.sum_, (get_value(self.a1) + get_value(self.a2)), me)
        elif has_value(self.a1) and has_value(self.sum_):
            set_value(self.a2, (get_value(self.sum_) - get_value(self.a1)), me)
        elif has_value(self.a2) and has_value(self.sum_):
            set_value(self.a1, (get_value(self.sum_) - get_value(self.a2)), me)
        else:
            raise Exception("No values")
        return self.connect_if_called(me)
        
    def proccess_forget_value(self, me):
        forget_value(self.sum_, self.me)
        forget_value(self.a1, me)
        forget_value(self.a2, me)
        return self.process_new_value(me)
        #self.connect_if_called(me)
    
################################################### Adder ###################################################
    
################################################### Mulitpier ###################################################
#maybe i have to put self.connect_if_called(me) lower or maybe i have to return it when func is done
class Mulitpier:
    
    def __init__(self, m1, m2, product):
        self.m1 = m1
        self.m2 = m2
        self.product = product
        
    def connect_if_called(self, me):
        connect(self.m1, me)
        connect(self.m2, me)
        connect(self.product, me)
        
    def process_new_value(self, me):
        if has_value(self.m1) and get_value(self.m1) == 0 or has_value(self.m2) and get_value(self.m2) == 0:
            set_value(self.product, 0, me)
        elif has_value(self.m1) and has_value(self.m2):
            set_value(self.product, (get_value(self.m1) * get_value(self.m2)), me)
        elif has_value(self.product) and has_value(self.m1):
            set_value(self.m2, (get_value(self.product) / get_value(self.m1)), me)
        elif has_value(self.product) and has_value(self.m2):
            set_value(self.m1, (get_value(self.product) / get_value(self.m2)), me)        
        else:
            raise Exception("No values")
        return self.connect_if_called(me)
        
    def proccess_forget_value(self, me):
        forget_value(self.product, self.me)
        forget_value(self.m1, me)
        forget_value(self.m2, me)
        return self.process_new_value(me)
        #return self.connect_if_called(me)
    
################################################### Mulitpier ###################################################
        
################################################### Averager ###################################################
#maybe i have to put self.connect_if_called(me) lower or maybe i have to return it when func is done
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
    
################################################### Averager ###################################################

################################################### Squarer ###################################################
#maybe i have to put self.connect_if_called(me) lower or maybe i have to return it when func is done
class Squarer:
    
    def __init__(self, a, b, squarer):
        self.a = a
        self.b = b
        self.squarer = squarer
        
    def connect_if_called(self, me):
        connect(self.a, me)
        connect(self.b, me)
        
    def process_new_value(self, me):
        if has_value(self.b):
            if get_value(self.b) < 0:
                raise Exception("square lesser 0 square is" + str(self.b))
            set_value(self.a, sqrt(get_value(b)), me)
            if has_value(self.a):
                set_value(self.b, sqrt(get_value(a)), me)
        '''
        maybe this
        if has_value(self.b):
            if get_value(self.b) < 0:
                raise Exception("square lesser 0 square is" + str(self.b))
        set_value(self.a, sqrt(get_value(b)), me)
        if has_value(self.a):
            set_value(self.b, sqrt(get_value(a)), me)
        '''
        return self.connect_if_called(me)
        
    def proccess_forget_value(self, me):
        forget_value(self.a, me)
        forget_value(self.b, me)
        return self.process_new_value(me)
        #return self.connect_if_called(me)
    
################################################### Squarer ###################################################
    
################################################### Probe ###################################################
class Probe:
    
    def __init__(self, name, connector):
        self.name = name
        self.connector = connector
        
    def connect(self, me):
        self.connector.connect(me)
        return me
        
    def print_probe(self, value):
        print("Tester", self.name, "=", value)
    
    def proccess_new_value(self):
        self.print_probe(get_value(self.connector))
        
    def proccess_forget_value(self):
        self.print_probe("?")
        
    def I_have_a_value(self, me):
        self.connect(me)
        return self.proccess_new_value()
    
    def I_lost_my_value(self, me):
        self.connect(me)
        return self.proccess_forget_value()  
    

################################################### Probe ###################################################
    
def inform_about_value(constraint):
    constraint.I_have_a_value()
    
def inform_about_no_value(constraint):
    constraint.I_lost_my_value()

def celsius_fahrenheit_converter(c, f):
    #declaration
    u, v, w, x, y = make_connector(), make_connector(),
    make_connector(), make_connector(), make_connector()
    #***********
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(9, w)
    constant(5, x)
    constant(32, y)
    return "ok"

#Not sure
def make_connector():
    return Constraint()

def constant(value, connector):
    
    class me:
        def __init__(self, request = None):
            if request is not None:
                raise Exception("Unknown request in constant")
            
        def __str__(self):
            return "<me>"
    
    connect(connector, value, me)
    set_value(connector, value, me)
    return me

def cp(x, y):
    z = make_connector()
    Adder(x, y, z)
    return z

def cmin(x, y):
    z = make_connector()
    Adder(z, x, y)
    return z

def cmul(x, y):
    z = make_connector()
    Multiplier(x, y, z)
    return z

def cdiv(x, y):
    z = make_connector()
    Multiplier(z, x, y)
    return z

def cv(x):
    z = make_connector()
    constant(x, z)
    return z

def celsius_fahrenheit_converter(x):
    return cp(cmul(cdiv(cv(9)), (cv(5))), x), (cv(32))