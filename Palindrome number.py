# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:10:46 2020

@author: Admin
"""

N=int(input())
long=[]
c=0
while N:
    c=1
    long.append(N%10)
    N=int(N/10)
if c==0:
    if N==0:
        print("Palindrome")
else:
    for i in range(int(len(long)/2)):
        c=0
        if long[i]!=long[len(long)-i-1]:
            print('Not Palindrome')
        
if c!=0:
    print('Palindrome')