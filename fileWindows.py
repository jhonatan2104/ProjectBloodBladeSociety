from tkinter import *
from fileClass import *
from functools import partial
import time


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
        self.IchigoKurosakiPNG = PhotoImage(file=System.choosePlayer(0).imageShow)
        self.KillerBeePNG = PhotoImage(file=System.choosePlayer(1).imageShow)
        self.XenaPNG = PhotoImage(file=System.choosePlayer(2).imageShow)
        self.RoronoaZoroPNG = PhotoImage(file=System.choosePlayer(3).imageShow)
        self.GohanPNG = PhotoImage(file=System.choosePlayer(4).imageShow)
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
            self.root.destroy()
            TelaMain(self.p1, self.BOT).construtor()

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
    def __init__(self, player, bot):
        self.root = Tk()
        self.player = player
        self.bot = bot
        self.imageLife1 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageLife2 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageMana1 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageMana2 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")

        self.lbLifePlayer = Label(self.root, width=200, height=60, image=self.imageLife1)
        self.lbLifeBOT = Label(self.root, width=200, height=60, image=self.imageLife2)
        self.lbManaPlayer = Label(self.root, width=200, height=60, image=self.imageMana1)
        self.lbManaBOT = Label(self.root, width=200, height=60, image=self.imageMana2)

        self.yDisplayLifi = 370
        self.xDisplayLifiPlayer = 40
        self.xDisplayLifiBOT = 1260

        self.yDisplayMana = 550
        self.xDisplayManaPlayer = 40
        self.xDisplayManaBOT = 1260

        self.c1 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c2 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c3 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c4 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayLifePlayer = [self.c1, self.c2, self.c3, self.c4]

        self.c5 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c6 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c7 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c8 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayLifeBOT = [self.c5, self.c6, self.c7, self.c8]

        self.c9 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c10 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c11 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c12 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayManaPlayer = [self.c9, self.c10, self.c11, self.c12]

        self.c13 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c14 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c15 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c16 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayManaBOT = [self.c13, self.c14, self.c15, self.c16]

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
        strNumber = number if len(number) == len(display) else "#"*(len(display)-len(number))+str(number)
        for elem in range(len(display)):
            imag = dicImagens[strNumber[elem]]
            display[elem].create_image(30, 35, image=imag)
            display[elem].image = imag

    def construtor(self):
        self.root.geometry("1500x780+12+0")
        self.root["bg"] = "Black"

        #Display LIFE PLAYER
        for j in range(len(self.displayLifePlayer)):
            self.displayLifePlayer[j].config(bg="Black")
            self.displayLifePlayer[j].place(x=j*50+self.xDisplayLifiPlayer, y=self.yDisplayLifi+80)
        self.lbLifePlayer.place(x=self.xDisplayLifiPlayer, y=self.yDisplayLifi)
        for j in range(len(self.displayManaPlayer)):
            self.displayManaPlayer[j].config(bg="Black")
            self.displayManaPlayer[j].place(x=j*50+self.xDisplayManaPlayer, y=self.yDisplayMana+80)
        self.lbManaPlayer.place(x=self.xDisplayManaPlayer, y=self.yDisplayMana)

        # Display LIFE BOT
        for j in range(len(self.displayLifeBOT)):
            self.displayLifeBOT[j].config(bg="Black")
            self.displayLifeBOT[j].place(x=j*50+self.xDisplayLifiBOT, y=self.yDisplayLifi+80)
        self.lbLifeBOT.place(x=self.xDisplayLifiBOT, y=self.yDisplayLifi)
        for j in range(len(self.displayManaBOT)):
            self.displayManaBOT[j].config(bg="Black")
            self.displayManaBOT[j].place(x=j*50+self.xDisplayManaBOT, y=self.yDisplayMana+80)
        self.lbManaBOT.place(x=self.xDisplayManaBOT, y=self.yDisplayMana)

        self.setDisplay(str(self.player.hp), self.displayLifePlayer)
        self.setDisplay(str(self.bot.hp), self.displayLifeBOT)
        self.setDisplay(str(self.player.mana), self.displayManaBOT)
        self.setDisplay(str(self.bot.mana), self.displayManaPlayer)
        self.root.mainloop()


TelaInicio().construtor()