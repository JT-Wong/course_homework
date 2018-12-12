# -*- coding: utf-8 -*-
import math


def fun(n):
    H_n = 0.0
    G_n = 0.0
    i = 1
    while i <= n:
        H_n += 1/i
        i += 1

    s_l = []
    m = int(math.sqrt(n))
    i = 2
    tem_n = n
    while (i <= m+1):
        if tem_n % i == 0:
            # s_l.append(i)
            G_n += i
            while (tem_n % i == 0):
                tem_n = tem_n/i

        i += 1


    if tem_n != 1:
        G_n += i
        # s_l.append(tem_n)

    print(H_n)
    print(math.exp(H_n))
    print(math.log(H_n, math.e))
    print(H_n + math.exp(H_n) * math.log(H_n, math.e))
    print(G_n)


fun(1023)
