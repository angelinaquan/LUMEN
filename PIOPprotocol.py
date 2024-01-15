import math
from sympy import diff,symbols, Poly,div
import numpy as np
from sympy.polys.domains import GF
from sympy import Matrix
from random import randint

def get_hx(p,n,k):
    x = symbols('x')
    F = GF(p)
    # 定义多项式h, h', h''
    # h_coeffs = np.random.randint(0, p, k).tolist()
    # h_prime_coeffs = np.random.randint(0, p, k).tolist()
    # h_double_prime_coeffs = np.random.randint(0, p, k).tolist()
    # 定义符号x

    # 定义多项式h, h_prime, h_double_prime, Q, f
    h = Poly(3 * x ** 12 + x + 1, domain=F)
    h_prime = Poly(36 * x ** 11 + 1, domain=F)
    h_double_prime = Poly(396 * x ** 10, domain=F)
    Q = Poly(5 * x ** 31 + 3, domain=F)
    f = Poly(9 * x ** 15 + 3, domain=F)
    return h, h_prime, h_double_prime, Q, f

def offline_phase(p,n,k,h, h_prime, h_double_prime,Q,f):
    print("------------------------------")
    print("[PIOPprotocol]")
    x = symbols('x')
    F = GF(p)
    # 生成随机的矩阵M1和M2
    M1 = np.random.randint(0, p, (k, k))
    M2 = np.random.randint(0, p, (k, k))

    # 将 NumPy 矩阵转换为 SymPy 矩阵
    M1 = Matrix(M1)
    M2 = Matrix(M2)


    relation = h_prime - h_double_prime + (Q - h * h_double_prime) * h_prime

    # 定义和计算Qi多项式
    P1 = Poly(-x**9 + x**8 - 7*x**7 - 5*x**6 + 4*x**5 + 3*x**4 + 3*x**3 + x**2 - x, x, modulus=17)
    P2 = Poly(-6*x**9 - 3*x**8 - 6*x**7 + 8*x**6 - 2*x**5 + 7*x**4 + x**3 - 7*x**2 - 3*x - 8, x, modulus=17)
    P3 = Poly(-x**9 - 8*x**8 - 8*x**6 - 8*x**5 - 4*x**4 + 5*x**3 + x**2 + 7, x, modulus=17)
    P4 = Poly(8*x**9 + 3*x**8 - x**7 + 7*x**6 - x**5 - 8*x**4 + 5*x**3 + 8*x**2 + x - 7, x, modulus=17)
    # print("over")

    A = np.random.randint(0, p, (k, k))
    B = np.random.randint(0, p, (k, k))

    # 将 NumPy 矩阵转换为 SymPy 矩阵
    A = Matrix(A)
    B = Matrix(B)

    SUM1 = sum([M1[i, i] for i in range(k)])
    SUM2 = sum([M2[i, i] for i in range(k)])
    Q1 = Q.subs(x, x ) + SUM1 * P1.subs(x, 1) + n * P3.subs(x, 4)
    Q2 = Q.subs(x, x) + SUM2 * (P2.subs(x, 1) - Q1)
    SUMA = sum([A[i, i] for i in range(k)])
    SUMB = sum([B[i, i] for i in range(k)])
    Q3 = x * P1 - SUMA * Q1 * (x - P1)
    Q4 = x * P2 - SUMB * Q2 * (x - P2)

    '''
        算法中这里有点奇怪 A和B是矩阵  A(x)是没有意义的
    '''

    '''
    输出结果
    print(f"Q1: {Q1}")
    print(f"Q2: {Q2}")
    print(f"Q3: {Q3}")
    print(f"Q4: {Q4}")
    '''
    return relation == 0,P1, P2, P3, P4, Q1, Q2, Q3, Q4

def delta_row(m ,x , M, el):
    row = int(m / el)
    return sum(M[i + row] * x ** i for i in range(el))

def delta_col(m ,x , M, el):
    col = m % el
    return sum(M[i * el + col] * x ** i for i in range(el))

def online_phase(n,k,N,m,alpha,Q,C,P1,P2,f,h_prime, h_double_prime,q,Q1, Q2, Q3, Q4):
    # Round 1
    x = symbols('x')
    y = symbols('y')

    a1 = randint(2 ** (N - 1), 2 ** N)
    a2 = randint(2 ** (N - 1), 2 ** N)
    a3 = randint(2 ** (N - 1), 2 ** N)
    a4 = randint(2 ** (N - 1), 2 ** N)
    a5 = randint(2 ** (N - 1), 2 ** N)
    a6 = randint(2 ** (N - 1), 2 ** N)
    alpha = min(128+alpha//8, alpha)
    nig1 = alpha - a1 - a3 - 1
    nig2 = alpha - a2 - a4 - 1
    '''
    coefficients = [randint(0, 1) for _ in range(6)]  #可自定义重新生成
    Z = Poly(coefficients, x)
    coefficients = [randint(0, 1) for _ in range(6)]
    b1 = Poly(coefficients, x)
    coefficients = [randint(0, 1) for _ in range(10)]
    b2 = Poly(coefficients, x)
    '''
    Z = Poly(x ** 3 + x ** 2 + x, x, domain='ZZ')
    b1 = Poly(x, x, domain='ZZ')
    b2 = Poly(x ** 7 + x ** 4, x, domain='ZZ')
    r_hat = a1 * Q + a2 * sum(P2.eval(i) * (x**i - f.eval(i))for i in range(alpha))
    s_hat = a3 * (h_prime - sum(P1.eval(j) * x**alpha for j in range(k))) + a4 * q.eval(m+n**k)
    t_hat = h_double_prime * (x - a4) + r_hat * s_hat * a6
    '''print("rst")
        print(b1)
        print(b2)
        print(r_hat)
        print(s_hat)
        print(t_hat)
    '''
    #Round 2.
    # 验证者校验
    g_hat = b1 * (a1 * x ** 2 - a3 * x + a5) * r_hat +P1
    h_hat = b2 * (a2 * x ** 3 - a4 * x ** 2 + a6) * P2 - alpha * g_hat
    f_hat = g_hat + alpha * h_hat
    '''
        print("ghf")
        print(g_hat)
        print(h_hat)
        print(f_hat)
    '''
    # Round 3.
    t = 257 #τ
    el = 4
    M = [randint(0, 32) for _ in range(el**2)]
    p_hat = sum((h_prime.eval(m) + alpha * h_double_prime.eval(m)) * delta_row(m, x ,M, el) * delta_col(m, x ,M, el)  for m in M)
    # print(p_hat)

    array = []
    for i in range (el):
        tmp = []
        for j in range (el):
            tmp.append(M[i * el + j])
        array.append(tmp)
    M = array
    det_M = int(np.linalg.det(M))
    r1 = t * det_M * r_hat / (x**alpha)
    #print("r1")

    num_tmp1 = det_M * n**4 * (x**4 + Q2 - x**3 * Q3 - x**2 * Q4)
    num_tmp2 = -(Q + alpha * C) * Z * Z.subs(x,y)
    Q2_prime = diff(Q2,x)
    Q3_prime = diff(Q3, x)
    Q4_prime = diff(Q4, x)
    num_tmp3 = r_hat * n**2 * (x**3 + Q2_prime - x**3 * Q3_prime - x**2 * Q4_prime)
    '''
        创建一个特殊的环 包括 x和y 两个变量
        new_ring = Poly(x, y, domain='ZZ')
    '''
    num_tmp3.set_domain('ZZ')
    '''
    print(num_tmp1)
    print(num_tmp2)
    print(num_tmp3)
    '''
    T = num_tmp1 + num_tmp2 + num_tmp3
    r2 = div(T , Z)
    return r_hat,s_hat,t_hat,p_hat,r1,r2,Z




'''

# 假设的有限域参数
p = 17  # 例如，取质数17作为有限域的模
n = 16
# 定义符号
k = 10
N = 3
alpha = 25
m = 16
x = symbols('x')
q = Poly(-6*x**9 - 3*x**8 - 6*x**7 + 8*x**6 - 2*x**5 + 7*x**4 + x**3 - 7*x**2 - 3*x - 8, x, modulus=17)
h, h_prime, h_double_prime, Q, f = get_hx(p,k,n)
relation, P1, P2, P3, P4, Q1, Q2, Q3, Q4 = offline_phase(p,n,k,h, h_prime, h_double_prime,Q,f)
#print(relation, P1, P2, P3, P4, Q1, Q2, Q3, Q4)
online_phase(n,k,N,m,alpha,Q,P1,P2,f,h_prime, h_double_prime,q,Q1, Q2, Q3, Q4)

'''