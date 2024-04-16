# 11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

#   a. o produto do dobro do primeiro com metade do segundo .
#   b. a soma do triplo do primeiro com o terceiro.
#   c. o terceiro elevado ao cubo.

i1 = int(input("Primeiro número inteiro:"))
i2 = int(input("Segundo número inteiro:"))
r = float(input("Número real:"))

a = (i1 * 2) * (i2 / 2)
b = (i1 * 3) + r
c = r ** 3

print(f"""
O produto do dobro do primeiro com metade do segundo é {a:.2f}
A soma do triplo do primeiro com o terceiro é {b:.2f}
O terceiro elevado ao cubo é {c:.2f}

""")