import math
import operator as op
import sys
from collections import ChainMap as Environment
from copy import copy, deepcopy

def standard_env():
    "An environment with some Scheme standard procedures."
    env = {}
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'begin':   lambda *x: x[-1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x, y: [x, y],
        'eq?':     op.is_, 
        'equal?':  op.eq, 
        'even?': lambda x: x % 2 == 0,
        'length':  len, 
        'list':    lambda *x: list(x), 
        'list?':   lambda x: isinstance(x,list), 
        'map':     lambda *args: list(map(*args)), #maybe this way lambda proc, *args: list(map(proc, args))
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),   
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
        'display': print,
    })
    return env

global_env = standard_env()

class Environment:
    
    def __init__(self, procs):
        self.env = dict()
        self.env.update(procs)
    
    def __getitem__(self, key):
        item = self.env[key]
        if isnstance(item, Delayed):
            return force(item)
        else:
            return item
        
Env = Environment(global_env)