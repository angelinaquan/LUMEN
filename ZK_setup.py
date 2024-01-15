import secrets
from sympy import symbols, Poly
from sympy.abc import x

def gen_vector(alpha, q):
    """
    Generate a vector in Z^alpha with elements in [0, q)
    """
    return [secrets.randbelow(q) for _ in range(alpha)]

def gen_poly(d, q):
    """
    Generate a polynomial with degree < d with coefficients in [0, q)
    """
    coeff = [secrets.randbelow(q) for _ in range(d)]
    return Poly(coeff, x)


def setup(alpha, d, q):
    """
    Args:
    alpha (int): size of the vector v
    d (int): degree of polynomial
    q (int): order of group G

    Returns:
    tuple: public parameters (G, v, u, d, p2)
    """
    # Sample a group of order q
    print("------------------------------")
    print("[setup]")
    G = gen_vector(alpha, q)

    # Randomly choose g from G
    g = secrets.choice(G)

    # Generate a vector v in Z^alpha
    v = gen_vector(alpha, q)

    # Let u = {g, g^2, ..., g^alpha} mod q
    u = [pow(g, i, q) for i in range(1, alpha + 1)]

    # Choose a function f(x) in Z/(x^d - 1)
    f = Poly(x ** d - 1)

    # Generate a masking polynomial p1(x) (monic) and a witness polynomial p2(x) with degrees < d
    p1 = gen_poly(d, q)
    p2 = gen_poly(d, q)

    # Publish the public parameters (G, v, u, d, p2(x))
    return (G, v, u, d, f, p1, p2)