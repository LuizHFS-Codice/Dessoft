def define_posicoes(Lin,Col,Ori,Tam):
    lf=[]
    Cont=0
    Lis_Pos=0
    #
    if Ori=='horizontal':
        for i in range(Tam):
            Cont=Col+i
            Lis_Pos=[Lin,Cont]
            lf.append(Lis_Pos)
        Cont=0
        #######################
    else:
        Lis_Cont=range(Lin,Tam+1)
        for i in range(Tam):
            Cont=Lin+i
            Lis_Pos=[Cont,Col]
            lf.append(Lis_Pos)
        ###
    return lf

linha = 2
coluna = 4
orientacao = "vertical"
tamanho = 3

print(define_posicoes(linha, coluna, orientacao, tamanho))