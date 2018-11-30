from math import *
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import gmpy2
import sys

def LowExpo(e, ciphertext, N, iterations): #if exponent is low it is enough to take e-th root or eventually reverse mod operation and then take e-th root
                                            #user chooses how long he/she would try to find the answer by setting iterations parameter
    for i in range(iterations):
        ans = gmpy2.iroot(ciphertext, e)
        if ans[1]:
            return ans[0]
        ciphertext+=N
    return 0

def HighExpo(e, ciphertext, N, iterations):
    return 0
