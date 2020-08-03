# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

def convert_temp(far):
    celsius = 5 * ((far-32) / 9)

    return celsius


graus_farenheit = float(
    input("Digite o grau em Farenheit: ").replace(",", "."))
graus_celsius = convert_temp(graus_farenheit)


print("{} ºF equivale a {} ºC.".format(graus_farenheit, graus_celsius))
