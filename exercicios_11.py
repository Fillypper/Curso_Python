#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

from random import randint
from time import sleep

A = []
B = []
C = []
ABC = []


for c in range(0, 10):
    numeros_A = randint(0, 20)
    A.append(numeros_A)

for c in range(0, 10):
    numeros_B = randint(0, 20)
    B.append(numeros_B)

for c in range(0, 10):
    numeros_C = randint(0, 20)
    C.append(numeros_C)

for c in range(0, 10):
    ABC.append(A[c])
    ABC.append(B[c])
    ABC.append(C[c])



print(f"Numeros da lista A: {A}\n")
print(f"Numeros da lista B: {B}\n")
print(f"Numeros da lista C: {C}\n")
print(f"Numeros da junção das listas: {ABC}")