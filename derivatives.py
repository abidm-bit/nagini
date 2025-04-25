"""
given a function f(x) = position
dy/dx of f(x) = f' =  first derivative = velocity (speed)
dy/dx of f' = f'' = second derivative = acceleration
dy/dx of f'' = f''' = third derivative = jerk

"""


from sympy import *
import sympy as sym
# sympy is a package to display math functions

# consider the function:   f(x) = 4x^4 + 3x^3 + 8x^2 + 24
"""
                           4     3       2    
                        4⋅x  + 3⋅x  + 8⋅x + 24
"""

# store the variable as a symbol
x=sym.Symbol('x')

# store the function
function = (4*x**4)+(3*x**3)+(8*x**2) + 24

# the first derivative:
dr = function.diff(x)

print(dr)
"""
                    printing the first derivative looks like this:
                                16*x**3 + 9*x**2 + 16*x
"""

print("\n")

# to make it readable, mathematical format:
sym.init_printing()

# now printing the first derivative
sym.pprint(dr)

print("\n")

"""
                    printing the first derivative looks like this:
                            3      2       
                        16⋅x  + 9⋅x  + 16⋅x
"""

# the second derivative:
dr2 = dr.diff(x)

# now printing the second derivative
sym.pprint(dr2)

print("\n")

"""                         2            
                        48⋅x  + 18⋅x + 16
"""

# the third derivative:
dr3 = dr2.diff(x)

# now printing the third derivative
sym.pprint(dr3)

print("\n")

"""                                     
                        96⋅x  + 18 
"""
