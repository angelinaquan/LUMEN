from ZK_setup import setup
from Crypto_func import getPrime
from. import main
alpha = 256      #安全参数
d = 256
q = 256


G, v, u, d, f, p1, p2= setup(alpha, d, q)
print(G)
print(v)
print(u)
print(d)
print(p2)