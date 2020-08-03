# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

base = float(input("Digite a base do quadrado: "))
altura = float(input("Digite a altura do quadrado: "))

def area_quadrado(b, h):
  return b * h

print("O dobro da área do quadrado é", area_quadrado(base, altura) * 2)