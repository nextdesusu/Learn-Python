import math
import operator as op
import sys
from collections import ChainMap as Environment
from copy import copy, deepcopy
from random import choice

Symbol = str              # A Scheme Symbol is implemented as a Python str
Number = (int, float)     # A Scheme Number is implemented as a Python int or float
Atom   = (Symbol, Number) # A Scheme Atom is a Symbol or Number
List   = list             # A Scheme List is implemented as a Python list
Exp    = (Atom, List)     # A Scheme expression is an Atom or List

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
        env =  Environment(dict(zip(self.parms, args)), self.env)
        call = eval(self.body, env)
        print('>>>', call)
        return call
    
def plus(*args):
    res = 0
    for arg in args:
        arg = eval(arg)
        res += arg
    return res

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
        
def set_value(var, value, env):
    env[var] = value
    
def create_lambda(x, env):
    (parms, body) = x
    return Procedure(parms, body, env)    
        
def to_let(x, env):
    print('let>>>', x)
    parms = list(map(lambda pair: pair[0], x[0]))
    args  = list(map(lambda pair: eval(pair[1], env), x[0]))
    body = x[1]
    proc = [parms, body]
    lambda_ = create_lambda(proc, env)
    return lambda_(*args)

def to_let_star(x, env):
    vars_ = list(map(lambda pair: pair[0], x[0]))
    args = list(map(lambda pair: pair[1], x[0]))
    body = x[1]
    proc = ["let", vars_[1], args[1]]
    print(proc)
    
    to_let([[vars_[0], args[0]], ])
    ### DO NOT USE ###
    
def to_letrec(x, env):
    parms = list(map(lambda pair: pair[0], x[0]))
    args  = list(map(lambda pair: pair[1], x[0]))
    new_env = Environment(dict(zip(parms, args)), env)
    vals = []
    for parm, arg in zip(parms, args):
        val = eval(arg, new_env)
        new_env[parm] = val
        vals.append(val)
    body = x[1]
    lambda_ = Procedure(parms, body, env)
    return lambda_(*vals)

def to_unless(x, env):
    (_, condition, usual_value, exceptional_value) = x
    exp = (exceptional_value if eval(condition, env) else usual_value)
    return eval(exp, env)
        
def eval(x, env=global_env):
    #print(x)
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):      # variable reference
        if x.startswith('"'):
            print(x[1:-1])
            return x[1:-1]
        elif x.startswith("'"):
            return x[1::]        
        return env[x]
    elif not isinstance(x, List):  # constant literal
        return x 
    elif x[0] == 'amb':
        if x[1::]:
            val = choice(x[1::])
            return eval(val, env)
        return
    elif x[0] == 'quote':          # (quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'unless':
        return to_unless(x, env)
    elif x[0] == 'if':             # (if test conseq alt)
        print('if', x[1::])
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'set!':
        set_value(x[1], x[2], env)
    elif x[0] == 'while':
        condition = x[1]
        instructions = x[2::]
        #print('condition', condition, 'body', body)
        while True:
            if eval(condition, env):
                for instruction in instructions:
                    eval(instruction, env)
            else:
                break
    elif x[0] == 'cond':
        if x[-1][0][0] == 'else':
            conds = x[1:-1]
            for elem in conds:
                if eval(elem[0], env):
                    return eval(elem[1], env)
            else:
                return eval(x[-1][1], env)
        else:
            conds = x[1::]
            for elem in conds:
                if eval(elem[0], env):
                    return eval(elem[1], env)        
    elif x[0] == 'define':         # (define var exp)
        exp = x[1]
        var = exp[0]
        parms = exp[1::]
        if len(x) > 2:
            body = x[2]
            env[var] = Procedure(parms, body, env)
        else:
            env[var] = parms[0]
    elif x[0] == 'unbound':
        del env[x[1]]
    elif x[0] == 'let':
        return to_let(x[1::], env)
    elif x[0] == 'let*':
        return to_let_star(x[1::], env)
    elif x[0] == 'letrec':
        return to_letrec(x[1::], env)
    elif x[0] == 'lambda':         # (lambda (var...) body)
        return create_lambda(x[1::], env)
    else:                          # (proc arg...)
        #print('next proc is', x)
        #print('args before', x[1])
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]
        #print('args after', args)
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
    program_root = "programm.sch"
    with open(program_root) as program:
        for string in split_commands(program):
            eval(parse(string))
    '''
    while True:
        user_input = input('Type a command allowed coomands: quit, execute \n')
        if user_input == 'quit':
            return
        if user_input == 'execute':
            try:
                with open(input('Type name of program: ')) as program:
                    print('--- Start ---')
                    print()
                    for string in program:
                        print('>>>', end = '')
                        eval(parse(string))
                        print()
                    print('--- End --- ')
            except FileNotFoundError:
                print('Programm does not exist')
            '''
'''
def Check():
    program_root = "programm.sch"
    try:
        with open(program_root) as program:
            print(program.read())
    except FileNotFoundError:
        print('Programm does not exist')
'''
if __name__ == '__main__':
    #Check()
    Main()
    sys.exit()