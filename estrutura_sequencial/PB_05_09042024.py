# 5. Faça um Programa que converta metros para centímetros.

escolha = input("""
1. Converter de Metros(m) para Centímetros(cm)
2. Converter de Centímetros(cm) para Metros(m)\n
Escolha uma opção: """)

match escolha:
    case 1:

        metro = float(input("Digite a medição em Metros(M): "))

        resultado = metro * 1000

        print(f"A conversão resultou em {resultado:.2f}cm")


