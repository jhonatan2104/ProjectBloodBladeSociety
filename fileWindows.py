from tkinter import *
from fileClass import *
from functools import partial


class TelaEscolhaBot:
    def __init__(self):
        self.btSizeX = 100
        self.btSizeY = 150
        self.margeX = 150
        self.margeY = 100
        self.x = 200
        self.y = 200
        self.color = "Black"
        self.root = Tk()
        self.imagemLabelBOT = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/ImagemLabelBOT.png")
        self.imagemLabelPlayer = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/ImagemLabelPlayer.png")
        self.IchigoKurosakiPNG = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.KillerBeePNG = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.XenaPNG = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.RoronoaZoroPNG = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.GohanPNG = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.backPNG = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/backPNG.png")
        self.bt1 = Button(self.root, image= self.IchigoKurosakiPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt2 = Button(self.root, image= self.KillerBeePNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt3 = Button(self.root, image= self.XenaPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt4 = Button(self.root, image= self.RoronoaZoroPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt5 = Button(self.root, image= self.GohanPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.lb = Label(self.root, image=self.imagemLabelPlayer, bg=self.color)

        self.btVoltar = Button(self.root,image=self.backPNG,bg="Black")
        self.bts = [[self.bt1, self.bt2, self.bt3], [self.bt4, self.bt5]]
        self.p1 = None
        self.BOT = None

    def choose(self,player):
        if self.p1 == None:
            player.PlayWAVShow()
            self.p1 = player
            self.lb["image"] = self.imagemLabelBOT
        elif self.BOT == None:
            player.PlayWAVShow()
            self.BOT = player
            #Alter essa parte do código quando CRIAR A TELA MAIN
            print(self.p1.name, self.BOT.name)
    def voltar(self):
        self.root.destroy()
        TelaInicio().construtor()
    def construtor(self):
        self.root.geometry("800x500+300+100")
        self.root["bg"] = self.color
        contCamp = 0
        for line in range(len(self.bts)):
            for column in range(len(self.bts[line])):
                self.bts[line][column]["command"] = partial(self.choose, System.choosePlayer(contCamp))
                contCamp += 1
                self.bts[line][column].place(x=self.x*column+self.margeX, y=self.y*line+self.margeY)
        self.lb.pack(side=TOP)
        self.btVoltar.pack(side=BOTTOM,anchor=SE)
        self.btVoltar["command"] = self.voltar
        self.root.mainloop()


class TelaInicio:
    def __init__(self):
        self.margeX = 0
        self.margeY = 150
        self.x = 265
        self.y = 200
        self.color = "Black"
        self.root = Tk()
        self.imagemPlayerXbot = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/playerXbotPNG.png")

        self.imagemPlayerXplayer = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/playerXplayerPNG.png")
        self.imagemLabel = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/ESCOLHA-O-MODO-DE-JOGO.png")

        self.bt1 = Button(self.root, image=self.imagemPlayerXbot)
        self.bt2 = Button(self.root, image=self.imagemPlayerXplayer)
        self.lb = Label(self.root, image=self.imagemLabel)

    def abrirTelaEscolhaPlayerBOT(self):
        self.root.destroy()
        TelaEscolhaBot().construtor()

    def abrirTelaEscolhaPlayer(self):
        self.root.destroy()
        #MUDAR ESSA PARTE DO CÓDIGO
        TelaEscolhaBot().construtor()

    def construtor(self):
        self.root.geometry("800x500+300+100")
        self.root["bg"] = self.color
        self.lb["bg"] = self.color
        self.lb.pack(side=TOP)
        self.bt1.place(x=self.x, y=self.y)
        self.bt2.place(x=self.x+self.margeX, y=self.y+self.margeY)
        self.bt1["command"] = self.abrirTelaEscolhaPlayerBOT
        self.bt2["command"] = self.abrirTelaEscolhaPlayer
        self.root.mainloop()
TelaInicio().construtor()

