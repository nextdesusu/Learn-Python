class Table:
    
    def __init__(self, keys, values, equal_func = lambda x, y: x == y):
        self.body = [[key, value] for key, value in zip(keys, values)]
        self.equal_func = equal_func
        
    def key_in(key):
        for pair in self.body:
            if self.equal_func(key, pair[0]):
                return True
        return False
        
    def add_sign(self, key, item):
        for index in range(len(self.body)):
            if self.equal_func(key, self.body[index][0]):
                self.body[index].append(item)
                return 
        self.body.append([key, item])
        
    def __str__(self):
        return str(self.body)
    
    def lookup(self, key):
        for pair in self.body:
            if self.equal_func(key, pair[0]):
                return pair[1::]
            
num_equal = lambda x, y: not abs(x - y) > 0.5

table = Table((1, 2, 3, 4.1), (1, 4, 9, 16.1), num_equal)
print(table)
print(table.lookup(4))