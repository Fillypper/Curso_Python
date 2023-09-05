#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros_lista = []
soma = 0
multiplicacao = 1

for numero in range(0, 5):
    numeros = int(input(f"Digite o {numero + 1}° numero: "))
    numeros_lista.append(numeros)
    soma += numeros
    multiplicacao *= numeros
print(f"Os numeros são {numeros_lista}")
print(f"Soma dos numero é {soma}")
print(f"Multiplicação dos números é {multiplicacao}")
