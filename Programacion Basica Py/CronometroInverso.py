# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:57:18 2020

@author: Administrador
"""


import time

timeH=int(input("ingrese las horas "))
timeM=int(input("ingrese los minutos "))
timeS=int(input("ingrese los segundos "))
horas=timeH
minutos=timeM
segundos=timeS

if timeM>0:
    for s in range(timeS):
                print(str(horas)+" horas "+str(minutos)+" minutos "+str(segundos)+" segundos ")
                segundos=segundos-1
                time.sleep(1)
if timeM>0:
    minutos=minutos-1
    segundos=59
    for m in range(timeM):
            for s in range(60):
                print(str(horas)+" horas "+str(minutos)+" minutos "+str(segundos)+" segundos ")
                segundos=segundos-1
                time.sleep(1)
            segundos=60
            minutos=minutos-1
                
if timeH>0:
    segundos=59
    minutos=59
    horas=horas-1
    for h in range(timeH):
        for m in range(60):
            for s in range(60):
                print(str(horas)+" horas "+str(minutos)+" minutos "+str(segundos)+" segundos ")
                segundos=segundos-1
                time.sleep(1)
            segundos=60
            minutos=minutos-1
        minutos=59    
        horas=horas-1

            
