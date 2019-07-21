import random
import math

mapsize = 5

def print_chart(*src):
    print(src)
    
def noise(freq):
    phase = random.uniform(0, 2*math.pi)
    return [math.sin(2*math.pi * freq*x/mapsize + phase)
            for x in range(mapsize)]
    
def weighted_sum(amplitudes, noises):
    output = [0.0] * mapsize  # make an array of length mapsize
    for k in range(len(noises)):
        for x in range(mapsize):
            output[x] += amplitudes[k] * noises[k][x]
    return output

amplitudes = [0.2, 0.5, 1.0, 0.7, 0.5, 0.4]
frequencies = [1, 2, 4, 8, 16, 32]

frequencies = range(1, 31)  # [1, 2, ..., 30]

def random_ift(rows, amplitude):
    for i in range(rows):
        random.seed(i)
        amplitudes = [amplitude(f) for f in frequencies]
        noises = [noise(f) for f in frequencies]
        sum_of_noises = weighted_sum(amplitudes, noises)
        print_chart(i, sum_of_noises)

random_ift(10, lambda f: 1)