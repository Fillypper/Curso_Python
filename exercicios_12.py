#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


from random import randint, uniform

idades = []
alturas = []
soma, cont, media = 0, 0, 0
for ia in range(0, 30):
    idade = randint(10, 20)
    altura = uniform(1.4, 2.0)
    idades.append(idade)
    alturas.append(altura)

for altura in alturas:
    soma += altura
    media = soma / len(alturas)

for c in range(0,30):
    if idades[c] >= 13 and alturas[c] < media:
        cont += 1

print(f"Tiveram {cont} pessoas com 13 anos ou mais e menor que a altura média de {media:.2f}")

