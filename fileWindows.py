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
        if self.p1 is None:
            player.PlayWAVShow()
            self.p1 = player
            self.lb["image"] = self.imagemLabelBOT
        elif self.BOT is None:
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
        self.btVoltar.pack(side=BOTTOM, anchor=SE)
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


class TelaMain:
    def __init__(self):
        self.root = Tk()
        self.lb1 = Canvas(self.root, width=300, height=200)
        self.lb2 = Canvas(self.root, width=300, height=200)
        self.lb3 = Canvas(self.root, width=300, height=200)
        self.bts1 = [self.lb1, self.lb2, self.lb3]
        self.lb4 = Canvas(self.root, width=300, height=200)
        self.lb5 = Canvas(self.root, width=300, height=200)
        self.lb6 = Canvas(self.root, width=300, height=200)
        self.bts2 = [self.lb4, self.lb5, self.lb6]

    def setDisplay(self, number, display):
        dicImagens = {
            "#": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/#.png"),
            "0": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/#.png"),
            "1": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/1.png"),
            "2": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/2.png"),
            "3": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/3.png"),
            "4": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/4.png"),
            "5": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/5.png"),
            "6": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/6.png"),
            "7": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/7.png"),
            "8": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/8.png"),
            "9": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/9.png")
        }
        l = [
            PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/2.png")
        ]
        strNumber = number if len(number) == len(display) else "#"*(len(display)-len(number))+str(number)
        for elem in range(len(display)):
            imag = dicImagens[strNumber[elem]]
            display[elem].create_image(50, 70, image=imag)
            display[elem].image = imag

    def construtor(self):
        self.root.geometry("800x500+100+100")

        for indexBt in range(len(self.bts1)):
            self.bts1[indexBt].place(x=100*indexBt+200, y=100)
        for indexBt in range(len(self.bts2)):
            self.bts2[indexBt].place(x=100*indexBt+200, y=300)
        self.setDisplay(str(4), self.bts1)
        self.setDisplay(str(452), self.bts2)
        self.root.mainloop()

TelaMain().construtor()


