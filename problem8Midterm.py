#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:59:33 2020

@author: em583r
"""

def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    for i in L:
        if not g(f(i)):
            L.remove(i)
    return max(L)

L = [0, -10, 5, 6, -4]

print(applyF_filterG(L, f, g))
print(L)