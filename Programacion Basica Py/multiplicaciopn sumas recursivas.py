# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:36:29 2020

@author: Estudiantes
"""

def multsumasrecursivas(m,n):
    if n==1:
        return m
    return m+multsumasrecursivas(m,n-1)
print(multsumasrecursivas(int(input("ingrese un numero")),int(input("ingrese otro numero"))))