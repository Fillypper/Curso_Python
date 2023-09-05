#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []

for pessoa in range(0, 5):
    for ia in range(0, 1):
        idade = int(input(f"Digite a idade da {pessoa + 1}° pessoa: "))
        idades.append(idade)
        altura = float(input(f"Digite a altura da  {pessoa + 1}° pessoa: "))
        alturas.append(altura)

for idade in reversed(idades):
    print(idade, end=" ")
print()
for altura in reversed(alturas):
    print(f"{altura:.2f}", end=" ")



