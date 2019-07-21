from math import sqrt, cos, sin
import math as m

square = lambda x: x * x

atan = lambda x, y: m.atan(x / y)

class Rectangular:
    
    def __init__(self, imag):
        self.imag = imag
        
    def __str__(self):
        return self.imag
    
    def __repr__(self):
        return self.imag
    
class Polar:
    
    def __init__(self, imag):
        self.imag = imag
        
    def __str__(self):
        return self.imag
    
    def __repr__(self):
        return self.imag
    
polar = Polar('Polar')
rectangular = Rectangular('Rectangular')

def pair(elem):
    try:
        elem[0]
        elem[1]
        return True
    except:
        return False

def attach_tag(type_tag, contents):
    return [type_tag, contents]

def typ_tag(datum):
    if pair(datum):
        return datum[0]
    raise Exception("TYPE-TAG error {} is not correct".format(datum))

def contents(datum):
    if pair(datum):
        return datum[1]
    raise Exception("CONTENTS error {} is not correct".format(datum))

def is_rectangular(z):
    return isinstance(type_tag(z), Rectangular)

def is_polar(z):
    return isinstance(type_tag(z), Polar)

##########################################Rectangular#################################3

def real_part_rectangular(z):
    return z[0]

def imag_part_rectangular(z):
    return z[1]

def magnitude_rectangular(z):
    return sqrt(square(real_part(z)) + square(imag_part(z)))

def angle_rectangular(z):
    return atan(imag_part(z), real_part(z))

def make_from_real_imag_rectangular(x, y):
    return attach_tag(rectangular, [x, y])

def make_from_mag_ang_rectangular(r, a):
    return attach_tag(rectangular, [r * cos(a), r * sin(a)])

#############################Polar########################################

def magnitude_polar(z):
    return z[0]

def angle_polar(z):
    return z[1]

def real_part_polar(z):
    return magnitude_polar(z) * cos(angle_polar(z))

def imag_part_polar(z):
    return magnitude_polar(z) * sin(angle_polar(z))

def make_from_real_imag_polar(x, y):
    return attach_tag(polar, [sqrt(square(x) + square(y)), atan(x, y)])

def make_from_mag_ang_polar(r, a):
    return attach_tag(polar, [r, a])

def real_part(z):
    if is_rectangular(z):
        return real_part_rectangular(contents(z))
    elif is_polar(z):
        return real_part_polar(contents(z))
    else:
        raise Exception('unknown type REAL-PART {}'.format(z))
    
def imag_part(z):
    if is_rectangular(z):
        return imag_part_rectangular(contents(z))
    elif is_polar(z):
        return imag_part_polar(contents(z))
    else:
        raise Exception('unknown type IMAG-PART {}'.format(z))    
    
def magnitude(z):
    if is_rectangular(z):
        return magnitude_rectangular(contents(z))
    elif is_polar(z):
        return magnitude_polar(contents(z))
    else:
        raise Exception('unknown type MAGNITUDE {}'.format(z))
    
def angle(z):
    if is_rectangular(z):
        return angle_rectangular(contents(z))
    elif is_polar(z):
        return angle_polar(contents(z))
    else:
        raise Exception('unknown type ANGLE {}'.format(z))
    
def make_from_real_imag(x, y):
    return make_from_real_imag_rectangular(x, y)

def make_from_mag_ang(r, a):
    return make_from_mag_ang_polar(r, a)
    
def add_complex(z1, z2):
    return make_from_real_imag(real_part(z1) + real_part(z2), imag_part(z1) + imag_part(z2))

def sub_complex(z1, z2):
    return make_from_real_imag(real_part(z1) - real_part(z2), imag_part(z1) - imag_part(z2))

def mul_complex(z1, z2):
    return make_from_mag_ang(magnitude(z1) * magnitude(z2), angle(z1) + angle(z2))

def div_complex(z1, z2):
    return make_from_mag_ang(magnitude(z1) / magnitude(z2), angle(z1) - angle(z2))