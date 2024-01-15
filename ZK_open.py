from sympy import symbols, Eq

def Open(q, c, p2, d):
    print("------------------------------")
    print("[open]")
    # Define the symbols
    x = symbols('x')

    # Calculate the left side of the equation
    left_side =  q * c

    # Calculate the right side of the equation
    right_side = p2

    # Check if the equation is satisfied
    result = Eq((left_side, x**d - 1), right_side)

    return result