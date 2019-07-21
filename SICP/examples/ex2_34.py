def accumulate(op, initial, sequence):
    if not len(sequence):
        return initial
    return op(sequence[0], accumulate(op, initial, sequence[1::]))
    
def horner_eval(x, coefficient_sequence):
    return accumulate(lambda this_coeff, higher_terms: (higher_terms * x) + this_coeff, 0, coefficient_sequence)

print(horner_eval(2, [1, 3, 5, 0, 1]))