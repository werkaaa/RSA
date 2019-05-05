import gmpy2

#Let's imagine a situation, where we have a group of users with the same N and each of them has a unique pair of public/private exponents ei, di

def Recover(e, d, N): #recovers factorization of N from private and public exponent
    #we get x that is coprime with N
    x = 2
    flag = True
    flag2 = True
    while flag:
        if flag2:
            x = 2
            flag2 = False
        else:
            x = gmpy2.next_prime(x)%N
        po = (e*d-1)/2
        y = gmpy2.powmod(gmpy2.mpz(x), gmpy2.mpz(po), N)
        while (y==1 or y==-1) and po%2==0:
            po = po/2
            y = gmpy2.powmod(gmpy2.mpz(x), gmpy2.mpz(po), N)
        if y!=1 and y!= -1:
            p = gmpy2.gcd(N, y-1)
            q = y-1
            return p,q

#Attack from the inside
#We want to know ones private exponent, having our exponents and the modulus
def FindPrivate(e1, d1, e2, N): #We want to find ones private exponent
    p, q = Recover(e1, d1, N) #We recover factorization of N from our own exponents
    phi = (p-1)*(q-1)
    return gmpy2.invert(e2, phi)

#Attack from the outside
#Eve sees two ciphertexts c1, c2 of the same message m. She also has e1, e2 and N
def FindMessage(c1, c2, e1, e2, N):
    t1 = gmpy2.invert(e1, e2)
    print(t1)
    t2 = (t1*e1 - 1)//e2
    print(t2)
    return (gmpy2.powmod(c1, t1, N)*gmpy2.powmod(c2, -t2, N))%N

if __name__ == "__main__":
    print(Recover(17, 507905, 1441499))
    print(FindMessage(1514, 8189, 11, 5,18923))
