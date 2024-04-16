# 16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
# e o preço total.

tamanho = float(input("Qual tamanho em metros quadrados da área a ser pintada? "))

litros_por_lata = 18

preco_por_lata = 80.00

quantidade_de_latas = (tamanho / 3) * litros_por_lata

preco_total = quantidade_de_latas * preco_por_lata

print(f"A quantidade de latas será de {quantidade_de_latas} e o preço será R${preco_total:.2f}")
