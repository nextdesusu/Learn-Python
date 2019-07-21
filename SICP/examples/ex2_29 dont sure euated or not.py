def make_mobil(left, right):
    return list((left, right))

def make_branch(length, structure):
    return list((length, structure))

def left_branch(mobil):
    return mobil[0]

def right_branch(mobil):
    return mobil[1]

def branch_length(branch):
    return branch[0]

def branch_structure(branch):
    return branch[1]

def total_weight(mobil):
    
    def counter(branch):
        if isinstance(branch_structure(branch), list):
            return total_weight(branch_structure(branch)) + branch_length(branch)
        else:
            return branch_length(branch)
        
    return counter(left_branch(mobil)) + counter(right_branch(mobil))

def balanced(mobil):
    
    def multiplier(branch):
        if isinstance(branch_structure(branch), list):
            return multiplier(branch_structure(branch))
        else:
            return branch_structure(branch) 
    
    left_ml = multiplier(left_branch(mobil))
    right_ml = multiplier(right_branch(mobil))    
        
    def total_weight(mobil, first_time):
        
        def counter(branch):
            if isinstance(branch_structure(branch), list):
                return total_weight(branch_structure(branch), False) + branch_length(branch)
            else:
                return branch_length(branch)
            
        if first_time:
            return (left_ml * counter(left_branch(mobil))) == (right_ml * counter(right_branch(mobil))) 
            
        return counter(left_branch(mobil)) + counter(right_branch(mobil))    

            
    return total_weight(mobil, True)


a_b = make_branch(3, 4)
b_b = make_branch(1, 4)
new_car1 = make_mobil(a_b, b_b)
new_car2 = make_mobil(a_b, b_b)
new_branch1 = make_branch(2, new_car1)
new_branch2 = make_branch(1, new_car2)
new_car3 = make_mobil(new_branch1, new_branch2)
print(balanced(new_car3))


print(new_car3)
print(total_weight(new_car3))

