# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:29:03 2020

@author: Admin
"""

n=input()
c=0
for i in range (len(n)):
    x=int(n[i])
    c=c+pow(x,3)
if c==int(n):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')