# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:21:00 2020

@author: Estudiantes
"""
def factorial (a):
    b=1
    for i in range(1,a+1):
       b=b*i
    print("el factorial de ",a," es : ",b)
numerop=factorial(int(input("ingrese el numero ")))
