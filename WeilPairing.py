# -*- coding: utf-8 -*-
from Crypto.Util.number import *
from ecc import ModECExp, ModECAdd, ModECDbl


def Lfunc(a, g, h, var, p):
    if g == h:
        v = (((3 * pow(g[0], 2, p) + a) % p) * inverse((2 * g[1]) % p, p)) % p
    else:
        v = (((h[1] - g[1]) % p) * inverse(h[0] - g[0], p)) % p
    return (var[1] - (v * (var[0] - g[0]) + g[1])) % p


def Vfunc(g, var, p):
    return (var[0] - g[0]) % p


def Gfunc(a, g, h, var, p):
    if g[0] == h[0] and g[1] == (- h[1] % p):
        return (var[0] - g[0]) % p
    elif g == h:
        vinv = inverse(Vfunc(ModECDbl(a, g[0], g[1], p), var, p), p)
        return (Lfunc(a, g, g, var, p) * vinv) % p
    else:
        vinv = inverse(Vfunc(ModECAdd(g[0], g[1], h[0], h[1], p), var, p), p)
        return (Lfunc(a, g, h, var, p) * vinv) % p


def Miller(a, g, h, n, p):
    t = []
    arr = bin(n)[2:]
    f = 1
    t = g
    for i in range(1, len(arr)):
        f = (pow(f, 2, p) * Gfunc(a, t, t, h, p)) % p
        t = ModECDbl(a, t[0], t[1], p)
        if int(arr[i]) == 1:
            f = (f * Gfunc(a, t, g, h, p)) % p
            t = ModECAdd(t[0], t[1], g[0], g[1], p)
    return f % p


def WeilPair(a, g, h, p, r):
    if g == h:
        return 1
    elif g[0] == "inf" or h[0] == "inf":
        return 1
    else:
        minv = inverse(Miller(a, h, g, r, p), p)
        return (- Miller(a, g, h, r, p) * minv) % p


if __name__ == "__main__":
    a = 0
    b = 11
    p = 31
    r = 5
    g = [2, 9]
    h = [3, 10]

    print Miller(a, g, h, r, p) == 10
    print Miller(a, g, ModECExp(a, h[0], h[1], 2, p), r, p) == 20
    print Miller(a, g, ModECExp(a, h[0], h[1], 3, p), r, p) == 23
    print WeilPair(a, g, ModECExp(a, h[0], h[1], 5, p), p, r)

    a = 37
    b = 0
    p = 1009
    r = 7
    g = [417, 952]
    h = [561, 153]

    print Miller(a, g, h, r, p)
    print Miller(a, h, g, r, p)
    print WeilPair(a, g, h, p, r)
    print (Miller(a, g, h, r, p) * inverse(Miller(a, h, g, r, p), p)) % p
    print pow((Miller(a, g, h, r, p) * inverse(Miller(a, h, g, r, p), p)), 7, p)

    #  homomorphism
    print WeilPair(a, ModECExp(a, g[0], g[1], 2, p), ModECExp(a, h[0], h[1], 2, p), p, r)
    print WeilPair(a, ModECExp(a, g[0], g[1], 4, p), ModECExp(a, h[0], h[1], 1, p), p, r)
    print pow(WeilPair(a, g, h, p, r), 4, p)
