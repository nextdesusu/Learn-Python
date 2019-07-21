class ID:
    
    prev_id = -1
    
    def __call__(self):
        self.prev_id += 1
        return self.prev_id

get_new_id = ID()

class Global_process:
    procs = []
    
    def search_proc(self, id_):
        for index, proc in enumerate(self.procs):
            if proc[0] == id_:
                return index
    
    def execute(self, proc_id):
        index = self.search_proc(proc_id)
        id_, proc, args = self.procs.pop(index)
        proc(*args)
        return id_
    
    def execute_all(self):
        for id_, proc, args in self.procs:
            proc(*args)
            print("executed:", id_, 'proc:', proc.__name__, 'args:', args)
            
    def add(self, proc, args):
        self.procs.append([get_new_id(), proc, args])
        
    def __str__(self):
        return str(self.procs)
    
global_procs = Global_process()

def make_serialized(proc):
    
    def wrapper(*args):
        global_procs.add(proc, args)
        
    return wrapper

def make_account(name, amount):
    
    class Account:
        
        def __init__(self, name, amount):
            self.owner = name
            self.balance = amount
            
            
        @make_serialized   
        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Your balance is", self.balance, "and you trying to draw", amount)
        
        @make_serialized        
        def draw(self, amount):
            self.balance += amount
                
        def __str__(self):
            return "%name: {}, balance: {}%".format(self.owner, self.balance)
        
        def __repr__(self):
            return str(self)
                
    return Account(name, amount)

anton = make_account('anton', 100)
print(anton)
anton.withdraw(10)
print(global_procs)
anton.withdraw(12)
print(global_procs)
anton.withdraw(50)
print(global_procs)
anton.draw(50)
print(global_procs)
anton.draw(50)
print(global_procs)
print(anton)
global_procs.execute_all()
print(anton)