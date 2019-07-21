def random_update(x):
    return ((13 * x) + 5) % 24

def random_numbers(init):
    state = init
    while True:
        yield state
        state = random_update(state)        

class RandomGenerator:
    
    def __init__(self, init):
        self.gen = random_numbers(init)
        
    def reset(self, new_init):
        self.gen = random_numbers(new_init)
        
    def __call__(self):
        return self.gen
    
gen = RandomGenerator(10)
gen.reset(15)
        
for num in gen():
    print(num)