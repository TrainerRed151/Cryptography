# Copyright © 2018 Brian Pomerantz. All Rights Reserved.


class Point:
    def __init__(self, P, curve):
        self.x = P[0]
        self.y = P[1]
        self.curve = curve


    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def __eq__(self, Q):
        return self.x == Q.x and self.y == Q.y

    def __add__(self, Q):
        if self == Q:
            return dbl(self)

        l = (Q.y - self.y) * pow(Q.x-self.x, self.curve.p-2, self.curve.p)
        xr = (l*l - self.x - Q.x) % self.curve.p
        yr = (l*(self.x - xr) - self.y) % self.curve.p

        return Point((xr, yr), self.curve)

    def dbl(self):
        l = (3*self.x*self.x + self.curve.a)*pow(2*self.y, self.curve.p-2, self.curve.p)
        xr = (l*l - self.x - self.x) % self.curve.p
        yr = (l*(self.x - xr) - self.y) % self.curve.p

        return Point((xr, yr), self.curve)

    def dbladd(self, n):
        if n == 0:
            return Point((0, 0), self.curve)
        elif n == 1:
            return self
        elif n%2 == 1:
            return self + self.dbladd(n-1)
        else:
            return (self.dbl()).dbladd(n//2)

    def __mul__(self, n):
        return self.dbladd(n)

    def __rmul__(self, n):
        return self.dbladd(n)


class Curve:
    def __init__(self, p, a, b, G):
        self.p = p
        self.a = a
        self.b = b
        self.G = G

    def getG(self):
        return Point(self.G, self)


secp256k1 = Curve(
    int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F', 16),
    0,
    7,
    (
        int('79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798', 16),
        int('483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8', 16)
    )
)
