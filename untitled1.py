#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:19:15 2020

@author: em583r
"""

def squareRoot(x):
    epsilon = 0.01
    numGuesses = 0
    low = 0
    high = x
    ans = (high + low)/2
    print(str(ans))
    while abs(ans**2-x) >= epsilon:
        numGuesses += 1
        if ans**2 < x:
            print("********" + str(ans**2) + "is less than " + str(x))
            low = ans
        else:
            print("********" + str(ans**2) + "is greater than " + str(x))
            high = ans
        ans = (high + low)/2
    print("it took " + str(numGuesses) + " to get to the answer: " + str(int(ans)))
    
    
    
    
    
    
    