#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

from random import randint
from time import sleep

A = []
B = []
AB = []


for c in range(0, 10):
    numeros_A = randint(0, 20)
    A.append(numeros_A)

for c in range(0, 10):
    numeros_B = randint(0, 20)
    B.append(numeros_B)

for c in range(0, 10):
    AB.append(A[c])
    AB.append(B[c])


print(f"Numeros da lista A: {A}\n")
print(f"Numeros da lista B: {B}\n")
print(f"Numeros da junção das listas: {AB}")