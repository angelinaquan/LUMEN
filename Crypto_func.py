from random import randint
import math
from Crypto.Hash import keccak


def fast_modular(x,times,mod):#快速模幂运算
    res = 1
    tmp = x
    while times != 0:
        if times%2 == 1:
            res = (res * tmp)%mod
        times = times//2
        tmp = (tmp*tmp)%mod
    return res % mod

def isprime(n):#素性检测
    if n == 1:
        return 0
    if n == 2:
        return 1
    m,k = n-1,0
    while m %2 == 0:
        a = randint(2,n-1)
        x = fast_modular(a,m,n)
        if x == 1 or x == n-1:
            return 1
        while k>1:
            x = fast_modular(x,2,n)
            if x == n-1 :
                return 1
            k = k-1
        return 0

def chaos_maker(p, g, seed):
    res = 0
    x = seed
    for _ in range(randint(0, 114514)):
        x = pow(g, x, p)
    for i in range(256):
        x = pow(g, x, p)
        if x < (p - 1) // 2:
            res -= (1 << i) - 1
        elif x > (p - 1) // 2:
            res += (1 << i) + 1
        else:
            res ^= (1 << i + 1)
    return res if res > 0 else -res

def keygen(p, g):
    u, v = chaos_maker(p, g, randint(0, 1 << 64)), chaos_maker(p, g, randint(0, 1 << 64))
    return next_prime(u**2+v**2),next_prime(2*u*v)

def randomnum(p,q,s,len):
    numarray = ''
    n = q*p
    tmp = s*s%n
    for i in range (len):
        tmp = tmp*tmp % n
        numarray += str(tmp%2)
    return numarray

def next_prime(num):
    while isprime(num) == 0:
        num+=3
    return num

def issafeprime(number):
    q = int((number-1) / 2)
    return isprime(q)

def getPrime(N):
    number = randint(2 ** (N - 1), 2 ** N)   #generate_random_odd
    if number % 2 == 0 :
        number = number +1
    while (not isprime(number)):    #if not prime: ++2
        number = number + 2
    return number

def getsafePrime(N):
    number = randint(2 ** (N - 1), 2 ** N)   #generate_random_odd
    if number % 2 == 0 :
        number = number +1
    while (not isprime(number) or not issafeprime(number)):    #if not prime: ++2
        number = number + 2
    return number

def keccak_256(data):
    # 创建 Keccak 对象
    keccak_hash = keccak.new(digest_bits=256)

    # 更新数据
    keccak_hash.update(data.encode('utf-8'))

    # 获取结果
    hash_result = keccak_hash.hexdigest()
    return hash_result