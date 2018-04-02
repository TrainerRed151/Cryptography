# Copyright © 2018 Brian Pomerantz. All Rights Reserved.

# Code to implement RSA Encryption Scheme with Optimally Asymmetric Encryption Padding (OAEP)

class RSAKey:
    def __init__(self, n, e, d=0, p=0, q=0):
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
            extra = ", d=%d, p=%d, q=%q" % (self.d, self.p, self.q)

        return "RSAKey(%d, %d%s)" % (self.n, self.e, extra)

    def __str__(self):
        extra = ""
        if self.private:
            extra = ", d=%d, p=%d, q=%q" % (self.d, self.p, self.q)

        return "n=%d, e=%d%s" % (self.n, self.e, extra)
    
    def publicKey(self):
        return RSAKey(self.n, self.e)

    def can_decrypt(self):
        return self.private

    def size_in_bits(self):
        return n.bit_length()

    def size_in_bytes(self):
        return (n.bit_length()-1)//8 + 1

def generate(bits, e=65537):
    if e % 2 == 0 or e < 3:
        raise ValueError("RSA public exponent must be a positive, odd integer larger than 2.")


