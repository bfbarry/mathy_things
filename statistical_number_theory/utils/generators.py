import numpy as np
import matplotlib.pyplot  as plt
import json
import math
import decimal

def pi_dig(prec):
    """
    Compute Pi to the current precision.
    Taken from https://docs.python.org/3/library/decimal.html#recipes
    """
    decimal.getcontext().prec = prec
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    pi = +s               # unary plus applies the new precision
    pi_dig = [int(i) for i in str(pi)[2:]]
    return pi_dig

def rational_num_dig(num, denom, prec):
    decimal.getcontext().prec = prec
    d = str(decimal.Decimal(num) / decimal.Decimal(denom))[2:]
    return [i for i in d]

def sqrt_dig(num, prec, dec = True):
    """If dec = True, only returns digits to the right of the decimal place"""
    decimal.getcontext().prec = prec
    d = str(decimal.Decimal(num)**decimal.Decimal(.5)) #math.sqrt doesn't work for this
    
    if dec == True:
        d = d[d.index('.')+1:]
    else:
        d = d.replace('.','')
    
    return [i for i in d]
