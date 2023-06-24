# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:52:27 2020

@author: Soumick
"""

test_cases=int(input())
content=[]
for i in range(test_cases):
    x=list(map(int,input().split()))
    for j in range(12):
        if x.count(x[j])==4:
            continue
        else:
            content.append('No')
            break
    else:
        content.append('Yes')
for i in range(len(content)):
    print(content[i])
