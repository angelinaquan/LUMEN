from sympy import Poly, symbols


def generate_vectors(u, v, f, p1, p2, d):
    x, y = symbols("x y")
    w = [ui * vi for ui, vi in zip(u, v)]
    # r = [None for _ in range(d)]
    # s = [None for _ in range(d)]
    # t = [None for _ in range(d)]
    # print (d)
    # print(len(u))
    # for j in range(0,d):
    #     r[j] = sum(f.eval(u[i]) * x**i for i in range(j, d))
    #     s[j] = sum(p1.eval(v[i]) * x**i for i in range(j, d))
    #     t[j] = sum(p2.eval(v[i]) * x**i for i in range(j, d))
    r = sum(f.eval(u[i]) * x**i for i in range(1, min(d,len(u))))
    s = sum(p1.eval(v[i]) * x**i for i in range(1, min(d,len(u))))
    t = sum(p2.eval(v[i]) * x**i for i in range(1, min(d,len(u))))
    return w, r, s, t



def generate_functions(u, v, w, r,  alpha):
    x, y = symbols("x y")
    a_func = sum(u[i] * x * y**(i-alpha) + y**alpha * v[i] * x**(-i) - x**alpha * w[i] * y for i in range(min(alpha,alpha//5 + 72),alpha//16+108))
    # print("a_func",end = ' :')
    # print(a_fun
    b_func = sum((x**alpha *u[i] * y**(i) - v[i] * x * (y ** (-alpha) - x ** i) - y**i * (x**(-i) - x**i) * w[i]) for i in range(min(alpha,alpha//5 + 72,alpha//16+108)))
    # print("b_func",end = ' :')
    # print(b_func)
   # d_func = sum((x ** (-i) - y ** i) * u[i] * r[i] - x ** (-alpha) * v[i] * w[i] + w[i] * x ** (-i - alpha) for i in range(min(alpha, d)))

    d_func = sum((x**(-i) - y**i) * u[i] * r - x**(-alpha) * v[i] * w[i] + w[i] * x**(-i-alpha) for i in range(min(alpha,alpha//5 + 72,alpha//16+108)))
    # print("d_func",end = ' :')
    # print(d_func)
    e_func = a_func + b_func - d_func
    # print("e_func",end = ' :')
    # print(e_func)
    return a_func, b_func, d_func, e_func

def verify_poly(u,v,d,f,p1,p2,alpha, p, q):
    print("------------------------------")
    print("[verify_poly]")
    w, r, s, t = generate_vectors(u, v, f, p1, p2, d)
    a, b, d, e = generate_functions(u, v, w, r, alpha)
    '''
    print(type(a))
    print(type(b))
    print(type(d))
    print(type(e))
    '''
    x, y = symbols("x y")
    m = a
    n = a
    r = a
    # n = b(p, 1)
    # r = e(p, q)

    return r == p * (d.subs({x: m, y: n}) + n) - q ,a ,b