"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""
from random import randint

MAX_OS = 6 
sistema_operacional = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * MAX_OS
total_votos = 0

def percentual(votos, total_votos):
    percentual = (votos / total_votos) * 100
    return percentual
opcoes = """OPÇÕES:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
0- Sair"""
print(opcoes)

while True:
    os_escolhido = int(input("Qual OS deseja votar: "))
    if os_escolhido >= 1 and os_escolhido <= 6:
        quantidade_votos = int(input("Quantos votos esse OS obteve: "))
        votos[os_escolhido - 1] += quantidade_votos
        total_votos += quantidade_votos
    elif os_escolhido == 0:
        break
    else:
        print("Digite um numero de 1a 6 ou 0 para sair")
print("Sistema Operacional     Votos      %")
print("-------------------     -----     ---")
for i in range(MAX_OS):
    if votos[i] > 0:
        print(f"{sistema_operacional[i]:22} {votos[i]:5} {percentual(votos[i], total_votos):10.0f}%\n")
print("-------------------     -----")
print(f"Total                   {total_votos:10}\n\n")
print(f"O Sistema Operacional mais votado foi o {sistema_operacional[votos.index(max(votos))]}, com {max(votos)} votos, correspondendo a {percentual(max(votos), total_votos):.0f}% dos votos.")

