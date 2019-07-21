def integers():
    n = 1
    while 1:
        yield n
        n += 1

def partial_sums(stream):
    
    def get_part_sums(stream, n):
        sum_src = stream()
        sum_ = next(sum_src)
        for i in range(n):
            sum_ += next(sum_src)
        return sum_
    
    n = 0
    while 1:
        yield get_part_sums(stream, n)
        n += 1
        
sums = partial_sums(integers)
for elem in sums:
    print(elem)

