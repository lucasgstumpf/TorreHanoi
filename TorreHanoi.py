
import Interface
from Interface import *

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
    Interface.UIJogadas(jogadas)

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
            discoSaida = len(torre1)
            discoEscolha = len(torre3)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre1[discoSaida-1] > torre3[discoEscolha-1]:
                certo = True
            
    
    elif torreSaida == 2:
        if torreEscolha == 1:
            discoSaida = len(torre2) 
            discoEscolha = len(torre1)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre2[discoSaida-1] > torre1[discoEscolha-1]:
                certo = True

        elif torreEscolha == 3:
            discoSaida = len(torre2) 
            discoEscolha = len(torre3)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre2[discoSaida-1] > torre3[discoEscolha-1]:
                certo = True
 
    elif torreSaida == 3:
        if torreEscolha == 1:
            discoSaida = len(torre3)
            discoEscolha = len(torre1)
            if discoEscolha == 0:
                certo = True
                return certo
            elif torre3[discoSaida-1] > torre1[discoEscolha-1]:
                certo = True

        elif torreEscolha == 2:
            discoSaida = len(torre3)
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


#------------------Função Principal
def main():
    print("Programa iniciado! Divirta-se")
    #Pergunta a quantidade de discos


    