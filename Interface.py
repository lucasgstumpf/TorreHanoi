"""
-Colocar Lista de jogadas aparecendo
-Texto para torre entrada e torre saida e botao para confirmar
-Enfeites
-Botao Voltar jogada

"""


import TorreHanoi
from TorreHanoi import *
import tkinter as tk
from tkinter import *

app = Tk()
app.title("Torre de Hánoi")
app.geometry("1200x600")
app.configure(background="#ADEAEA")
app.resizable(True, False)

#TABULEIRO
# 320 e o Y da altura
# Para subir a peca -30

#-------------------------BASES-------------------------

torreInterface1=Label(app,background = "#808080",foreground ="#000")
torreInterface1.place(x=150,y=50,width="10",height="300")

torreInterface2=Label(app,background = "#808080",foreground ="#000")
torreInterface2.place(x=550,y=50,width="10",height="300")

torreInterface3=Label(app,background = "#808080",foreground ="#000")
torreInterface3.place(x=950,y=50,width="10",height="300")

base= Label(app,background = "#000",foreground ="#000")
base.place(x=30,y=350,width="1100",height="30")

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

TorreHanoi.main()

app.mainloop()
