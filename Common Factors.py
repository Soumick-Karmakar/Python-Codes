# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:44:40 2020

@author: Admin
"""

def even(x):
  a=int(x**0.5)
  print(a,end=' ')
  if a%2==0:
    even(a)
  else:
    if a!=1:
      odd(a)


def odd(x):
  if x==1:
    print(x)
  else:
    a=int((x**0.5)**3)
    print(a,end=' ')
    if a%2==0:
      even(a)
    else:
      odd(a)


test=int(input())
val=[]
for i in range(test):
  val.append(int(input()))
for i in range(test):
  x=val[i]
  print(x,end=' ')
  if x%2==0:
    even(x)
  else:
    odd(x)
  print('\n')
     