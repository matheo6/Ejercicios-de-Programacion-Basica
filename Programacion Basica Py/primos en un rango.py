# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:41:45 2020

@author: Estudiantes
"""

lista=[]
a=int(input("ingrese el rango"))
for i in range(a):
    c=0
    for x in range(1,i):
        if i%x==0:
            c=c+1
    if c<2:
            lista.append(i)
print(lista)
