# 8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

ganha_hora = float(input("Quanto você ganha por hora? "))
horas_mes = int(input("Quantas horas você trabalha por mês? "))

salario = ganha_hora * horas_mes

print(f"O seu salário será de R${salario:.2f}")
