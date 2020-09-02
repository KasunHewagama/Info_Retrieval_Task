# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:30:54 2020

@author: Kasun_Hewagama
@Sid: IT18165180
@Batch: DS 2020
"""
#Entering the values that should permutate
Term = input("Enter the term to rotate : ") 
#Printing permuterm coresponding to inserted term
print("Term to be permutate",Term) 

a = Term + '$'
print(a)
X = len(a)
for i in range(X-1,0,-1):
    c = a[i:]+a[:i]
    print(c,Term)
print(a,Term)
