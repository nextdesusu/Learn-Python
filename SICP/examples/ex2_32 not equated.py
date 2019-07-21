from itertools import chain, combinations

def powerset(iterable):
    xs = list(iterable)
    # note we return an iterator rather than a list
    return list(chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1)))

d = [1, 2, 3]
print(powerset(d))
