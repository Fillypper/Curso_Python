#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []
soma = 0
for c in range(0, 4):
    notas = float(input(f"Digite a {c + 1} nota: "))
    lista.append(notas)
    print(lista)

for nota in lista:
    soma += nota

media = soma / len(lista)

print(f"A média do aluno é {media:.2f}")