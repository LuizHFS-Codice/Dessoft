#Jogo
#Funções para rodar o jogo-----------
from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import posicao_valida
import random
#------------------------------------
#Condições Iniciais------------------
tamanhos=[4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
Embarcacoes=['submarino','contratorpedeiro','navio-tanque','porta-aviões'] #Lista de Embarcações
Pos=0
Lin=0
Col=0
Ori=0
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
    }
ListNavios=[]
#-----------------------------------
#loop de for para cada tamanho
for tamanho in tamanhos:
    if tamanho==4:
        Embarc=Embarcacoes[3] #Porta Avião
    elif tamanho==3:
        Embarc=Embarcacoes[2] #Navio Tanque
    elif tamanho==2:
        Embarc=Embarcacoes[1] #Contra Torpedeiro
    elif tamanho==1:
        Embarc=Embarcacoes[0] #Submarino
#Posição X,Y
#---------------------------------------------------------------------------------------------------------
    ListNavios=[]
    print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')
    Lin=int(input("Linha escolhida> "))
    Col=int(input("Coluna Escolhida> "))
#Orientação
#---------------------------------------------------------------------------------------------------------
    if tamanho>1:
        Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
        if Ori==1:
            Ori='vertical'
        else:
            Ori='horizontal'
    else:
        Ori='vertical' #lembrar que o sub é sempre vertical 
#     Check1=posicao_valida(frota,Lin,Col,Ori,tamanho)
# #Checagem
# #----------------------------------------------------------------------------------------------------------
#     if Check1 == False: 
#         while Check1 != True: #Caso não seja uma posição valida
    while not posicao_valida(frota,Lin,Col,Ori,tamanho): # tentar simplificar a verificacao se essa posicao é válida
             
            print('Esta posição não está válida!')
            print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')
            Lin=int(input("Linha escolhida> "))
            Col=int(input("Coluna Escolhida> "))
            if tamanho>1:
                Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
                if Ori==1:
                    Ori='vertical'
                else:
                    Ori='horizontal'
            else:
                Ori='vertical'
    #         Check1=posicao_valida(frota,Lin,Col,Ori,tamanho)
    # else:
    #     Pos=define_posicoes(Lin,Col,Ori,tamanho) #Posição da Embarcação
    #     ListNavios.append(Pos)
    #     frota[Embarc]+=ListNavios #Colocando a posição da embarcação dentro da Frota

    # add depois da vericação a posição válida á frota 

    Pos = define_posicoes(Lin, Col, Ori, tamanho)
    frota[Embarc].append(Pos)
#-----------------------------------------------------------------------------------------------------------
# print(frota)
#-----------------------------------------------------------------------------------------------------------

# sugestão de melhora pra simplificar de forma que ao invés de ter um bloco só 
# pro submarino, usar um if dentro do bloco que já temos para determinar a orientacao

# Tentativa 1:

# def obter_input_valido(Embarc, tamnho):
#     while True:

#         print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')

#         Lin = int(input("Linha escolhida>"))
#         Col = int(input('Coluna Escolhida>'))

#         # automaticamnte saber a orientacao para o submarino

#         if tamnho == 1:
#             Ori = "vertical"

#         else:

#             Ori = int(input('Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> '))
#             Ori = "vertical" if Ori == 1 else "horizontal"

#         if posicao_valida(frota, Lin, Col, Ori, tamnho):
#             return Lin, Col, Ori
        
#         else:

#             print("Esta posição não está válida!")
#----------------------------------------------------------------------------------------------------
#Frota do Jogador
Jogador=posiciona_frota(frota)
#----------------------------------------------------------------------------------------------------
#Frota Oponente
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
Oponente=posiciona_frota(frota_oponente)
#-------------------------------------------------------------------------------------------------------
#Loop de jogo
jogando=True
jogadax=0
jogaday=0
jogadas=[]
listajogadas=[]
jogadasoponente=[]
casualidades=0
baixas=0
while jogando:
    
    #---------------------------------------------------------------------------------------------------
    #Função de mostrar os dois tabuleiros juntos, fornecido pelo PrairieLearn
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
    print(monta_tabuleiros(Jogador,Oponente))
    #-----------------------------------------------------------------------------------------------------
    #jogadas eixo x
    jogadax=int(input('Jogador, qual linha deseja atacar? '))
    while jogadax not in range(0,10):
        print('Linha inválida!')
        jogadax=int(input('Jogador, qual linha deseja atacar? '))
    #jogadas eixo y
    jogaday=int(input('Jogador, qual coluna deseja atacar? '))
    while jogaday not in range(0,10):
        print('Coluna inválida!')
        jogaday=int(input('Jogador, qual coluna deseja atacar? '))
    #------------------------------------------------------------------------------------------------------
    #Check para jogadas repetidas
    jogadas=[jogadax,jogaday]
    while jogadas in listajogadas:
        print(f'A posição linha {jogadax} e coluna {jogaday} já foi informada anteriormente!')
    #Repetição da jogada do eixo x
        jogadax=int(input('Jogador, qual linha deseja atacar? '))
        while jogadax not in range(0,10):
            print('Linha inválida!')
            jogadax=int(input('Jogador, qual linha deseja atacar? '))
    #Repetição da jogadas eixo y
        jogaday=int(input('Jogador, qual coluna deseja atacar? '))
        while jogaday not in range(0,10):
            print('Coluna inválida!')
            jogaday=int(input('Jogador, qual coluna deseja atacar? '))
        jogadas=[jogadax,jogaday]
    listajogadas.append(jogadas)
    #-------------------------------------------------------------------------------------------------------
    #Efeito no tabuleiro oponente
    Oponente=faz_jogada(Oponente,jogadas[0],jogadas[1])
    #-------------------------------------------------------------------------------------------------------
    #Check para finalizar o jogo
    casualidades=afundados(frota_oponente,Oponente)
    if casualidades==10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando=False
    #--------------------------------------------------------------------------------------------------------
    #Jogadas do oponente
    else:
        jogadax=random.randint(0,9)
        jogaday=random.randint(0,9)
        jogadas=[jogadax,jogaday]
        while jogadas in jogadasoponente:
            jogadax=random.randint(0,9)
            jogaday=random.randint(0,9)
            jogadas=[jogadax,jogaday]
        jogadasoponente.append(jogadas)
    #---------------------------------------------------------------------------------------------------------
    #Consequencias da jogada do oponente
        print(f'Seu oponente está atacando na linha {jogadas[0]} e coluna {jogadas[1]}')
        Jogador=faz_jogada(Jogador,jogadas[0],jogadas[1])
        baixas=afundados(frota,Jogador)
        if baixas==10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando=False