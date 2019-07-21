from itertools import islice

def fib():
     prev, curr = 0, 1
     while True:
          yield curr
          prev, curr = curr, prev + curr
          
def counter(start = 0):
     state = start
     while 1:
          yield state
          state += 1

f = fib()
print(list(islice(f, 0, 10)))
print(list(islice(counter(), 0, 10)))