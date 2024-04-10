# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

for numero in range(1,5):
    nota = float(input(f"{numero}º nota: "))
    notas.append(nota)

resultado = (notas[0] + notas[1] + notas[2] + notas[3]) / 4

print(f"A média do aluno é {resultado:.1f}")