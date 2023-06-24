# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 07:29:08 2020

@author: Admin
"""

n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ",end='')
    for k in range(i):
        print("* ",end='')
    print("\n")
for i in range(n):
    for j in range(i):
        print(" ",end='')
    for k in range(n-i):
        print("* ",end='')
    print("\n")