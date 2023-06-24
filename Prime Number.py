# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:13:40 2020

@author: Admin
"""

n=int(input())
c=0
if n==1 or n==2 or n==3:
    print('Not a Prime Number')
else:
    for i in range(2,(int(n/2))):
        if n%i==0:
            print('Not a Prime Number')
            c=1
            break
    if c==0:
        print('Prime Number')