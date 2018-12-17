from math import *
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from fractions import Fraction
import gmpy2
import sys

def LowPubExpo(e, ciphertext, N, iterations): #if exponent is low it is enough to take e-th root or eventually reverse mod operation and then take e-th root
                                            #user chooses how long he/she would try to find the answer by setting iterations parameter
    for i in range(iterations):
        ans = gmpy2.iroot(ciphertext, e)
        if ans[1]:
            return ans[0]
        ciphertext+=N
    return 0

def LowPubExpoList(e, list_of_moduli, list_of_ciphertexts):

    multi = 1
    for i in range(e):
        multi*=list_of_moduli[i]

    c=0
    for i in range(e):
        tmp = multi/list_of_moduli[i]
        c += list_of_ciphertexts[i]*tmp*gmpy2.invert(gmpy2.mpz(tmp),gmpy2.mpz(list_of_moduli[i]))

    c = gmpy2.t_mod(gmpy2.mpz(c), gmpy2.mpz(multi))
    c = gmpy2.iroot(c, e)

    return c



def ContinuedFractions(a, b, how_many):
    convergents = []
    z = Fraction(a,b)

    for i in range(how_many):
        convergents.append(z)
        tmp = gmpy2.div(z.numerator, z.denominator)
        if(z-tmp!=0):
            #z = Fraction(1, z-tmp)
            z = Fraction(z.denominator, z.numerator % z.denominator)
        else:
            break

    return convergents

def NWD(a, b):

    frac = [];
    while(b!=0):
        z = Fraction(a, b)
        frac.append(z)
        tmp = a % b
        a = b
        b = tmp

    return frac


def HighExpo(e, ciphertext, N, iterations): #Wienner's attack - continued fractions
    limit = gmpy2.iroot(N, 4)/3


    return 0

if __name__ == "__main__":
    mod = [377, 391, 589]
    cipher = [330, 34, 419]

    q = LowPubExpoList(3, mod, cipher)
    print(q[0])
    print(gmpy2.div(3,2))

    print( ContinuedFractions(6792605526025, 9449868410449, 10000))
    print( ContinuedFractions(1659, 2308, 10000))
    print( ContinuedFractions(47, 20, 10000))
    print (NWD(6792605526025, 9449868410449))