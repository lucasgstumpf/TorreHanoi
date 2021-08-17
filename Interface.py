"""
-Enfeites

"""

import TorreHanoi
from TorreHanoi import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial

app = tk.Tk()
app.title("Torre de Hánoi")
app.geometry("1200x600")
app.configure(background="#ADEAEA")
app.resizable(True, False)

#Inicializar torres
torre0 = []
torre1 = []
torre2 = []
torre3 = []
jogadas = []

def iniciarJogo():
    totalDiscos = int(vTotalDisco.get())
    UIInicializarDiscos(totalDiscos)
    i = 1
    while i <= totalDiscos:
        TorreHanoi.acrescentarTorre(torre1,i)
        TorreHanoi.acrescentarTorre(torre0,i)
        UIJogadas(jogadas)
        i += 1
    print(torre1)
    print(torre2)
    print(torre3)

#-------------------------Imprimir Jogadas------------------------

def UIJogadas(jogadas):
    Label(app,text="Lista de Jogadas",background = "#ADEAEA",foreground ="#000").place(x=440,y=400,width="150",height="30")
    vListaJogadas = Label(app,background = "#4169e1",foreground ="#000")
    vListaJogadas["text"] = str(jogadas)
    vListaJogadas.place(x=460,y=420,width="200",height="50")

#-------------------------BASES-------------------------
def UIInicializarBases():
    torreInterface1=Label(app,background = "#808080",foreground ="#000")
    torreInterface1.place(x=150,y=50,width="10",height="300")

    torreInterface2=Label(app,background = "#808080",foreground ="#000")
    torreInterface2.place(x=550,y=50,width="10",height="300")

    torreInterface3=Label(app,background = "#808080",foreground ="#000")
    torreInterface3.place(x=950,y=50,width="10",height="300")

    base= Label(app,background = "#000",foreground ="#000")
    base.place(x=30,y=350,width="1100",height="30")
UIInicializarBases()



#-------------------------DISCOS-------------------------
#AlturaDisco = 170 + (30* altura) 
#Trocar y pela altura disco1
#o X deve ser mudado para x = (numero padrao) + (Torre * 400)
#

disco6 = Label(app,background = "#ff0",foreground ="#000")
#disco1.place(x=117,y=170,width="75",height="30")

disco5 = Label(app,background = "#f23",foreground ="#000")
#disco2.place(x=103,y=200,width="105",height="30")

disco4 = Label(app,background = "#103",foreground ="#000")
#disco3.place(x=89,y=230,width="135",height="30")

disco3 = Label(app,background = "#080",foreground ="#000")
#disco4.place(x=75,y=260,width="165",height="30")

disco2 = Label(app,background = "#ff007f",foreground ="#000")
#disco5.place(x=61,y=290,width="195",height="30")

disco1 = Label(app,background = "#0000ff",foreground ="#000")
#disco6.place(x=47,y=320,width="225",height="30")



#-------------------------Entradas de dados das torres
def moverDiscos(torre1,torre2, torre3, jogadas):
    torreSaida = int(vTorreSaida.get())
    torreEscolha = int(vTorreEntrada.get())

    if torreSaida > 3 or torreSaida < 1 or torreEscolha > 3 or torreEscolha < 1:
        #warning de torre não existente
        torreInexistete()

    if torreSaida == torreEscolha:
        #warning de escolha da mesma torre para entrada e saida
        torresIguais()
    #Realiza a troca do disco nas torres]
    if TorreHanoi.comparaDisco(torreSaida, torreEscolha, torre1, torre2, torre3):
        TorreHanoi.trocaDeTorre(torreSaida, torreEscolha, torre1, torre2, torre3,jogadas)
        TorreHanoi.ListaJogadas(jogadas, torreSaida, torreEscolha)
    else:
        superioridade()
        #warning de colocar disco menor em uma maior

    print(torre1)
    print(torre2)
    print(torre3)
    UIJogadas(jogadas)

#--------------------------Erros
def torresIguais():
    tk.messagebox.showwarning("Erro de escolha de torre", "Não pode escolher a mesma torre para saída e entrada de discos")

def torreInexistete():
    tk.messagebox.showwarning("Erro de escolha de torre", "A torre escolhida não existe")

def superioridade():
    tk.messagebox.showwarning("Erro de escolha de torre", "Não pode colocar um disco maior sobre um menor")

#-------------------------Inicializa a interface dos discos-------------------------
def UIInicializarDiscos(totalDiscos):
    aux = 0
    if aux < totalDiscos:
        disco1.place(x=47,y=320,width="225",height="30")
        aux = aux + 1
    if aux < totalDiscos:
        disco2.place(x=61,y=290,width="195",height="30")
        aux = aux + 1
    if aux < totalDiscos:
        disco3.place(x=75,y=260,width="165",height="30")
        aux = aux + 1
    if aux < totalDiscos:
        disco4.place(x=89,y=230,width="135",height="30")
        aux = aux + 1
    if aux < totalDiscos:
        disco5.place(x=103,y=200,width="105",height="30")
        aux = aux + 1
    if aux < totalDiscos:
        disco6.place(x=117,y=170,width="75",height="30")

# FUNÇÃO PARA MOVER OS DISCOS
#Precisa receber o numero do disco que quer sair, e precisa saber qual torre vai e qual posição,
#Precisa saber a posição no array q ele vai entrar( len()-1)
#Criar uma função que ve a altura do negocio

def UIMoverDisco(disco,torreEscolha,altura):
    if disco == 6:
        disco6.place(x= (117+((torreEscolha - 1)*400)),y= 320 - (30* altura) ,width="75",height="30")
   
    elif disco == 5:
        disco5.place(x=103+(((torreEscolha - 1)*400)),y= 320 - (30* altura) ,width="105",height="30")

    elif disco == 4:
        disco4.place(x=89 +(((torreEscolha - 1)*400)),y=320 - (30* altura) ,width="135",height="30")

    elif disco == 3:
        disco3.place(x=75 +(((torreEscolha - 1)*400)),y=320 - (30* altura),width="165",height="30")

    elif disco == 2:
        disco2.place(x=61 +(((torreEscolha - 1)*400)),y=320 - (30* altura),width="195",height="30")

    elif disco == 1:
        disco1.place(x=47 +(((torreEscolha - 1)*400)),y=320 - (30* altura),width="225",height="30")

#-------------------------BOTÕES-------------------------

Label(app,text="Digite o número de discos",background = "#ADEAEA",foreground ="#000").place(x=10,y=400,width="150",height="30")
vTotalDisco = Entry(app)
vTotalDisco.place(x=10,y=420,width="150",height="20")
button03 = Button(app,text="Começar!", command= iniciarJogo).place(x=10,y=550,width="150",height="30")

Label(app,text="Digite a torre de saida",background = "#ADEAEA",foreground ="#000").place(x=250,y=400,width="150",height="30")
vTorreSaida = Entry(app)
vTorreSaida.place(x=250,y=420,width="150",height="20")
Label(app,text="Digite a torre de Entrada",background = "#ADEAEA",foreground ="#000").place(x=250,y=440,width="150",height="30")
vTorreEntrada = Entry(app)
vTorreEntrada.place(x=250,y=460,width="150",height="20")

button01 = Button(app,text="Mover")
button01["command"] = partial(moverDiscos,torre1,torre2, torre3,jogadas)
button01.place(x=250,y=490,width="150",height="30")

button02 = Button(app,text="Voltar jogada")
button02["command"] = partial(TorreHanoi.VoltarJogadas,jogadas, torre1, torre2, torre3)
button02.place(x=250,y=540,width="150",height="30")


TorreHanoi.main()

app.mainloop()
