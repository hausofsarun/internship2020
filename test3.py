#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:33:11 2020

@author: hausofsarun
"""

inp = input()
inp = inp.split(' ')
ans = []
guessHistory = ''
cnt = 0
for i in range(12):
    ans.append('_')
for i in range(12):
    print(ans[i],end = ' ')
for i in range(5):
    guess = input()
    found = False
    for k in range(12):
        if guess == inp[k]:
            ans[k] = guess
            found = True
            cnt += 1
    for i in range(12):
        print(ans[i],end = ' ')
    if not found:
        guessHistory += guess+' '
    print(guessHistory)
print(cnt)