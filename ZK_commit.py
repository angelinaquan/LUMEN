from sympy import symbols
from sympy.polys.polytools import div
import numpy as np

# Define x as symbol


def commit(g, v, u, d, p1, p2, f):
    '''
    G: group of unknown order
    v: vector in Z_alpha
    u: {g, g^2, ..., g^alpha}, g randomly chosen from G
    d: degree of polynomial
    p1: masking polynomial (monic)
    p2: witness polynomial with degree < d
    f: function in Z/(x^d - 1)
    '''
    x = symbols('x')
    print("------------------------------")
    print("[commit]")
    # Calculate q(x)

    qx = sum([v_i * p1 for v_i in v]) + p2 * x**g

    # Calculate c(x)
    cx = (sum(g for g in u )* f + p1 )* qx

    return cx, qx