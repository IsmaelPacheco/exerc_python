# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

def convert_temp(cel):
    far = (cel*1.8) + 32

    return far


graus_celsius = float(
    input("Digite o grau em Celsius: ").replace(",", "."))
graus_farenheit = convert_temp(graus_celsius)


print("{} ºC equivale a {} ºF.".format(graus_celsius, graus_farenheit))
