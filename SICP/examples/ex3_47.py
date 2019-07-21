def clear(cell, proccess_id):
    cell[proccess_id] = False

def test_and_set(cell, proccess_id):
    if cell[proccess_id]:
        return True
    cell[proccess_id] = True
    return False

def make_semaphore():
    
    class Semaphore:
        
        def __init__(self, *procs):
            processes = list(procs)
            cell = [False for b in range(len(procs))]
        
        def acquire(self, procces_id):
            if test_and_set(self.cell, procces_id):
                return self.acquire(procces_id)
            
        def release(self, process_id):
            clear(self.cell, procces_id)
    
    return Semaphore()