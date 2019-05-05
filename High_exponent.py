from fractions import Fraction
import gmpy2


def ContinuedFractions(a, b):
    fractions = []
    z = Fraction(a, b)
    conv1 = 0
    conv2 = 1
    convergents = [0, 1]

    limit  = gmpy2.iroot(b, 4)[0]/3

    while conv2<=limit:
        fractions.append(z)
        tmp = gmpy2.div(z.numerator, z.denominator)
        if(z-tmp!=0):
            z = Fraction(z.denominator, z.numerator % z.denominator)
        else:
            break
        h = conv2 *(z.numerator //  z.denominator) + conv1
        conv1 = conv2
        conv2 = h
        convergents.append(conv2)

    return convergents

def CheckExpo(e, N):
    test_val = N // 2 + 3
    exponents = ContinuedFractions(e, N)
    test_val_tmp = pow(test_val, e, N)
    for i in exponents:
        if pow(test_val_tmp, i, N)== test_val: return i

    return false

def HighPubExpo(e, N, ciphertext):
    d = CheckExpo(e, N)
    if d: return pow(ciphertext, d, N)

    return false


if __name__ == "__main__":
    print( ContinuedFractions(6792605526025, 9449868410449))
    print( ContinuedFractions(13, 7))
    print (CheckExpo(6792605526025, 9449868410449))
    print(HighPubExpo(6792605526025, 9449868410449, 1005))
    print(pow(5084082073372, 6792605526025, 9449868410449))

