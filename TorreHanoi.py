#------------------
def Teste():
    x = 5 
    return x




#------------------- Lista de jogadas
def ListaJogadas(jogadas,torreSaida,torreEscolha ):
    jogadas.append([torreSaida, torreEscolha])

#-------------------Voltar Jogadas

def VoltarJogadas(jogadas, torre1, torre2, torre3):
    ultima = int(len(jogadas) - 1)
    torreEscolha = int(jogadas[ultima][0])
    torreSaida = int(jogadas[ultima][1]) 
    trocaDeTorre(torreSaida, torreEscolha, torre1, torre2, torre3)


#-------------------Verifica se ganhou o jogo
def WinTeste(torre0,torre2,torre3):

    if (torre2 == torre0) or (torre3 == torre0):
        return True
    else:
        return False

#-------------------Realiza a troca do disco nas torres
def trocaDeTorre(torreSaida, torreEscolha, torre1, torre2, torre3):
    if torreSaida == 1:
        if torreEscolha == 2:
            novoDisco = retirarTorre(torre1)
            acrescentarTorre(torre2,novoDisco)
        elif torreEscolha == 3:
            novoDisco = retirarTorre(torre1)
            acrescentarTorre(torre3,novoDisco)
    elif torreSaida == 2:
        if torreEscolha == 1:
            novoDisco = retirarTorre(torre2)
            acrescentarTorre(torre1,novoDisco)
        elif torreEscolha == 3:
            novoDisco = retirarTorre(torre2)
            acrescentarTorre(torre3,novoDisco)
    elif torreSaida == 3:
        if torreEscolha == 1:
            novoDisco = retirarTorre(torre3)
            acrescentarTorre(torre1,novoDisco)
        elif torreEscolha == 2:
            novoDisco = retirarTorre(torre3)
            acrescentarTorre(torre2,novoDisco)

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
    totalDiscos = int(input("Digite a quantidade de discos: "))

    #Inicialização das torres
    torre0 = []
    torre1 = []
    torre2 = []
    torre3 = []
    jogadas = []

    
    #Acrescenta todos os discos na torre 1
    while totalDiscos > 0:
        acrescentarTorre(torre1,totalDiscos)
        acrescentarTorre(torre0,totalDiscos)
        totalDiscos -= 1

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

            ListaJogadas(jogadas,torreSaida,torreEscolha) #Armazena as jogadas

            if torreSaida != torreEscolha:
                aux == 1
            if not (torreSaida < 4 and torreSaida > 0 and torreEscolha < 4 and torreEscolha > 0):
                print("\nEscolha de torre inadequada\n")
            


        #Realiza a troca do disco nas torres
        trocaDeTorre(torreSaida, torreEscolha, torre1, torre2, torre3)
        saiu = WinTeste(torre0, torre2, torre3)

        print(torre1)
        print(torre2)
        print(torre3)
        print(jogadas)

    print("Parabéns você venceu")

main()