def integers():
    n = 1
    while True:
        yield n
        n += 1

def merge_weighted(s1, s2, weight):
    next_s1, next_s2 = next(s1), next(s2)
    while next_s1 and next_s2:
        if weight(next_s1) < weight(next_s2):
            yield next_s1
            next_s1 = next(s1)
        elif weight(next_s1) < weight(next_s2):
            yield next_s2
            next_s2 = next(s2)
        elif weight(next_s1) and weight(next_s2):
            yield next_s1
            next_s1, next_s2 = next(s1), next(s2)            
        else:
            next_s1, next_s2 = next(s1), next(s2)
            
def random_pairs():
    while True:
        yield (randint(1, 10001), randint(1, 10001))
        
def weight_func(x):
    dels = (2, 3, 5)
    for del_ in dels:
        if x % del_== 0:
            return False
    return True
            
for elem in merge_weighted(integers(), integers(), weight_func):
    print(elem)
