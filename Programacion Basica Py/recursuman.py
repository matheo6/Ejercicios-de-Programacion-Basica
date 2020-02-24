# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:28:37 2020

@author: Estudiantes
"""

def recursuman(n):
    if n==1:
        return n
    return n+recursuman(n-1)
print(recursuman(int(input("ingrese un numero"))))