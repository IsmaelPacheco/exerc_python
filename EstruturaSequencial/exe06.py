# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Digite o raio do círculo: "))

def calcula_area (num):
  res = math.pi * (num*num)
  return res

print(calcula_area(raio))