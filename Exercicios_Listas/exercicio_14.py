"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
alternativa = []

telefonou = input("Telefonou para a vítima?: ")
alternativa.append(telefonou)

local = input("Esteve no local do crime?: ")
alternativa.append(local)

mora = input("Mora perto da vítima?: ")
alternativa.append(mora)

devia = input("Devia para a vítima?: ")
alternativa.append(devia)

trabalhou = input("Já trabalhou com a vítima?")
alternativa.append(trabalhou
                   )
if alternativa.count('sim') == 5:
    print("Assassino")
elif alternativa.count('sim') == 3 or alternativa.count('sim') == 4:
    print('Cúmplice')
elif alternativa.count('sim') == 2:
    print("Suspeita")
else:
    print("Inocente")
    