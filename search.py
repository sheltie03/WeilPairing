# -*- coding: utf-8 -*-
from Crypto.Util.number import *
from WeilPairing import WeilPair
from ecc import ModECExp, ModECAdd, ModECDbl, ValidModEC, ModECExpr
from DLPsolver import DLPsolver
from random import randint

if __name__ == "__main__":
    #  Private Set
    user = [1, 1, 1, 1, 1, 0]
    owner = [1, 1, 1, 1, 1, 1]

    tmp = 0
    for i in range(len(user)):
        tmp = tmp + user[i] * owner[i]
    print "IPvalue : ", tmp

    user = user + user
    owner = owner + owner

    #  PP
    a = 37
    b = 0
    p = 1009
    r = 7
    g = [417, 952]
    h = [561, 153]

    #  msk: bb, bstar, dd, dstar
    bb = []
    bstar = []
    for i in range(12):
        bb.append(randint(1, 6))
        bstar.append(inverse(bb[i], r))
    dd = []
    dstar = []
    for i in range(2):
        dd.append(randint(1, 6))
        dstar.append(inverse(dd[i], r))

    # Random integer
    alph = r
    alps = r
    beta = r
    bets = r
    while (alph * beta + alps * bets) % r == 0:
        alph = randint(1, 6)
        alps = randint(1, 6)
        beta = randint(1, 6)
        bets = randint(1, 6)

    #  User & Owner side
    Q1 = []
    D1 = []
    for i in range(6):
        Q1.append(ModECExpr(a, h[0], h[1], beta * user[i] * bb[i], p, r))
        D1.append(ModECExpr(a, g[0], g[1], alph * owner[i] * bstar[i], p, r))
    for i in range(6):
        Q1.append(ModECExpr(a, h[0], h[1], bets * user[i + 6] * bb[i + 6], p, r))
        D1.append(ModECExpr(a, g[0], g[1], alps * owner[i + 6] * bstar[i + 6], p, r))

    Q2 = []
    D2 = []
    Q2.append(ModECExpr(a, h[0], h[1], beta * dd[0], p, r))
    Q2.append(ModECExpr(a, h[0], h[1], bets * dd[1], p, r))
    D2.append(ModECExpr(a, g[0], g[1], alph * dstar[0], p, r))
    D2.append(ModECExpr(a, g[0], g[1], alps * dstar[1], p, r))

    #  Server side
    base = WeilPair(a, g, h, p, r)
    x = 1
    y = 1
    for i in range(len(D1)):
        x = x * WeilPair(a, D1[i], Q1[i], p, r) % p
    for i in range(len(D2)):
        y = y * WeilPair(a, D2[i], Q2[i], p, r) % p

    print "Answer  : ", DLPsolver(x, y, p) % r

# Validation on EC
#    for i in range(1, 73):
#        tmp = WeilPair(a, ModECExpr(a, g[0], g[1], i, p, r), h, p, r) 
#        gg = ModECExpr(a, g[0], g[1], i, p, r)
#        print tmp, gg, ValidModEC(a, b, p, ModECExpr(a, g[0], g[1], i, p, r))


