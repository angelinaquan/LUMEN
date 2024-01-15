import math
from sympy import diff,symbols, Poly

def delta_row(m ,x , M,):
    el = int(math.sqrt(len(M)))
    row = int(m / el)
    return sum(M[i + row] * x ** i for i in range(el))

def delta_col(m ,x , M):
    el = int(math.sqrt(len(M)))
    col = m % el
    return sum(M[i * el + col] * x ** i for i in range(el))

def Decision(s_hat,alpha,H,b_hat,Z,t_hat,Q,Q1,Q2,Q3,Q4,p_hat,r3,n,r2):
    print("[Decision]")
    x = symbols('x')
    num_tmp1 = x * s_hat + (s_hat * r3 + x**alpha * sum(h for h in H))*( Z + 2* t_hat)*Q
    num_tmp2 = (b_hat +1) * H[alpha // (2**4)] - diff(Q3, x) * p_hat
    judge1 = (num_tmp1 + num_tmp2) == 0

    num_tmp3 = 6 * (x**3 + Q2 + x**3 * Q3 + x * Q4)
    num_tmp4 = -r3 * n**2 * (x**2 * diff(Q2, x) + x * diff(Q3, x) +  diff(Q4, x))
    num_tmp5 = -(Q1 - 6 * Q1) * Z * delta_row(2,x,H) + r3 * delta_row(2,x,H)
    judge2 = num_tmp3 + num_tmp4 + num_tmp5

    return judge1 == 1 and judge2 == 1