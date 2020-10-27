import numpy as np
from sympy import *

x = Symbol("x")

def f(x):
    return x**3 - 3*x**2 - 6*x

def g(x,h):
    return (f(x+h) - f(x-h)) / (h*2)

def f_prim(x):
    return (3*x**2 - 6*x - 6)

# diff = [g(2.5, a) for a in np.linspace(0.101, 0.0, 10)]

diff = []

for h in np.linspace(hsd):
    diff.appned(g(2.5, h))

print(diff)
print("")
print(f_prim(2.5))

# evaluate f for interval [2.0, 3.0]
# find the gradient between the points = p
# find the gradient using the forumla g = q
# compare p and q