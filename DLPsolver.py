# -*- coding: utf-8 -*-

from Crypto.Util.number import *
from math import ceil, sqrt


def MulChine(ls):
    l = len(ls)
    inv = []
    ans = []
    mul = []
    answer = 0
    multi = 1
    for i in range(l):
        multi *= ls[i][1]
    for i in range(l):
        tmp = 1
        for j in range(l):
            if j != i:
                tmp *= ls[j][1]
        mul.append(tmp)
        ans.append(inverse(tmp, ls[i][1]))
    for i in range(l):
        answer += ls[i][0] * ans[i] * mul[i]
    return answer % multi


def IntFactor(m):
    q = []
    r = 2
    s = int(ceil(sqrt(m)))  # from math import sqrt, ceil
    while r <= s:
        if m % r == 0:
            e = 0
            while m % r == 0:
                m /= r
                e += 1
            q.append([r, e])
            s = int(ceil(sqrt(m)))
        r += 1
    if m > 1:
        q.append([m, 1])
    return q


def DLPsolver(y, g, p):
    ls = []
    q = IntFactor(p - 1)
    for re in q:
        r = re[0]
        e = re[1]
        m = p - 1
        mm = m / (r ** e)
        ymm = pow(y, mm, p)
        gmm = pow(g, mm, p)
        gg = pow(g, m / r, p)
        xr = 0
        for i in range(0, e):
            m /= r
            yy = pow(ymm, m / mm, p) * inverse(pow(gmm, (m / mm) * xr, p), p)
            ggj = 1
            for j in range(0, r):
                if yy == ggj:
                    xr += j * (r ** i)
                    break
                ggj = ggj * gg % p
        ls.append([xr, r ** e])
    return MulChine(ls) % p


if __name__ == "__main__":
    # Polling-Hellman Algorithm
    p = 64243681
    y = 36454640
    g = 7
    print DLPsolver(y, g, p)
    print pow(g, DLPsolver(y, g, p), p) == y

    # Chinese Remainder Theorem
    # x = 1 mod 3
    # x = 2 mod 5
    # x = 3 mod 7
    ls = [[1, 3], [2, 5], [3, 7]]
    print MulChine(ls)

    # Integer Factorization
    p = 878071079966331252243778198
    print IntFactor(p)
