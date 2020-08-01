# Faça um Programa que peça as 4 notas bimestrais e mostre a média

nota_1 = int(input("Digite a nota 01:"))
nota_2 = int(input("Digite a nota 02:"))
nota_3 = int(input("Digite a nota 03:"))
nota_4 = int(input("Digite a nota 04:"))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print("A média das notas foi {}.".format(media))