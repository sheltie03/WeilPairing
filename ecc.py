# -*- coding: utf-8 -*-
from Crypto.Util.number import *


def ModECAdd(x1, y1, x2, y2, p):
    if x1 == "inf":
        return [x2, y2]
    elif x2 == "inf":
        return [x1, y1]
    elif (x1 - x2) % p == 0 and (y1 + y2) % p == 0:
        return ["inf", "inf"]
    else:
        v = (((y2 - y1) % p) * inverse(x2 - x1, p)) % p
        x3 = (pow(v, 2, p) - x1 - x2) % p
        y3 = (v * (x1 - x3) - y1) % p
        return [x3, y3]


def ModECDbl(a, x, y, p):
    if y == "inf" or y % p == 0:
        return ["inf", "inf"]
    else:
        v = (((3 * pow(x, 2, p) + a) % p) * inverse((2 * y) % p, p)) % p
        xx = (pow(v, 2, p) - (2 * x) % p) % p
        yy = ((v * (x - xx)) % p - y) % p
        return [xx, yy]


def ModECExp(a, x, y, k, p):
    if k == 0:
        return ["inf", "inf"]
    arr = bin(k)[2:]
    g = [x, y]
    for i in range(1, len(arr)):
        g = ModECDbl(a, g[0], g[1], p)
        if int(arr[i]) == 1:
            g = ModECAdd(g[0], g[1], x, y, p)
    return g


def ModECExpr(a, x, y, k, p, r):
    k = k % r
    if k == 0:
        return ["inf", "inf"]
    arr = bin(k)[2:]
    g = [x, y]
    for i in range(1, len(arr)):
        g = ModECDbl(a, g[0], g[1], p)
        if int(arr[i]) == 1:
            g = ModECAdd(g[0], g[1], x, y, p)
    return g


def ValidModEC(a, b, p, g):
    if isinstance(g[0], str):
        return True
    else:
        return pow(g[1], 2, p) == (pow(g[0], 3, p) + a * g[0] + b) % p
