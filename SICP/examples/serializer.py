def clear(cell):
    cell[0] = False

def test_and_set(cell):
    if cell[0]:
        return True
    cell[0] = True
    return False

def make_mutex():
    
    class Mutex:
        
        cell = [False]
        
        def acquire(self):
            if test_and_set(self.cell):
                return self.acquire()
            
        def release(self):
            clear(self.cell)
    
    return Mutex()

def make_serializer():
    
    class Serializer:
        
        def __init__(self, p, *args):
            mutex = make_mutex()
            self.serialized_p = list(args)
            mutex.acquire()
            for elem in args:
                p(args)
            mutex.release()
        
        '''
        def __call__(self, proc):
            self.serialized_p.append(proc)
            
        def parallel_execute(self):
            proc = self.serialized_p.pop(0)
            eval(proc) 
        '''
        
        def __call__(self, proc, *args):
            self.serialized_p.append([proc, args])
        
        def parallel_execute(self):
            proc, args = self.serialized_p.pop(0)
            proc(*args)
            
        def __str__(self):
            str_ = '#'
            for pair in self.serialized_p:
                str_ += 'proc: {}, args: {}; '.format(pair[0].__name__, pair[1])
            str_+= '#'
            return str_
    
    return Serializer()

def parallel_execute(s):
    s.parallel_execute()