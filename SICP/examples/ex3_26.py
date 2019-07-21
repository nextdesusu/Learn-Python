def make_tree(entry, left, right):
    return [entry, left, right]

def create_binary_tree(keys, values):
    items = ([key, value] for key, value in zip(keys, values))
    
    def sort_by_key(set_):
        return sorted(set_, key = lambda val: val[0])
    
    def make_trees(set_):
        first = set_[0]
        rest = set_[1::]
        middle = len(set_) // 2
        left = rest[0:middle]
        right = rest[middle::]
        #print(first, "|", left, "||", right, middle)
        return make_tree(first, left, right)
        
    res = sort_by_key(items)
    return make_trees(res)

class Table:
    
    def __init__(self, keys, values, equal_func = lambda x, y: x == y):
        self.body = create_binary_tree(keys, values)
        self.equal_func = equal_func
        print(self.body)
        
    def key_in(self, key):
        if key >= self.body[1][0][0] and key >= self.body[2][0][0]:
            rest = self.body[2]
        elif key >= self.body[1][0][0] and key < self.body[2][0][0]:
            rest = self.body[1]
        else:
            rest = self.body[0]
            print(self.body[1][0][0], self.body[2][0][0])
        return rest
            
    def add_sign(self, key, item):
        rest = self.key_in(key)
        for index in range(len(rest)):
            if self.equal_func(key, rest[index][0]):
                rest[index].append(item)
                return 
        rest.append([key, item])
        
    def __str__(self):
        return str(self.body)
    
    def lookup(self, key):
        rest = self.key_in(key)
        for pair in rest:
            if self.equal_func(key, pair[0]):
                return pair[1::]

a = Table((1, 3, 2, 5, 4, 7, 6, 8), ('a', 'c', 'b', 'e', 'd', 'g', 'g', 'h'))
a.add_sign(6, 'hehe')
print(a)