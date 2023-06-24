# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:59:27 2020

@author: Admin
"""

x=int(input())
y=int(input())
if x>y:
    x=x-y
    y=x+y
    x=y-x
else:
    y=y-x
    x=x+y
    y=x-y
print(x)
print(y)