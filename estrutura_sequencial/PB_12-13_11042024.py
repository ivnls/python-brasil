# 12.Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte 
# fórmula: (72.7*altura) - 58 

# 13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# 
#     Para homens: (72.7*h) - 58
#     Para mulheres: (62.1*h) - 44.7 

sexo = input("Qual o seu sexo? (M) (F): ")

if sexo == "M":
    altura = float(input("Digite a sua altura em Metros(M): "))
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    altura = float(input("Digite a sua altura em Metros(M): "))
    peso_ideal = (62.1* altura) - 44.7
else:
    print("Esta opção não está disponível!")
    exit()

print(f"O seu peso ideal é {peso_ideal:.1f}Kg")
