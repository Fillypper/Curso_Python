"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
from random import uniform

notas = float(input("Digite a nota: "))
todas_notas = []
todas_notas.append(notas)
soma, cont, cont2 = 0, 0, 0

while notas != -1:
    notas = float(input("Digite a nota: "))
    if notas != -1:
       todas_notas.append(notas)


print(f"Tivemos {len(todas_notas)} notas")

print("Valores um ao lado do outro: ")
for notas in todas_notas:
    print(notas, end=" ")
    soma += notas

print()
print("Valores na forma inversa e um abaixo do outro: ")
for notas in reversed(todas_notas):
    print(notas)

print(f"A soma dos valores é {soma}")

media = soma / len(todas_notas)
print(f"A média dos valores é {media:.2f}")


for notas in todas_notas:
    if notas > media:
        cont += 1
print(f"Tiveram {cont} notas acima da média {media:.2f}")
for notas in todas_notas:
    if notas < media:
        cont2 += 1
print(f"Tiveram {cont} notas abaixo da média {media:.2f}")
print("Programa encerrado")