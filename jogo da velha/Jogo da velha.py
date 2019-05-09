#Jogo da Velha(Luis Eduardo Bet and Emily)


import sys #Biblioteca Python utilizada para a finalização do programa
x_o = "X"
jorge = 2 #Variável utilizada na marcação das casase na alternancia das jogadas 
c1 = ('1')#
c2 = ('2')#
c3 = ('3')#
c4 = ('4')#
c5 = ('5')# Variáveis que iram armazenar os números das casas
c6 = ('6')# e altera-los futuramente através das jogadas dos users
c7 = ('7')#
c8 = ('8')#
c9 = ('9')#
#Função que define o formato e as casa do Tabuleiro
def tabuleiro():
    print(c1 ,"  |  ", c2  ,"  |  ", c3)
    print(c4 ,"  |  ", c5  ,"  |  ", c6)
    print(c7 ,"  |  ", c8  ,"  |  ", c9)
    
#Menu de Início 
menu=input("Você deseja Continuar [C] ou Sair[S]? ").upper()
if menu=='S':
    sys.exit()
elif menu== "C":
     pass
while menu!="C" and menu!="S":
    menu=input("Valor Inválido...Por favor digite umas das letras dentro do colchetes!!").upper()
    if menu=='S':
        sys.exit()
    elif menu== "C":
        pass
            
#Loop que vai definir se é a jogada de [X] ou [O]
tabuleiro()
while True:
    if jorge % 2 == 0: x_o ='X'
    else: x_o = 'O'

    print("Agora é a vez de",x_o) 
    jogada = str(input())
#Verifica se o número digitado pelo usuário é válido
    while jogada.isnumeric() == False:
        jogada= str(input("Por favor coloque um número válido:"))
    while int(jogada)>=10 or int(jogada) <= 0:
        jogada= int(input("Por favor coloque um número válido:"))
    jogada = int(jogada)
#Estrutura de decisão que define qual casa será preenchida com [X] ou [O],
#onde também verifica se a casa ja esta preenchida(fazendo o jogador perder a vez) ou vazia
    if jorge % 2 == 0: x_o ='X'

    else:x_o= "O"
    
    if jogada == 1 and c1 == '1' :
        c1= x_o

    elif jogada == 2 and c2== '2':
        c2 = x_o
    

    elif jogada == 3 and c3== '3' :
        c3 = x_o
   

    elif jogada == 4  and c4== '4':
        c4 = x_o
    

    elif jogada == 5 and c5=='5':
        c5 = x_o
 

    elif jogada == 6 and c6=='6':
        c6 = x_o


    elif jogada == 7 and c7=='7':
        c7 = x_o

    elif jogada == 8 and c8=='8':
        c8 = x_o
    
    elif jogada == 9 and c9=='9':
        c9 = x_o
    

    jorge = (jorge + 1)#Variável jorge possui uma soma, o que possibilita a alternancia de jogadas entre [X] e [O]
    tabuleiro()
    
    #Estrutura de decisão que permite o analisar e printar quem foi ou Vencedor ou se deu Velha
    if c1 == 'X' and c2 == 'X' and c3 == 'X':
        print ('O Jogador [X] VENCEU!!')
        break
    elif c4 == 'X' and c5 == 'X' and c6 == 'X':
        print ('O Jogador [X] VENCEU!!')
        break
    elif c7 == 'X' and c8 == 'X' and c9 == 'X':
        print ('O Jogador [X] VENCEU!!')
        break
    elif c1 == 'X' and c4 == 'X' and c7 == 'X':
        print ('O Jogador [X] VENCEU!!')
        break
    elif c2 == 'X' and c5 == 'X' and c8 == 'X':
        print ('O Jogador [X] VENCEU!!')
        break
    elif c3 == 'X' and c6 == 'X' and c9 == 'X':
        print ('O Jogador [X] VENCEU')
        break
    elif c1 == 'X' and c5 == 'X' and c9 == 'X':
        print ('O Jogador [X] VENCEU!!')
        break
    elif  c3 == 'X' and c5 == 'X' and c7 == 'X':
        print ('O Jogador [X] VENCEU!!')
        break
    elif c1 == 'O' and c2 == 'O' and c3 == 'O':
        print ('O Jogador [O]  VENCEU!!')
        break
    elif c4 == 'O' and c5 == 'O' and c6 == 'O':
        print ('O Jogador [O]  VENCEU!!')
        break
    elif c7 == 'O' and c8 == 'O' and c9 == 'O':
        print ('O Jogador [O]  VENCEU!!')
        break
    elif c1 == 'O' and c4 == 'O' and c7 == 'O':
        print ('O Jogador [O]  VENCEU!!')
        break
    elif  c2 == 'O' and c5 == 'O' and c8 == 'O':
        print ('O Jogador [O]  VENCEU!!')
        break
    elif  c3 == 'O' and c5 == 'O' and c9 == 'O':
        print ('O Jogador [O]  VENCEU!!')
        break
    elif c1 == 'O' and c5 == 'O' and c9 == 'O':
        print ('O Jogador [O]  VENCEU!!')
        break
    elif c3 == 'O' and c5 == 'O' and c7 == 'O':
        print ('O Jogador [O]  VENCEU!!')
        break
    elif jorge == 9:
        print('DEU VELHA!!')
        break
#Input colocado para que os usuários consigam visualizar as mensagens de Vencer/Deu Velha no Prompt de Comando
a= input("Digite qualquer coisa para sair:")
            
            


   

















