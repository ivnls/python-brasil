#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
#total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
#para o sindicato, faça um programa que nos dê:

#    salário bruto.
#    quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#    o salário líquido.
#    calcule os descontos e o salário líquido, conforme a tabela abaixo:

#    + Salário Bruto : R$
#    - IR (11%) : R$
#    - INSS (8%) : R$
#    - Sindicato ( 5%) : R$
#    = Salário Liquido : R$

imposto_renda = 11
inss = 8
sindicato = 5

ganha_hora = float(input("Quanto você ganha por hora? "))
horas_mes = int(input("Quantas horas você trabalha por mês? "))

salario_bruto = ganha_hora * horas_mes

imposto_descontado = (salario_bruto * (imposto_renda + inss + sindicato)) / 100

salario_liquido = salario_bruto - imposto_descontado

print(f"O salário bruto será de R${salario_bruto:.2f}.")
print(f"O salário líquido será de R${salario_liquido:.2f}.")