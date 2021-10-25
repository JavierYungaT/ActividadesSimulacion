# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importamos librerias
import numpy as np
from random import randint, uniform,random
from matplotlib import pyplot as plt


num_tiros=int(input("Ingrese el numero de veces: ")); #Número de veces a lanzar el dado
#Declaramos variables
dado1=np.zeros(num_tiros)
dado2=np.zeros(num_tiros)
suma_dados=np.zeros(num_tiros)

#Numero randómicos
for i in range (0,num_tiros):
    dado1[i]=randint(1, 6)
    dado2[i]=randint(1, 6)
    
#suma los dos arrays
suma_dados=dado1+dado2 

#frecuencia
frecNums=np.unique(suma_dados, return_counts=True)

#Imprimir numeros

print("Dado1      ",dado1)
print("Dado2      ",dado2)
print("Suma dados ",suma_dados)
print("Orden     ",frecNums[0])
print("Frecuencia ",frecNums[1])



plt.bar(frecNums[0],frecNums[1])