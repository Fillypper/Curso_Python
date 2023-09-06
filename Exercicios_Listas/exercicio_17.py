"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
    """



saltos = []

soma = 0
nome  = input("Digite o nome do atleta: ")
for c in range(0, 5):
    if c == 0:
        salto = float(input("Digite o primeiro salto: "))
        saltos.append(salto)
    elif c == 1:
        salto = float(input("Digite o segundo salto: "))
        saltos.append(salto)
    elif c == 2:
        salto = float(input("Digite o terceiro salto: "))
        saltos.append(salto)
    elif c == 3:
        salto = float(input("Digite o quarto salto: "))
        saltos.append(salto)
    elif c == 4:
        salto = float(input("Digite o quinto salto: "))
        saltos.append(salto)
    soma += salto
media = soma / 5
print()
print(f"Primeiro Salto: {saltos[0]:.2f} m\n"
        f"Segundo Salto: {saltos[1]:.2f} m\n"
        f"Terceiro Salto: {saltos[2]:.2f} m\n"
        f"Quarto Salto: {saltos[3]:.2f} m\n"
        f"Quinto Salto: {saltos[4]:.2f} m\n")
print()

print("Resultado final:"
f"Atleta: {nome}\n"
f"Saltos: {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]}\n"
f"Média dos saltos: {media} m\n")


