# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:19:41 2020

@author: Administrador
"""

archivo = open("ascci.txt", "w")
for i in range(257):
    archivo.write(str(i)+str(" ")+chr(i)+str("\n"))
archivo.close()