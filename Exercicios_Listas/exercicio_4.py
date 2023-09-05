#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
lista = []
consoantes = []
cont = 0
for c in range(0, 10):
    letras = input("Digite uma letra: ")
    lista.append(letras)

    if letras not in 'aeiou':
        cont+=1
        consoantes.append(letras)
        print(consoantes)
        
print(f"A lista normal é {lista}")

print(f"Foram lidas {cont} consoantes, que são {consoantes}")
    