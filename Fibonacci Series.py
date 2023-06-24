# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:04:57 2020

@author: Admin
"""

N=int(input())
a=0
b=1
for i in range((N)):
    if i==0:
        print(a)
    elif i==1:
        print(b)
    else:
        c=a
        a=b
        b=c+a
        print(b)