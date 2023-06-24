# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:36:50 2021

@author: SOUMICK KARMAKAR
"""

def divide(a,lst):
    for i in range(2,10):
        if a%i==0:
            lst.append(str(i))
            a=int(a//i)
            if len(str(a))>1:
                lst=divide(int(a),lst)
            else:
                if a!=1:
                    lst.append(str(a))
            return lst
    else:
        return None


a=int(input())
z=a//2
z+=1
lst=[]
val=[]
for i in range(2,10):
    print(i)
    if a%i==0:
        lst.append(str(i))
        a/=i
        lst=divide(a,lst)
        if lst!=None:
            val.append(int(''.join(lst)))
if len(val)>=1:
    print(val)
else:
    print ('Not Possible')

