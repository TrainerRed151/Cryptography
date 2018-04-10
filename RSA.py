# Copyright © 2018 Brian Pomerantz. All Rights Reserved.

# Code to implement RSA Encryption Scheme with Optimally Asymmetric Encryption Padding (OAEP)

import os
import math

class RSAKey:
    def __init__(self, n=0, e=0, d=0, p=0, q=0):
        if d == 0 or p == 0 or q == 0:
            self.private = False
        else:
            self.private = True
        
        self.n = n
        self.e = e
        self.d = d
        self.p = p
        self.q = q

    def __repr__(self):
        extra = ""
        if self.private:
            extra = ", d=%d, p=%d, q=%d" % (self.d, self.p, self.q)

        return "RSAKey(n=%d, e=%d%s)" % (self.n, self.e, extra)

    def __str__(self):
        extra = ""
        if self.private:
            extra = ", d=%d, p=%d, q=%q" % (self.d, self.p, self.q)

        return "(n=%d, e=%d%s)" % (self.n, self.e, extra)
    
    def publicKey(self):
        return RSAKey(n=self.n, e=self.e)

    def can_decrypt(self):
        return self.private

    def size_in_bits(self):
        return n.bit_length()

    def size_in_bytes(self):
        return (n.bit_length()-1)//8 + 1


def lcm(a, b):
    return (a*b)//math.gcd(a, b)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return (g, x - (b//a)*y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Modular multiplicative inverse does not exist.")
    else:
        return x % m

def getPrime(bits):
    test = 0
    while test != 1:
        p = int.from_bytes(os.urandom((bits+7)//8), 'big')
        test = pow(2, p-1, p)

    return p


def generate(bits, e=65537):
    if e % 2 == 0 or e < 3:
        raise ValueError("RSA public exponent must be a positive, odd integer larger than 2.")

    p = 0
    q = 0
    while ((p - q) < 2**(bits//4)):
        p = getPrime(bits//2)
        q = getPrime(bits - p.bit_length())

    if q > p:
        temp = q
        q = p
        p = temp

    n = p*q
    lam = lcm(p-1, q-1)
    d = modinv(e, lam)
    
    if (e*d) % lam != 1:
        raise Exception("Private exponent derivation error.")

    return RSAKey(n=n, e=e, d=d, p=p, q=q)
