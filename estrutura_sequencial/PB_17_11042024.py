# 17.Faça um Programa para uma loja de tintas. O programa deverá pedir
# o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
# que custam R$ 25,00.
# 
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanho = float(input("Qual tamanho em metros quadrados da área a ser pintada? "))

litros_por_lata = 18
litros_por_galao = 3.6

preco_por_lata = 80.00
preco_por_galao = 25.00

quantidade_de_latas = (tamanho / 6) * litros_por_lata
quantidade_de_galoes = (tamanho / 6) * litros_por_galao 

preco_total_lata = quantidade_de_latas * preco_por_lata
preco_total_galao = quantidade_de_galoes * preco_por_galao

print(f"""A quantidade de latas será de {quantidade_de_latas} e o preço será R${preco_total_lata:.2f} ou
você pode optar por {quantidade_de_galoes} de {litros_por_galao}L por R${preco_por_galao:.2f}""")