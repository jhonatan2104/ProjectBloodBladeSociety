from tkinter import *
from fileClass import *
from functools import partial

class TelaEscolhaBot:
    def __init__(self):
        self.btSizeX = 100
        self.btSizeY = 150
        self.marge = 40
        self.x = 200
        self.y = 200
        self.color = "Black"
        self.root = Tk()
        self.IchigoKurosaki = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.KillerBee = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.Xena = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.RoronoaZoro = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.Gohan = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.bt1 = Button(self.root, image= self.IchigoKurosaki, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt2 = Button(self.root, image= self.KillerBee, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt3 = Button(self.root, image= self.Xena, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt4 = Button(self.root, image= self.RoronoaZoro, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt5 = Button(self.root, image= self.Gohan, width=self.btSizeX,
                          height=self.btSizeY)
        self.lb = Label(self.root, text = "ESCOLHA O SEU CAMPEÃO")
        self.bts = [[self.bt1, self.bt2, self.bt3], [self.bt4, self.bt5]]
        self.p1 = None
        self.BOT = None

    def choose(self,player):
        if self.p1 == None:
            self.p1 = player
            self.lb["text"] = "ESCOLHA QUEM DESEJA DASAFIAR"
        elif self.BOT == None:
            self.BOT = player
            #Alter essa parte do código quando CRIAR A TELA MAIN
            print(self.p1.name, self.BOT.name)

    def construtor(self):
        self.root.geometry("600x600+100+100")
        contCamp = 0
        for line in range(len(self.bts)):
            for column in range(len(self.bts[line])):
                self.bts[line][column]["command"] = partial(self.choose, System.choosePlayer(contCamp))
                contCamp += 1
                self.bts[line][column].place(x=self.x*column+self.marge, y=self.y*line+self.marge)
        self.lb.pack(side=TOP)
        self.root.mainloop()
r = TelaEscolhaBot()
r.construtor()