from sympy import symbols, Poly
def calculate_f_of_v(f, v):
    x = symbols('x')
    return f + Poly(v, x)


def calculate_b_hat_times_v_prime(b_hat, v):

    return b_hat * len(v)


def calculate_u_prime_times_len_v(u_prime, v):
    return u_prime * len(v)


def verify_eval(b_hat, v_prime, u_prime, f, v):
    print("[verify_eval]")
    f_of_v = calculate_f_of_v(f, v)
    bhat_times_vprime = calculate_b_hat_times_v_prime(b_hat, v)
    uprime_times_len_v = calculate_u_prime_times_len_v(u_prime, v)

    # Check the relation
    if f_of_v == bhat_times_vprime :
        return 1
    else:
        return 0
