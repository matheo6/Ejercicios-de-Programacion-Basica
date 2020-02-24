# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:15:43 2020

@author: Estudiantes
"""

a=int(input("ingrese el numero"))
b=int(input("ingrese el segundo numero"))
if a>b:
   c=b
   b=a
   a=c
print("el primer numero",a,"el segundo numero",b)