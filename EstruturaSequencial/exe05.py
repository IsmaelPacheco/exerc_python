# Faça um Programa que converta metros para centímetros.

valor_metros = float(
    input("Digite o valor em metros à converter:")
    .replace(",", "."))

valor_centimetro = valor_metros * 100
add_plural = ""

if valor_metros > 0:
    if valor_metros > 1:
        add_plural = "s"

    print("{} metro{} equivale a {} centímetros."
          .format(valor_metros, add_plural, valor_centimetro))

elif valor_metros < 0:
    print("Número inválido!")
