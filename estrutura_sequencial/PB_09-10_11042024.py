# 09.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

#    C = 5 * ((F-32) / 9).

# 10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print("""
1.Converter Celcius(ºC) para Fahrenheith(ºF).
2.Converter Fahrenheit(ºF) para Celsius(ºC).
""")
opcao = int(input("Qual a alternativa?"))


match opcao:
    case 1:
        c = float(input("Qual a temperatura em Celsius(ºC)?"))

        f = c * ((9 / 5) + 32)

        print(f"A temperatura convertida é {f:.1f}")
    case 2:
        f = float(input("Qual a temperatura Fahrenheit(ºF)?"))

        c = 5 * ((f - 32) / 9)

        print(f"A temperatura convertida é {c:.1f}ºC")
    case other:
        print("Esta opção não está disponível!")