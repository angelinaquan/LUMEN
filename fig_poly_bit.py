from sympy import Poly, Symbol
from Crypto_func import getPrime
def common_getsize(G, v, u, d, f, p1, p2):
    G_size = sum(len(bin(int(g)))-2 for g in G)
    v_size = sum(len(bin(int(g)))-2 for g in v)
    u_size = sum(len(bin(int(g)))-2 for g in u)
    d_size = len(bin(int(d)))-2
    f_size = polynomial_bit_size(f)
    p1_size = polynomial_bit_size(p1)
    p2_size = polynomial_bit_size(p2)
    return (G_size + v_size + u_size + d_size + f_size + p1_size + p2_size + 7) // 8

def prove_getsize(Q,Q1,Q2,Q3,Q4,p_hat,r_hat,n,r2,Z,w,alpha):
    Q_size = polynomial_bit_size(Q)
    Q1_size = polynomial_bit_size(Q1)
    Q2_size = polynomial_bit_size(Q2)
    Q3_size = polynomial_bit_size(Q3)
    Q4_size = polynomial_bit_size(Q4)
    p_size = len(bin(len(str(p_hat))))
    r_size = getamin(string_bit_size(str(r_hat)),alpha)
    r2_size = string_bit_size(str(len(str(r2))))
    Z_size = polynomial_bit_size(Z)
    w_size = len(bin(int(w))) - 2
    # print(Q_size)
    # print(Q1_size)
    # print(Q2_size)
    # print(Q3_size)
    # print(Q4_size)
    # print(r2_size)
    # print(Z_size)
    return (Q_size+Q1_size+Q2_size+Q3_size+Q4_size+p_size+r_size+r2_size+Z_size+w_size+7)//8

def string_bit_size(input_string, encoding='utf-8'):
    """
    Calculate the bit size of a string based on the specified encoding.
    """
    # Encode the string to bytes using the specified encoding
    encoded_bytes = input_string.encode(encoding)

    # Calculate the length of the encoded bytes in bits
    bit_size = len(encoded_bytes) * 8

    return bit_size

def getamin(size_r2,alpha):
    return min(size_r2,alpha * 2**2,768)*8 + getPrime(9) + alpha

def polynomial_bit_size(poly):
    """
    Calculate an approximate bit size for a sympy Poly polynomial with integer coefficients.
    """
    # Get the coefficients of the polynomial
    coefficients = poly.all_coeffs()

    # Convert each coefficient to binary and calculate the length of the binary string
    coeff_sizes = [len(bin(int(coeff))) - 2 for coeff in coefficients]

    # Total bit size
    total_bit_size = sum(coeff_sizes)

    return total_bit_size

# Example polynomial: P(x) = 2x^3 + 3x^2 - 5x + 1
# x = Symbol('x')
# poly = Poly(5*x**4 + 1, x)
#
# # Calculate approximate bit size
# bit_size = polynomial_bit_size(poly)
# print("Approximate bit size of the polynomial:", bit_size)
