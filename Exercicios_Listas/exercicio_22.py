"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""
from random import randint

MAX_DEFEITOS = 4
defeitos = ["necessita da esfera", "necessita de limpeza", "necessita troca do cabo", "quebrado ou inutilizado "]
situacoes = [0] * MAX_DEFEITOS
total_situacoes = 0
#nummero indeterminado de entradas
defeitos_print = """
1- necessita da esfera 
2- necessita de limpeza 
3- necessita troca cabo
4- quebrado ou inutilizado
0- Sair"""
def percentual(total, unitario):
    percentual = (unitario / total) * 100
    return percentual

print(defeitos_print)

while True:
    relatorio_de_defeito = int(input("Digite a opção do defeito: "))
    if relatorio_de_defeito >= 1 and relatorio_de_defeito <= 4:
        situacoes[relatorio_de_defeito - 1] += 1
        total_situacoes += 1
    elif relatorio_de_defeito == 0:
        break
    else:
        print("Digite um numero de 1 a 4 ou 0 para sair")
print("Situação                        Quantidade              Percentual")
#ja é o terceiro exercicio que faço do mesmo jeito e tenho que voltar para olhar como fiz o for

#é sempre feito pela lista com o maximo de "votos" que se pode ter, e não pela lista de quantidade de votos

for c in range(MAX_DEFEITOS):
    print(f" {c + 1} - {defeitos[c]:<29} {situacoes[c]:<10} {percentual(total_situacoes, situacoes[c]):>15.1f}%")
