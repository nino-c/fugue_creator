from fractions import Fraction
import sys
from IPython.display import *
from abjad import *
from abjad.tools.ipythontools import *
_show = Show() # replaces native show() with ipythontools notebook inline Show()


from sympy import Matrix, Symbol, S, pprint
from sympy.polys import *
#from sympy.polys.domains.compositedomain import CompositeDomain
#from sympy.galgebra.vector import *


# Cannon in n voices
n = 4

# sample theme
_sample_theme = zip(
    [14,14,14,14,7,
        12,11,12,14,16,
        16,14,12,11,9,14,
        14,12,14,12,11,7,9,7],
    map(lambda x: Fraction(x,4), [4,2,2,4,4,
       3,1,1,1,2,
       1,1,1,1,2,2,
       2,2,3,1,2,2,
       4,4])
    )

def create_theme(notes):
    return map(lambda (i,note): 
        list(note)+ 
            [ reduce(lambda a,b: a+b, [x[1] for x in _sample_theme][:(i+1)]) ], 
            enumerate(_sample_theme))
    
sample_theme = create_theme(_sample_theme)





##########################################

"""
SymPy heirarchy

class Domain(__builtin__.object)
class Ring(sympy.polys.domains.domain.Domain)
class Field(sympy.polys.domains.ring.Ring)
class CompositeDomain(sympy.polys.domains.domain.Domain)

class FractionField(sympy.polys.domains.field.Field, 
    sympy.polys.domains.compositedomain.CompositeDomain)
"""

def output_theme(theme):
    return map(lambda x: scoretools.Note(x[0], (x[1].numerator, x[1].denominator)), theme)

theme = output_theme(sample_theme)

score = Score([])
stave = StaffGroup([], context_name='%s-voice'%(n,))

staff1 = Staff(theme)
#staff2 = Staff(theme)
stave.append(staff1)
#stave.append(staff2)
score.append(stave)
_show(stave)
