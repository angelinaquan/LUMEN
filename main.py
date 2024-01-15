import secrets
import time
from ZK_setup import setup
from PIOPprotocol import get_hx,online_phase,offline_phase
from sympy import symbols, Poly
from ZK_RecursiveProtocol import recursive_protocol
from ZK_commit import commit
from ZK_open import Open
from Crypto_func import getPrime
from ZK_VeriftEval import  verify_eval
from ZK_VerifyPoly import verify_poly
from Decision import Decision
from  fig_poly_bit import common_getsize, prove_getsize
import numpy as np

def main():
    x = symbols('x')
    '''
        给定setup函数所需的安全参数
    '''
    alpha = 3840
    d = 16
    q = 64
    time1 = time.time()
    G, v, u, d, f, p1, p2 = setup(alpha,d,q)
    time2 = time.time()
    setup_time = time2 - time1
    common_parameters_size = common_getsize(G, v, u, d, f, p1, p2)
    print(f"setup_time: {setup_time}")
    '''
        commit 阶段
    '''
    time1 = time.time()
    cx,qx = commit(secrets.choice(G), v, u, d, p1, p2, f)
    time2 = time.time()
    commit_time = time2 - time1
    print(f"commit_time: {commit_time}")
    '''
        open 阶段
    '''
    time1 = time.time()
    result  = Open(qx, cx, p2, d)
    time2 = time.time()
    openVerify_time = time2 - time1
    print(f"openVerify_time: {openVerify_time}")
    '''
        recursive_protocol 阶段
    '''
    time1 = time.time()
    keccak_256result = recursive_protocol(str(G) + str(f) + str(p1) + str(p2))
    time2 = time.time()
    recursive_protocol_time = time2 - time1
    print(f"recursive_protocol_time: {recursive_protocol_time}")
    p = getPrime(10) # 得到一个10bit长的素数
    n = 2**20
    '''
        k,N,m为定义的元组，后续可修改
    '''
    k = 32   #k不宜超过256，严重降低PIOPprotocol性能
    N = 512
    m = 256
    '''
        生成PIOPprotocol需要的h, h_prime, h_double_prime, Q, f
    '''
    time1 = time.time()
    h, h_prime, h_double_prime, Q, f = get_hx(p, k, n)
    relation ,P1, P2, P3, P4, Q1, Q2, Q3, Q4 = offline_phase(p, n, k, h, h_prime, h_double_prime, Q, f)
    r_hat,s_hat,t_hat,p_hat,r1,r2,Z = online_phase(n, k, N, m, alpha, Q, cx, P1, P2, f, h_prime, h_double_prime, qx, Q1, Q2, Q3, Q4)
    time2 = time.time()
    PIOPprotocol_time = time2 - time1
    print(f"PIOPprotocol_time: {PIOPprotocol_time}")
    prove_size = prove_getsize(Q,Q1,Q2,Q3,Q4,p_hat,r_hat,n,r2,Z,len(str(t_hat)),alpha)
    '''
        Decision ：VeriftEval + VerifyPoly + Decision
    '''
    time1 = time.time()
    judge1 ,a_hat ,b = verify_poly(u, v, d, f, p1, p2, alpha, p, q)
    judge2 = verify_eval(b, Poly(v, x), Poly(u, x), f, v)
    judge3 = Decision(Q3,alpha,u,P2,Z,len(str(t_hat)),Q,Q1,Q2,Q3,Q4,p_hat,r_hat,n,r2)
    judge = (judge1 == 1) & (judge2 == 1) & (judge3 == 1)
    time2 = time.time()
    Decision_time = time2 - time1
    print(f"Decision: {Decision_time}")
    print(f"size of common parameters: {common_parameters_size} Byte")
    print(f"size of prove: {prove_size} Byte")
    return setup_time,commit_time,openVerify_time,recursive_protocol_time,PIOPprotocol_time,Decision_time,judge,common_parameters_size,prove_size

main()