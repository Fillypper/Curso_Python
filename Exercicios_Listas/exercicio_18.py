"""Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
    """

#Criamos a função de calculos de porcentagem, que utilizaremos 2 variaveis para fazela funcionar que serão os (votos daquele jogador / total de votos) * 100
def calcular_percentual(votos, total_votos):
    return (votos / total_votos) * 100

#Aqui declaramos a variavel MAX_JOGADORES = 23 (em maiusculo pois não mexeremos nessa varivel) e com numero 23 pois é o maximo de numeros nas camisas que teremos
MAX_JOGADORES = 23

#aqui criamos a lista votos e de inicio alocamos 23 espaços de 0 nela fazendo lista = [conteudo] * 23 (MAX_JOGADORES)
votos = [0] * MAX_JOGADORES

#Variavel para fazer a som da quantidade de votos
total_votos = 0


#Loop infinito esperando a declaração de break
while True:
    #variavel votos_jogador para receber os votos
    votos_jogador = int(input("Número do jogador (0=fim): "))
    #fazemos nosso primeiro if para verificar se votos_jogador estão entre 1 e 23
    if votos_jogador >= 1 and votos_jogador <= MAX_JOGADORES:
        #Aqui é bem interessante, pois pegamos a lista votos na posição votos_jogador - 1 ou seja, como a lista vai de 0 a 22 e temos uma votaçao de 1 a 23
        #diminuimos 1 da camisa do jogador e adiciomos +1 voto ao respectiva posição do numero na lista Ex. Camisa 1, posição 0, Camisa 23, posição 22
        votos[votos_jogador - 1] +=1
        #aqui nós colocamos +1 ao total de votos, cada vez que essa condição é verdadeira
        total_votos += 1
        #como pedido no enunciado, caso for digitado 0 no votos_jogador o programa chama o break para sair do loop infinito
    elif votos_jogador == 0:
        break
    else:
        #Caso as codições acima não forem satisfeitas(verdadeiras) será printado a mensagem a baixo e continuaremos no loop inifito
        print("Informe um valor entre 1 e 23 ou 0 para sair!")

print("Resultado da votação:\n\n")
#aqui printamos a quantidade total de votos
print(f"Foram computados {total_votos} votos.\n")
print("Jogador     Votos       %\n")

#Aqui fazemos loop de repetição for para a variavel MAX_JOGADORES
for i in range(MAX_JOGADORES):
    #e então printamos as informações abaixo, caso na lista votos nas posição [i] obtivermos numeros maiores que zero, pois 0 seria nenhum voto.
    if votos[i] > 0:
        #Aqui printamos primeiramente o numero da camisa do jogador, porém se deixarmos apenas pela posição [i] será retornado a posição da lista que é diferente da camisa dos jogadores, portanto colocaremos [i + 1] pois retornará as camisas dos jogadores 1 a 23 ao inves de 0 a 22, como nosso print é uma f string, formatei ela com :5 pois quero que a resposta ocupe 5 casas e mantenha distancia das proximas respostas
        #Printamos os votos por puxarmos a lista[i] que seria votos[0], votos[1].... e formatamos com 10 casas
        #Printamos também a nossa função de percentual com os valores prescritos lá em cima e formatando as com :10 casa, .1f uma casa após o ponto flutuante e colocando %
        print(f"{i+1:5} {votos[i]:10} {calcular_percentual(votos[i], total_votos):10.1f} %")
            