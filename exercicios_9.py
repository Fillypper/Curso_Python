#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

A = []
exp = []
quadrado_soma = 0
for c in range(0, 10):
    numeros = int(input(f"Digite o {c + 1}° numero: "))
    A.append(numeros)

for numeros in A:
    quadrado_soma += numeros ** 2

print(f"A soma total dos quadrados dos elementos é: {quadrado_soma}")


