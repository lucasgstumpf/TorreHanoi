import TorreHanoi
from TorreHanoi import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial
import time

#-------------------------JANELA 01 --------------
app = tk.Tk()
app.title("Torre de Hánoi")
app.geometry("1200x600")
app.configure(background="#ADEAEA")
app.resizable(True, False)

#-------------------------VARIÁVEIS GLOBAIS---------
torre0 = []
torre1 = []
torre2 = []
torre3 = []
jogadas = []
inicioJogo = 0
fimJogo = 0

#-------------------------TEMPO DE JOGO--------
def iniciarJogo():
    global inicioJogo
    inicioJogo = time.time()
    totalDiscos = int(vTotalDisco.get())
    UIInicializarDiscos(totalDiscos)
    i = 1
    while i <= totalDiscos:
        TorreHanoi.acrescentarTorre(torre1,i)
        TorreHanoi.acrescentarTorre(torre0,i)
        i += 1

def tempo():
    fimJogo = time.time()
    tempoTotal = fimJogo - inicioJogo
    tempoTotal = round(tempoTotal,0)
    tk.messagebox.showinfo("Tempo de jogo ", tempoTotal)

#-------------------------Imprimir Jogadas---------
def mostrarJogada(jogadas, novaJanela):
 
    if not jogadas:
        finalJogadas()
        return 

    moveu = jogadas[0][0]
    moveuDe = Label(novaJanela,background = "#fff",foreground ="#000")
    moveuDe["text"] = str(moveu)
    moveuDe.place(x=150,y=150,width="150",height="30")
    
    para = jogadas[0][1]
    paraTal = Label(novaJanela,background = "#fff",foreground ="#000")
    paraTal["text"] = str(para)
    paraTal.place(x=450,y=150,width="150",height="30")

    jogadas.pop(0) 

def UIJogadas2(jogadas):
    novaJanela = tk.Toplevel(app)
    novaJanela.title = "Suas jogadas"
    novaJanela.geometry("800x600")
    novaJanela.configure(background="#ADEAEA")
    novaJanela.resizable(True, False)

    buttonJogadas = tk.Button(novaJanela, text = "Histórico de Jogadas",background = "#fff",foreground ="#000")
    buttonJogadas["command"] = partial(mostrarJogada,jogadas, novaJanela)
    buttonJogadas.place(x=300,y=250,width="150",height="30")
    
    
    Label(novaJanela,text="Histórico de jogadas",background = "#4169e1",foreground ="#000").place(x=300,y=10,width="150",height="60")
    Label(novaJanela,text="Moveu de:",background = "#ADEAEA",foreground ="#000").place(x=150,y=100,width="150",height="30")

    Label(novaJanela,text="Para:",background = "#ADEAEA",foreground ="#000").place(x=450,y=100,width="150",height="30")

    vListaJogadas = Label(novaJanela,background = "#ADEAEA",foreground ="#000")

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
disco6 = Label(app,background = "#ff0",foreground ="#000")
disco5 = Label(app,background = "#f23",foreground ="#000")
disco4 = Label(app,background = "#103",foreground ="#000")
disco3 = Label(app,background = "#080",foreground ="#000")
disco2 = Label(app,background = "#ff007f",foreground ="#000")
disco1 = Label(app,background = "#0000ff",foreground ="#000")

#-------------------------Entradas de dados das torres--------
def moverDiscos(torre0, torre1,torre2, torre3, jogadas, fimJogo):
    torreSaida = int(vTorreSaida.get())
    torreEscolha = int(vTorreEntrada.get())

    if torreSaida > 3 or torreSaida < 1 or torreEscolha > 3 or torreEscolha < 1:
        torreInexistete()

    if torreSaida == torreEscolha:
        torresIguais()

    if TorreHanoi.comparaDisco(torreSaida, torreEscolha, torre1, torre2, torre3):
        TorreHanoi.trocaDeTorre(torreSaida, torreEscolha, torre1, torre2, torre3, jogadas)
        TorreHanoi.ListaJogadas(jogadas, torreSaida, torreEscolha)
    else:
        superioridade()

    if TorreHanoi.WinTeste(torre0, torre2, torre3):
        vitoria()
        
#--------------------------Erros------------------------
def torresIguais():
    tk.messagebox.showwarning("Erro de escolha de torre", "Não pode escolher a mesma torre para saída e entrada de discos")

def torreInexistete():
    tk.messagebox.showwarning("Erro de escolha de torre", "A torre escolhida não existe")

def superioridade():
   tk.messagebox.showwarning("Erro de escolha de torre", "Não pode colocar um disco maior sobre um menor")

def torreSemDisco():
    tk.messagebox.showwarning("Erro de escolha de torre", "A torre escolhida não epossui disco")

def finalJogadas():
    tk.messagebox.showinfo("Histórico de jogadas", "Final da fila de jogadas")

#-------------------------VITORIA------------------------
def vitoria():
    tk.messagebox.showinfo("Vitória", "Parabéns, você venceu!!!")

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

#-------------------------Mover discos-----------------------
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

Label(app,text="Digite a torre de saida",background = "#ADEAEA",foreground ="#000").place(x=250,y=400,width="150",height="30")
vTorreSaida = Entry(app)
vTorreSaida.place(x=250,y=420,width="150",height="20")

Label(app,text="Digite a torre de Entrada",background = "#ADEAEA",foreground ="#000").place(x=250,y=440,width="150",height="30")
vTorreEntrada = Entry(app)
vTorreEntrada.place(x=250,y=460,width="150",height="20")

button01 = Button(app,text="Mover")
button01["command"] = partial(moverDiscos, torre0, torre1, torre2, torre3, jogadas, fimJogo)
button01.place(x=250,y=500,width="150",height="30")

button02 = Button(app,text="Voltar jogada")
button02["command"] = partial(TorreHanoi.VoltarJogadas, jogadas, torre1, torre2, torre3)
button02.place(x=500,y=420,width="150",height="30")

button03 = Button(app,text="Começar!", command=iniciarJogo).place(x=10,y=450,width="150",height="30")

button04 = Button(app, text="Tempo de jogo", command=tempo).place(x=500,y=500,width="150",height="30")

button05 = Button(app, text="Histórico de jogadas")
button05["command"] = partial(UIJogadas2, jogadas)
button05.place(x=500,y=460,width="150",height="30")

#-------------------------EXECUÇÃO----------------------
TorreHanoi.main()

app.mainloop()
