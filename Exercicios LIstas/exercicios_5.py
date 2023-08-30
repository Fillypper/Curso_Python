#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
import random
lista = []
pares = []
impares = []



for v in range(0, 20):
    numeros = random.randint(0, 20) #Sei que é para o aprendizado porém, não queria perder tempo digitando 20 numeros então usei a biblioteca random pra me auxiliar
    lista.append(numeros)
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
print(f"Lista total: {lista}")

print(f"Lista de pares {pares}")

print(f"Lista de impares {impares}")