from math import *
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import gmpy2
import sys

def FermatFactorization(N): #N must be odd
    a = gmpy2.isqrt(N) + 1
    print(a)
    b2 = a*a - N
    b = gmpy2.isqrt(b2)


    while(b*b != b2):
        a += 1
        print("hah")
        b2 = a*a-N
        b = gmpy2.isqrt(b2)
    return a - gmpy2.isqrt(b2), a + gmpy2.isqrt(b2)

