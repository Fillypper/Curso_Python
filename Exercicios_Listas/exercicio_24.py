"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados."""

#importei a biblioteca random para pegar numeros aleatórios
from random import randint

#fiz o maximo de numeros que teria na lista
MAX_NUMEROS = 6

#declarei a lista com 6 posições com o valor 0
contador = [0] * 6

#fiz a função gerar numeros aleatórios
def numero_aleatorio():
    numero_aleatorio = randint(1, 6)
    return numero_aleatorio

#for com repetição de 100 vezes como solicitado
for c in range(100):
    #declarei uma variavel que recebe a função de numeros aleatório
    numeros = numero_aleatorio()
    #peguei a lista na posição numero aleatório - 1  e adicionei +1 para cada vez que ele for contado
    contador[numeros - 1] += 1

#finalizando com print de enumerate na lista para descobrir quantas vezes cada numero de 1 - 6 foram contados
for c, v in enumerate(contador):
    print(f"O número {c +1} foi contado {v} vezes")

