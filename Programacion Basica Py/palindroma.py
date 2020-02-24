# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:05:36 2020

@author: Estudiantes
"""

a=input(" ingrese la cadena de caracteres")

b=a.replace(" ","")
count=len(b)
for x in range(len(b)):
    if b[x]==b[len(b)-x-1]:
        count=count-1
if count==0:
    print("la palabra ",a," es palindroma")
else:
    print("la palabra ",a," no es palindroma")
   