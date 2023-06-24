# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:46:41 2020

@author: Admin
"""

a=input()
c=1
for i in range((int(len(a)/2))):
    if a[i]!=a[(len(a)-i-1)]:
        c=0
        print('Not Palindrome')
        break
if c!=0:
    print('Palindrome')