#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = []
medias = []
soma = 0
contador = 0
for alunos in range(0, 10):
    print(f"Notas do {alunos + 1}° aluno")
    soma = 0
    for nota in range(0, 4):
        notas_alunos = float(input(f"Digite a {nota + 1}° nota do aluno: "))
        soma += notas_alunos
    media = soma / 4
    medias.append(media)
    if media >= 7.0:
        contador += 1
    print(contador)
    print(notas)
    print(medias)
    print(soma)
    print(media)

print(f"Tiveram {contador} alunos com média maior ou igual a 7.0")


