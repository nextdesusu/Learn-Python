import math
import operator as op
import sys
from copy import copy, deepcopy

Symbol = str              # A Scheme Symbol is implemented as a Python str
Number = (int, float)     # A Scheme Number is implemented as a Python int or float
Atom   = (Symbol, Number) # A Scheme Atom is a Symbol or Number
List   = list             # A Scheme List is implemented as a Python list
Exp    = (Atom, List)     # A Scheme expression is an Atom or List

def my_eq(x, y):
    return x.compute() == y

class Delayed:
    
    def __init__(self, val, env):
        self.val = val
        self.env = env
        
    def __str__(self):
        return 'dl:' + str(self.val)
    
    def __repr__(self):
        return str(self)
    
    def compute(self):
        return eval(self.val, self.env)
    
def make_delayed(list_, env):
    return list(map(lambda x: Delayed(x, env), list_))

class Procedure:
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
        
    def share_env(self):
        return self.env
    
    def __str__(self):
        return "{} | {} ".format(self.parms, self.body)
    
    def __repr__(self):
        return str(self)
    
    def __call__(self, *args):
        env = Env()
        env.set_standart()
        env.chain(dict(zip(self.parms, args)))
        call = eval(self.body, env)
        print('call', call)
        return call
    
class Env:
    
    def __init__(self, dict_ = {}):
        self.env = dict_
        
    def chain(self, other_dict):
        self.env.update(other_dict)
    
    def set_standart(self):
        self.env.update(vars(math)) # sin, cos, sqrt, pi, ...
        self.env.update({
            '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
            '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':my_eq, 
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
        
    def __setitem__(self, key, item):
        self.env[key] = item
        
    def __getitem__(self, key):
        #print('a', self.env.get('a', 'still not assigned'))
        call = self.env[key]
        if isinstance(call, Delayed):
            print('delayed argument called')
            return call.compute()
        else:
            return call
        
    def get_env(self):
        return 
        
global_env = Env()
global_env.set_standart()

def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> Exp:
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Exp:
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)
        
def eval(x, env=global_env):
    #print(x)
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):      # variable reference
        if x.startswith('"'):
            return x[1:-1]
        elif x.startswith("'"):
            return x[1::]
        else:
            call = env[x]
            if callable(call):
                print('procedure', call)
                return call
            else:
                print('not procedure')
                return call
    elif not isinstance(x, List):  # constant literal
        return x
    elif x[0] == 'if':             # (if test conseq alt)
        #print('if', x[1::])
        (_, test, conseq, alt) = x
        print('cond is', test, '|||', eval(test, env))
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)   
    elif x[0] == 'define':         # (define var exp)
        exp = x[1]
        var = exp[0]
        parms = exp[1::]
        if len(x) > 2:
            body = x[2]
            env[var] = Procedure(parms, body, env)
        else:
            env[var] = Delayed(var, parms[0], env)
    elif x[0] == 'lambda':         # (lambda (var...) body)
        return create_lambda(x[1::], env)
    else:                          # (proc arg...)
        proc = eval(x[0], env)
        args = make_delayed([exp for exp in x[1:]], env)
        return proc(*args)
    
def repl(prompt='lis.py> '):
    "A prompt-read-eval-print loop."
    while True:
        val = eval(parse(input(prompt)))
        if val is not None: 
            print(schemestr(val))

def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, List):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)
    
def split_commands(program):
    commands = program.read()
    commands_list = []
    current_pos = -1
    left_bracket = 0
    for char in commands.replace('\n', '').replace('\t', ''):
        if left_bracket == 0:
            commands_list.append('')
            current_pos += 1
        commands_list[current_pos] += char
        if char == '(':
            left_bracket += 1
        if char == ')':
            left_bracket -= 1
    return commands_list
    
def Main():
    program_root = "programm_normal_order.sch"
    with open(program_root) as program:
        for string in split_commands(program):
            eval(parse(string))

if __name__ == '__main__':
    #Check()
    Main()
    sys.exit()