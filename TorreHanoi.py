
import Interface
from Interface import *

#------------------

def Variaveis(torre1, torre2, torre3, jogadas):
    return torre1, torre2, torre3, jogadas

#-------------------Resolução Recursiva
def resolucaoRecursiva(totalDiscos, fromPole, toPole, withPole, torre1, torre2, torre3, jogadas):
    if totalDiscos >= 1:
        resolucaoRecursiva(totalDiscos-1,fromPole,withPole,toPole, torre1, torre2, torre3, jogadas)
        trocaDeTorre(fromPole, toPole, torre1, torre2, torre3, jogadas)
        resolucaoRecursiva(totalDiscos-1,withPole,toPole,fromPole, torre1, torre2, torre3, jogadas)

#------------------- Lista de jogadas
def ListaJogadas(jogadas,torreSaida,torreEscolha ):
    jogadas.append([torreSaida, torreEscolha])

#-------------------Voltar Jogadas
def VoltarJogadas(jogadas, torre1, torre2, torre3):
    ultima = int(len(jogadas) - 1)
    torreEscolha = int(jogadas[ultima][0])
    torreSaida = int(jogadas[ultima][1]) 
    trocaDeTorre(torreSaida, torreEscolha, torre1, torre2, torre3, jogadas)
    jogadas.pop()


#-------------------Verifica se ganhou o jogo
def WinTeste(torre0,torre2,torre3):
    if (torre2 == torre0) or (torre3 == torre0):
        return True
    else:
        return False

#------------------Compara discos
def comparaDisco(torreSaida, torreEscolha, torre1, torre2, torre3):
    certo = False
    if torreSaida == 1:
        if torreEscolha == 2:
            discoSaida = len(torre1)
            discoEscolha = len(torre2)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre1[discoSaida-1] > torre2[discoEscolha-1]:
                certo = True
        elif torreEscolha == 3:
            discoSaida = len(torre1) - 1
            discoEscolha = len(torre3)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre1[discoSaida-1] > torre3[discoEscolha-1]:
                certo = True
            
    
    elif torreSaida == 2:
        if torreEscolha == 1:
            discoSaida = len(torre2) - 1
            discoEscolha = len(torre1)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre2[discoSaida-1] > torre1[discoEscolha-1]:
                certo = True

        elif torreEscolha == 3:
            discoSaida = len(torre2) - 1
            discoEscolha = len(torre3)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre2[discoSaida-1] > torre3[discoEscolha-1]:
                certo = True
 
    elif torreSaida == 3:
        if torreEscolha == 1:
            discoSaida = len(torre3) - 1
            discoEscolha = len(torre1)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre3[discoSaida-1] > torre1[discoEscolha-1]:
                certo = True

        elif torreEscolha == 2:
            discoSaida = len(torre3) - 1
            discoEscolha = len(torre2)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre3[discoSaida-1] > torre2[discoEscolha-1]:
                certo = True
                          
    return certo

#-------------------Realiza a troca do disco nas torres
def trocaDeTorre(torreSaida, torreEscolha, torre1, torre2, torre3, jogadas):
    novoDisco = 0
    altura = 0
    if torreSaida == 1:
        if torreEscolha == 2:
            altura = len(torre2)
            novoDisco = retirarTorre(torre1)
            acrescentarTorre(torre2,novoDisco)
        elif torreEscolha == 3:
            altura = len(torre3)
            novoDisco = retirarTorre(torre1)
            acrescentarTorre(torre3,novoDisco)

    elif torreSaida == 2:
        if torreEscolha == 1:
            altura = len(torre1)
            novoDisco = retirarTorre(torre2)
            acrescentarTorre(torre1,novoDisco)
        elif torreEscolha == 3:
            altura = len(torre3)
            novoDisco = retirarTorre(torre2)
            acrescentarTorre(torre3,novoDisco)
  
    elif torreSaida == 3:
        if torreEscolha == 1:
            altura = len(torre1)
            novoDisco = retirarTorre(torre3)
            acrescentarTorre(torre1,novoDisco)
        elif torreEscolha == 2:
            altura = len(torre2)
            novoDisco = retirarTorre(torre3)
            acrescentarTorre(torre2,novoDisco)

    Interface.UIMoverDisco(novoDisco, torreEscolha, altura)
    

#------------------Implementação da Pilha
def acrescentarTorre(torre, disco):
    #Adiciona no topo da pilha/torre
    torre.append(disco)

def retirarTorre(torre):
    total = len(torre) - 1
    disco = torre[total]

    #Retira o topo
    torre.pop()

    #retorna o valor do topo
    return disco


#Inicialização das torres
def inicializaçãoTorres():
    torre0 = []
    torre1 = []
    torre2 = []
    torre3 = []
    jogadas = []
    return(torre0,torre1,torre2,torre3,jogadas)

#------------------Função Principal
def main():
    
    #Pergunta a quantidade de discos
    '''
    #Inicialização das torres
    torre0 = []
    torre1 = []
    torre2 = []
    torre3 = []
    jogadas = []
    i = 1
    Interface.UIInicializarDiscos(totalDiscos)


    #Acrescenta todos os discos na torre 1
    while i <= totalDiscos:
        acrescentarTorre(torre1,i)
        acrescentarTorre(torre0,i)
        i += 1

    totalDiscos = len(torre1)

    print("total discos: ", totalDiscos)
    print(torre1)
    print(torre2)
    print(torre3)
    
    saiu = False
    while not saiu:
        aux = 0
        torreEscolha = torreSaida = 0
        #Verifica de qual torre vai sair o disco e para qual vai. Já previne erros de escolher
        #uma torre que não existe e escolher duas torres iguais
        while aux == 0 and not (torreSaida < 4 and torreSaida > 0 and torreEscolha < 4 and torreEscolha > 0):
            torreSaida = int(input("De qual torre deseja retirar o disco?(1,2,3) "))
            torreEscolha = int(input("Para qual torre irá o disco?(1,2,3,) "))


            if torreSaida != torreEscolha:
                aux == 1

            if not (torreSaida < 4 and torreSaida > 0 and torreEscolha < 4 and torreEscolha > 0):
                print("\nEscolha de torre inadequada\n")

        #Realiza a troca do disco nas torres]
        if comparaDisco(torreSaida, torreEscolha, torre1, torre2, torre3):
            trocaDeTorre(torreSaida, torreEscolha, torre1, torre2, torre3,jogadas)
            ListaJogadas(jogadas, torreSaida, torreEscolha)
            saiu = WinTeste(torre0, torre2, torre3)

        print(torre1)
        print(torre2)
        print(torre3)
        print(jogadas)
        
        #VoltarJogadas(jogadas,torre1,torre2,torre3)
        '''

    print("Parabéns você venceu")
