# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

data = []
x = int(input("Enter num input: "))
for i in range(x):
    wordInput = input()
    data.append(wordInput)

for j in range(x):
    word = data[j]
    a = word.split(' ')
    s = ''
    for b in a:
        if b[0].isupper():
            s += b[0]
    data[j] = s
for w in data:
    print(w)

