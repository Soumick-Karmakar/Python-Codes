# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:15:55 2020

@author: Admin
"""

lst=list(map(int,input().split()))
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]<lst[j]:
            n=lst[i]
            lst[i]=lst[j]
            lst[j]=n
for i in range(len(lst)):
    print(lst[i])