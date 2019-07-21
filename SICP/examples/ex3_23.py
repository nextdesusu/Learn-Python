def make_deque():
    return Deque()

def is_empty(deque):
    return deque.is_empty()

def front_ptr(deque):
    return deque.front_ptr

def rear_ptr(deque):
    return deque.rear_ptr

def frontinsertdeque(deque, item):
    deque.front_insert(item)
    
def rear_insert_deque(deque, item):
    deque.rear_insert(item)
    
def front_delete_deque(deque):
    if not is_empty(deque):
        deque.front_delete()
    
def rear_delete_deque(deque):
    if not is_empty(deque):
        deque.rear_delete()

class Deque:
    
    def __init__(self, *body):
        self.body = list(body)
        
    def is_empty(self):
        return not self.body
    
    def front_insert(self, val):
        self.body.insert(0, val)
        
    def rear_insert(self, val):
        self.body.append(val)
        
    def front_delete(self):
        self.body.pop(0)
        
    def rear_delete(self):
        self.body.pop()
        
    @property
    def front_ptr(self):
        try:
            return self.body[0]
        except:
            return []
    
    @property
    def rear_ptr(self):
        try:
            return self.body[len(self.body) - 1]
        except:
            return []
    
    def __str__(self):
        return "front: {}, body: {}, rear: {}".format(self.front_ptr, self.body, self.rear_ptr)
    
    
    
'''
q = Deque(1, 2, 3)
print(q)
front_delete_deque(q)
print(q)
rear_delete_deque(q)
print(q)
front_delete_deque(q)
print(q)
frontinsertdeque(q, 5)
print(q)
rear_insert_deque(q, 6)
print(q)
'''
a = make_deque()
print(a)
print(is_empty(a))
