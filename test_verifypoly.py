from ZK_VerifyPoly import verify_poly
from ZK_setup import setup
from Crypto_func import getPrime

alpha = 120      #安全参数
d = 32
q = 256
p = getPrime(q)

G, v, u, d, f, p1, p2= setup(alpha, d, q)

print(G)
print(v)
print(u)
print(d)
print(p2)
c = "some polynomial representation"
result = verify_poly(u,v,c,d,f,p1,p2,alpha, p, q)
print(result)