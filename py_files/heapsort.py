from heapq import heappush, heappop 
from random import randint

list_ = [randint(1, 100) for _ in range(randint(1, 50))]

def sort_(list_):
    heap = []
    res = []
    for elem in list_:
        heappush(heap, elem)
    while heap:
        res.append(heappop(heap))
    return res

print('Not sorted', list_)
print('Sorted', sort_(list_))
