# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_por_hora = float(
    input("Digite o valor ganho por hora: ").replace(",", "."))
horas_trabalhadas = float(
    input("Digite quantas horas trabalhadas: ").replace(",", "."))

salario = valor_por_hora * horas_trabalhadas

print("\nFoi trabalhado {} horas. \nSendo R${} por hora.\nO salário ganho neste mês foi de R$ {}."
      .format(horas_trabalhadas, valor_por_hora, salario))
