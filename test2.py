#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:29:20 2020

@author: hausofsarun
"""
def isPrimeNumber(x):
    if x > 1:
        for i in range(2,x//2):
            if (x % i) == 0:
                return False
        else:
            return True
    else:
        return False

def isFloatPrime(num):
#    if len(num) < 3:
#        return "Error"
    x = ''
    for i in range(3):
        x += num[i]
        if isPrimeNumber(int(x)) == True:
            return True
    return False
    


while True:
    inp = input()
    if inp == '0.0':
        break
    a = inp.split('.')
    num = a[0]+a[1]
    print(isFloatPrime(num))