#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

from random import uniform
from time import sleep

meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []
temperaturas_elevadas =[]
soma, media = 0, 0
for c in range(0, 12):
    temperatura_mensal = uniform(20.0, 40.0)
    temperaturas.append(temperatura_mensal)
    soma+= temperatura_mensal
media = soma / len(temperaturas)
for c in range(0,12):
    if str(temperatura_mensal)[c] > str(media):
        temperaturas_elevadas.append(meses_ano[c])

print(f"Os meses do ano com temperaturas mais elevadas foram {temperaturas_elevadas}")


