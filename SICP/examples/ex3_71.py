def Ramajan_numbers():
    
    memory = dict()
    keys = []
    
    cube = lambda x: x * x * x
    
    sum_cubes = lambda pair: cube(pair[0]) + cube(pair[1])   
    
    def unique_pairs():
        j = 0
        while True:
            for i in range(0, j + 1):
                yield i, j
            j += 1    
            
    for pair in unique_pairs():
        cube_sum = sum_cubes(pair)
        if not cube_sum in memory:
            memory[cube_sum] = [cube_sum, pair]
        else:
            memory[cube_sum].append(pair)
            keys.append(cube_sum)
            for key in keys:
                print(memory[key], end = ' ')
            print()
            
Ramajan_numbers()
    
