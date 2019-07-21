def Square_numbers():
    
    memory = dict()
    keys = []
    
    square = lambda x: x * x
    
    sum_square = lambda pair: square(pair[0]) + square(pair[1])   
    
    def unique_pairs():
        j = 0
        while True:
            for i in range(0, j + 1):
                yield i, j
            j += 1    
            
    for pair in unique_pairs():
        square_sum = sum_square(pair)
        if not square_sum in memory:
            memory[square_sum] = [square_sum, pair]
        else:
            memory[square_sum].append(pair)
            keys.append(square_sum)
            for key in keys:
                print(memory[key], end = ' ')
            print()
            
Square_numbers()
    
