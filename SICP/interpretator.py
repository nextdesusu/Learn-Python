def Eval(exp, env):
    if is_self_evaluating(exp):
        return exp
    elif is_variable(exp):
        return lookup_variable_value(exp, env)
    elif is_quoted(exp):
        return text_of_quotation(exp)
    elif is_asssignment(exp):
        return eval_assignment(exp, env)
    elif is_definition(exp):
        return eval_definition(exp, env)
    elif is_if(exp):
        return eval_if(exp, env)
    elif is_lambda(exp):
        '''
        maybe this way
        return make_procedure(lambda_paramters(exp),
                              lambda_body(exp),
                              env)
        '''
        return make_procedure(lambda_paramters(exp),
                              lambda_body(exp, env))
    elif is_begin(exp):
        return eval_sequence(begin_actions(exp), env)
    #what is it?
    #elif Eval(cond->if exp):
    #    return env
    elif is_application(exp):
        '''
        maybe this way
        return apply(Eval(operator(exp), env), list_of_values(operands(exp), env))
        '''
        return apply(Eval(operator(exp)), env, list_of_values(operands(exp), env))
    else:
        raise Exception("Unknown type of expression -- EVAL" + exp)

def apply(procedure, arguments):
    if is_primitive_procedure(procedure):
        return apply_primitive_procedure(procedure, arguments)
    elif is_compound_procedure(procedure):
        return eval_squence(procedure_body(procedure),
                            extend_envinronment(procedure_parameters(procedure),
                                                arguments,
                                                procedure_envinronment(procedure)))
    else:
        raise Exception("Unknown type of procedure -- APPLY " + procedure)
    
def list_of_values(exps, env):
    if is_no_operand(exps):
        return quoted('()')
    return cons(Eval(first_operand(exps), env), list_of_values(rest_operands(exps), env))

def eval_if(exp, env):
    if is_true(Eval(if_predicate(exp), env)):
        return Eval(if_consequent(exp), env)
    return Eval(if_alternative(exp), env)

def eval_sequence(exps, env):
    if is_last_exp(exps):
        return Eval(first_exp(exps), env)
    elif Eval(first_exp(exps), env):
        return eval_sequence(rest_exps(exps), env)
    
def eval_assignment(exp, env):
    set_variable_value(assignment_variable(exp),
                       Eval(assignment_value(exp), env),
                       env)
    return quoted('ok')

def eval_definition(exp, env):
    define_variable(definition_variable(exp),
                    Eval(definition_value(exp), env),
                    env)
    
    return quoted('ok')

#ex4_1

def list_of_values1(exps, env):
    if is_no_operand(exps):
        return quoted('()')
    left = Eval(first_operand(exps), env)
    right = Eval(rest_operands(exps), env)
    return cons(left, right)

def list_of_values2(exps, env):
    if is_no_operand(exps):
        return quoted('()')
    left = Eval(rest_operands(exps), env) 
    right = Eval(first_operand(exps), env)
    return cons(left, right)

def is_self_evaluating(exp):
    if is_number(exp):
        return True
    elif is_string(exp):
        return True
    else:
        return False
    
def is_variable(exp):
    return is_symbol(exp)

def is_quoted(exp):
    return is_tagged_list(exp, quoted('quote'))

def text_of_quotation(exp):
    return cadr(exp)

def is_tagged_list(exp, tag):
    if is_pair(exp):
        return is_eq(car(exp), tag)
    return False

def is_assignment(exp):
    return is_tagged_list(exp, quote('set!'))

def assignment_variable(exp):
    return cadr(exp)

def assignment_value(exp):
    return caddr(exp)

def is_definition(exp):
    return is_tagged_list(exp, quote('define'))

def is_definition_variable(exp):
    if is_symbol(cadr(exp)):
        return cadr(exp)
    return caddr(exp)

def is_definition_value(exp):
    if is_symbol(cadr(exp)):
        return caddr(exp)
    return make_lambda(cdadr(exp), cddr(exp))

def is_lambda(exp):
    return is_tagged_list(exp, quote('lambda'))

def lambda_parameters(exp):
    return cadr(exp)

def lambda_body(exp):
    return cddr(exp)

def make_lambda(parameters, body):
    return cons(quote('lambda'), cons(parameters, body))

def is_if(exp):
    return is_tagged_list(exp, quote('if'))

def if_predicate(exp):
    return cadr(exp)

def if_consequent(exp):
    return caddr(exp)

def if_alternative(exp):
    if not is_null(cdddr(exp)):
        return cadddr(exp)
    return quote('false')

def make_if(predicate, consequent, alternative):
    return list(quote('if'), predicate, consequent, alternative)

def is_begin(exp):
    return is_tagged_list(exp, quote('begin'))

def begin_actions(exp):
    return cdr(exp)

def is_last_exp(seq):
    return is_null(cdr(seq))

def first_exp(seq):
    return car(seq)

def rest_exps(seq):
    return cdr(seq)

def sequence_to_exp(seq):
    if is_null(seq):
        return seq
    elif is_last_exp(seq):
        return first_exp(seq)
    else:
        return make_begin(seq)
    
def make_begin(seq):
    return cons(quote('begin'), seq)

def is_application(exp):
    return is_par(exp)

def operator(exp):
    return car(exp)

def operands(exp):
    return cdr(exp)

def is_no_operands(ops):
    return is_null(ops)

def first_operand(ops):
    return car(ops)

def rest_operands(ops):
    return cdr(ops)

def is_cond(exp):
    return is_tagged_list(exp, quote('cond'))

def cond_clauses(exp):
    return cdr(exp)

def is_cond_else_clause(clause):
    return is_eq(cond_predicate(clause), quote('else'))

def cond_predicate(clause):
    return car(clause)

def cond_actions(clause):
    return cdr(clause)

def cond_to_if(exp):
    return expand_clauses(cond_clauses(exp))

def expand_clauses(clauses):
    if is_null(clauses):
        return quote('false')
    first = car(clauses)
    rest = cdr(clauses)
    if is_cond_else_clause(first):
        if is_null(rest):
            return sequence_to_exp(cond_actions(first))
        raise Exception('Else tree is not last COND->IF' + str(clauses))
    return make_if(cond_predicate(first),
                   sequence_to_exp(cond_actions(first)),
                   expand_clauses(rest))

def and_(exp):
    if is_null(cdr(exp)):
        return car(exp)
    if car(exp):
        return and_(cdr(exp))
    return quote('false')

def or_(exp):
    if is_null(exp):
        return quote('false')
    if car(exp):
        return car(exp)
    return or_(cdr(exp))

