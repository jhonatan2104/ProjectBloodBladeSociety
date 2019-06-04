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

        # PLAYER
        self.player = player
        self.bot = bot
        #CRIAR A UMA INSTÂNCIA DA INTALIGÊNCIA BOT
        self.intelBOT = InteligencePlayer(self.bot, 200)

        # DADOS PLAYER
        self.damageMagico = 0
        self.damageFisico = 0
        self.CONTAttackFalhos = 0
        self.CONTAttackCriticos = 0
        self.CONTAttack = 0
        self.damageMagicoSofrido = 0
        self.damageFisicoSofrido = 0
        self.manaRestaurada = 0
        self.manaGasta = 0

        # IMAGE PLAYER
        self.ImageShowPlayer = PhotoImage(file=self.player.imageShow)
        self.ImageIDPlayer = PhotoImage(file=player.imageID)
        self.ImageIDSwordPlayer = PhotoImage(file=player.sword.imageID)
        self.ImageIDShieldPlayer = PhotoImage(file=player.shield.imageID)

        # IMAAGE BOT
        self.ImageShowBOT = PhotoImage(file=self.bot.imageShow)
        self.ImageIDBOT = PhotoImage(file=bot.imageID)
        self.ImageIDSwordBOT = PhotoImage(file=bot.sword.imageID)
        self.ImageIDShieldBOT = PhotoImage(file=bot.shield.imageID)

        # Lb Player
        self.lbPlAYER = Label(self.root, image=self.ImageShowPlayer, width=100, height=150)
        self.nomePlAYER = Label(self.root, image=self.ImageIDPlayer, width=200, height=60, bg="Black")
        self.swordPlAYER = Label(self.root, image=self.ImageIDSwordPlayer, width=200, height=60, bg="Black")
        self.shieldPlayer = Label(self.root, image=self.ImageIDShieldPlayer, width=200, height=60, bg="Black")

        # Lb BOT
        self.lbBtBOT = Button(self.root, image=self.ImageShowBOT, width=100, height=150)
        self.nomeBOT = Label(self.root, image=self.ImageIDBOT, width=200, height=60, bg="Black")
        self.swordBOT = Label(self.root, image=self.ImageIDSwordBOT, width=200, height=60, bg="Black")
        self.shieldBOT = Label(self.root, image=self.ImageIDShieldBOT, width=200, height=60, bg="Black")

        self.imageLife1 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/life.png")
        self.imageLife2 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/life.png")
        self.imageMana1 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/mana.png")
        self.imageMana2 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/mana.png")

        self.lbLifePlayer = Label(self.root, width=200, height=60, image=self.imageLife1,  bg="Black")
        self.lbLifeBOT = Label(self.root, width=200, height=60, image=self.imageLife2, bg="Black")
        self.lbManaPlayer = Label(self.root, width=200, height=60, image=self.imageMana1, bg="Black")
        self.lbManaBOT = Label(self.root, width=200, height=60, image=self.imageMana2, bg="Black")

        #CANVAS STATUS
        self.imageStatusFalhou = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageStatusEfetivo = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageStatusCritico = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageStatusHome = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageStatusManaAlerta = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")

        self.canvasStatus = Canvas(self.root, width=725, height=200, highlightbackground="Black")

        #CANVAS ATTACK DICA
        self.canvasAttackDica = Canvas(self.root, width=725, height=200, highlightbackground="Black")

        #CONFIG DISPLAY
        self.yDisplayLifi = 450
        self.xDisplayLifiPlayer = 50
        self.xDisplayLifiBOT = 1250

        self.yDisplayMana = 610
        self.xDisplayManaPlayer = 50
        self.xDisplayManaBOT = 1250

        #DISPLAY
        self.c1 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c2 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c3 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c4 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c17 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayLifePlayer = [self.c1, self.c2, self.c3, self.c4, self.c17]

        self.c5 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c6 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c7 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c8 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c18 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayLifeBOT = [self.c5, self.c6, self.c7, self.c8, self.c18]

        self.c9 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c10 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c11 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c12 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c19 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayManaPlayer = [self.c9, self.c10, self.c11, self.c12, self.c19]

        self.c13 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c14 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c15 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c16 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c20 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayManaBOT = [self.c13, self.c14, self.c15, self.c16, self.c20]

        # CONFIG DISPLAY DANO, LATÊNCIA
        self.xMargeDisplayDL = 750
        self.xMargeLabelDL = 550
        self.yMargeDisplayDL = 450

        #IMAGE DANO, LATÊNCIA
        self.imgLatencia = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png"
        )
        self.imgDanoReal = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png"
        )

        #LABEL DANO, LATÊNCIA
        self.lbLatencia = Label(self.root, width=200, height=60, highlightbackground="Black", image=self.imgLatencia)
        self.lbDanoReal = Label(self.root, width=200, height=60, highlightbackground="Black", image=self.imgDanoReal)

        # DISPLAY DANO
        self.c21 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c22 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c23 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c24 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoReal = [self.c21, self.c22, self.c23, self.c24]

        # DISPLAY LATENCIA
        self.c25 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayLatencia = [self.c25]

        #BOTÕES DE ATTACK
        self.canvasAttk = Canvas(self.root, width=725, height=170, highlightbackground="Black")
        self.imageATTK1 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageATTK2 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageATTK3 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.imageDEF = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
        self.btAttk1 = Button(self.canvasAttk, width=175, height=160, image= self.imageATTK1)
        self.btAttk2 = Button(self.canvasAttk, width=175, height=160, image=self.imageATTK2)
        self.btAttk3 = Button(self.canvasAttk, width=175, height=160, image=self.imageATTK3)
        self.btdef1 = Button(self.canvasAttk, width=175, height=160, image=self.imageDEF)
        self.BTSCommands = [self.btAttk1, self.btAttk2, self.btAttk3, self.btdef1]

    def ActionBOT(self):
        attacksBOT = self.bot.sword.getAttack()
        value = self.intelBOT.resolverAttack(self.player)

        if value == 3:
            self.setCanvasStatus(3)
            self.setCanvasDICA()
            self.bot.restoreMana(0)

            # SET DISPLAY DADOS
            self.setDisplay(self.bot.mana, self.displayManaBOT)
            self.setDisplay(0, self.displayDanoReal)
            self.setDisplay(0, self.displayLatencia)
        else:
            attackBOT = attacksBOT[value]
            # o numero randomico para a latencia
            randomLatenciaAtaque = randint(0, 9)
            self.setDisplay(randomLatenciaAtaque, self.displayLatencia)
            if attackBOT.latencia <= randomLatenciaAtaque:
                # ATAQUE EFETIVO
                randomLatenciaDefesa = randint(0, 9)

                if self.player.shield.latencia <= randomLatenciaDefesa:
                    # DEFESA EFETIVA
                    self.setCanvasStatus(1)
                    self.setCanvasDICA(attackBOT)

                    # DADOS JOGÁVEIS
                    danos = System.calculeteDamageShield(self.player, attackBOT)
                    danoReal = danos[0] + danos[1]
                    self.player.sufferDamage(danoReal)
                    self.bot.userMana(attackBOT.mana)
                    self.bot.restoreMana(danoReal)

                    # DADOS ARMAZENÁVEIS
                    self.damageFisicoSofrido += danos[0]
                    self.damageMagicoSofrido += danos[1]

                    if self.verificarGame():
                        self.root.destroy()
                    else:
                        # SET DISPLAY DADOS
                        self.setDisplay(danoReal, self.displayDanoReal)
                        self.setDisplay(self.player.hp, self.displayLifePlayer)
                        self.setDisplay(self.bot.mana, self.displayManaBOT)
                else:
                    # DEFESA NAO EFETIVA
                    self.setCanvasStatus(2)
                    self.setCanvasDICA(attackBOT)

                    # DADOS JOGÁVEIS
                    danos = System.calculeteDamage(attackBOT)
                    danoReal = danos[0] + danos[1]
                    self.player.sufferDamage(danoReal)
                    self.bot.userMana(attackBOT.mana)
                    self.bot.restoreMana(danoReal)

                    # DADOS ARMAZENÁVEIS
                    self.damageFisicoSofrido += danos[0]
                    self.damageMagicoSofrido += danos[1]

                    if self.verificarGame():
                        self.root.destroy()
                    else:
                        # SET DISPLAY DADOS
                        self.setDisplay(danoReal, self.displayDanoReal)
                        self.setDisplay(self.player.hp, self.displayLifePlayer)
                        self.setDisplay(self.bot.mana, self.displayManaBOT)
            else:
                # ATAQUE NAO EFETIVO
                self.setCanvasStatus(0)
                self.setCanvasDICA(attackBOT)

                if self.verificarGame():
                    self.root.destroy()
                else:
                    # SET DISPLAY DADOS
                    self.setDisplay(0, self.displayDanoReal)

    def setDisplay(self, num, display):
        number = str(num)
        dicImagens = {
            "#": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/0.png"),
            "0": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/0.png"),
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

    def setCanvasStatus(self, status):
        '''
        :param status:  -1 - bem-vindo; 0 - falhou ;1 - efetivo; 2 - crítico; 3 - Mana insuficiente
        :return: Void
        '''
        if status == -1:
            self.canvasStatus.create_image(0, 0, image=self.imageStatusHome)
            self.canvasStatus.image = self.imageStatusHome
        elif status == 0:
            self.canvasStatus.create_image(0, 0, image=self.imageStatusFalhou)
            self.canvasStatus.image = self.imageStatusFalhou
        elif status == 1:
            self.canvasStatus.create_image(0, 0, image=self.imageStatusEfetivo)
            self.canvasStatus.image = self.imageStatusEfetivo
        elif status == 2:
            self.canvasStatus.create_image(0, 0, image=self.imageStatusCritico)
            self.canvasStatus.image = self.imageStatusCritico
        elif status == 3:
            self.canvasStatus.create_image(0, 0, image=self.imageStatusManaAlerta)
            self.canvasStatus.image = self.imageStatusManaAlerta

    def setCanvasDICA(self, attack=None):
        if attack is None:
            self.canvasAttackDica.config(bg="Black")
        else:
            imag = PhotoImage(file=attack.imageID)
            self.canvasAttackDica.create_image(0, 0, image=imag)
            self.canvasAttackDica.image = imag

    def verificarGame(self):
        if self.player.hp <= 0:
            print(f'''
                        {self.bot.name} ganhou!!
                        Dano Mágico : {self.damageMagico}
                    Dano Físico : {self.damageFisico}
                    Attacks Falhos : {self.CONTAttackFalhos} 
                    Attacks Críticos : {self.CONTAttackCriticos}
                    Attacks {self.CONTAttack}
                    Dano Mágico Sofrido {self.damageMagicoSofrido}
                    Dano Físico Sofrido {self.damageFisicoSofrido}
                    Mana Restaurada : {self.manaRestaurada}
                    Mana Gata : {self.manaGasta}
                        ''')
            return True
        if self.bot.hp <= 0:
            print(f'''
                        {self.player.name} ganhou!!
                        Dano Mágico : {self.damageMagico}
                    Dano Físico : {self.damageFisico}
                    Attacks Falhos : {self.CONTAttackFalhos} 
                    Attacks Críticos : {self.CONTAttackCriticos}
                    Attacks {self.CONTAttack}
                    Dano Mágico Sofrido {self.damageMagicoSofrido}
                    Dano Físico Sofrido {self.damageFisicoSofrido}
                    Mana Restaurada : {self.manaRestaurada}
                    Mana Gata : {self.manaGasta}
                        ''')
            return True
        return False

    def defensiveMode(self):
        self.setCanvasStatus(3)
        self.setCanvasDICA()
        manaRestore = self.player.restoreMana(0)

        #SET DISPLAY DADOS
        self.setDisplay(self.player.mana, self.displayManaPlayer)
        self.setDisplay(0, self.displayDanoReal)
        self.setDisplay(0, self.displayLatencia)

        # DADOS ARMAZENÁVEIS
        self.manaRestaurada += manaRestore

    def knock(self, attack):
        # o numero randomico para a latencia
        randomLatenciaAtaque = randint(0, 9)
        self.setDisplay(randomLatenciaAtaque, self.displayLatencia)
        if attack.latencia <= randomLatenciaAtaque:
            # ATAQUE EFETIVO
            randomLatenciaDefesa = randint(0, 9)

            if self.bot.shield.latencia <= randomLatenciaDefesa:
                # DEFESA EFETIVA
                self.setCanvasStatus(1)
                self.setCanvasDICA(attack)

                #DADOS JOGÁVEIS
                danos = System.calculeteDamageShield(self.bot, attack)
                danoReal = danos[0] + danos[1]
                self.bot.sufferDamage(danoReal)
                self.player.userMana(attack.mana)
                manaRestore = self.player.restoreMana(danoReal)

                # DADOS ARMAZENÁVEIS
                self.damageFisico += danos[0]
                self.damageMagico += danos[1]
                self.CONTAttack += 1
                self.manaGasta += attack.mana
                self.manaRestaurada += manaRestore

                if self.verificarGame():
                    self.root.destroy()
                else:
                    #SET DISPLAY DADOS
                    self.setDisplay(danoReal, self.displayDanoReal)
                    self.setDisplay(self.bot.hp, self.displayLifeBOT)
                    self.setDisplay(self.player.mana, self.displayManaPlayer)
            else:
                # DEFESA NAO EFETIVA
                self.setCanvasStatus(2)
                self.setCanvasDICA(attack)

                # DADOS JOGÁVEIS
                danos = System.calculeteDamage(attack)
                danoReal = danos[0] + danos[1]
                self.bot.sufferDamage(danoReal)
                self.player.userMana(attack.mana)
                manaRestore = self.player.restoreMana(danoReal)

                # DADOS ARMAZENÁVEIS
                self.damageFisico += danos[0]
                self.damageMagico += danos[1]
                self.CONTAttack += 1
                self.CONTAttackCriticos += 1
                self.manaGasta += attack.mana
                self.manaRestaurada += manaRestore

                if self.verificarGame():
                    self.root.destroy()
                else:
                    # SET DISPLAY DADOS
                    self.setDisplay(danoReal, self.displayDanoReal)
                    self.setDisplay(self.bot.hp, self.displayLifeBOT)
                    self.setDisplay(self.player.mana, self.displayManaPlayer)
        else:
            # ATAQUE NAO EFETIVO
            self.setCanvasStatus(0)
            self.setCanvasDICA(attack)

            # DADOS ARMAZENÁVEIS
            self.CONTAttack += 1
            self.CONTAttackFalhos += 1

            if self.verificarGame():
                self.root.destroy()
            else:
                # SET DISPLAY DADOS
                self.setDisplay(0, self.displayDanoReal)

    def construtor(self):
        self.root.geometry("1500x780+12+0")
        self.root["bg"] = "Black"
        self.lbPlAYER.place(x=self.xDisplayManaPlayer+50, y=20)
        self.lbBtBOT.place(x=self.xDisplayManaBOT+50, y=20)
        self.lbBtBOT["command"] = self.ActionBOT

        self.nomePlAYER.place(x=self.xDisplayManaPlayer, y=200)
        self.nomeBOT.place(x=self.xDisplayManaBOT, y=200)

        self.swordPlAYER.place(x=self.xDisplayManaPlayer, y=270)
        self.swordBOT.place(x=self.xDisplayManaBOT, y=270)

        self.shieldPlayer.place(x=self.xDisplayManaPlayer, y=340)
        self.shieldBOT.place(x=self.xDisplayManaBOT, y=340)

        recuo = 20
        #Display LIFE PLAYER
        for j in range(len(self.displayLifePlayer)):
            self.displayLifePlayer[j].config(bg="Black")
            self.displayLifePlayer[j].place(x=j*50+self.xDisplayLifiPlayer-recuo, y=self.yDisplayLifi+60)
        self.lbLifePlayer.place(x=self.xDisplayLifiPlayer, y=self.yDisplayLifi)

        for j in range(len(self.displayManaPlayer)):
            self.displayManaPlayer[j].config(bg="Black")
            self.displayManaPlayer[j].place(x=j*50+self.xDisplayManaPlayer-recuo, y=self.yDisplayMana+60)
        self.lbManaPlayer.place(x=self.xDisplayManaPlayer, y=self.yDisplayMana)

        # Display LIFE BOT
        for j in range(len(self.displayLifeBOT)):
            self.displayLifeBOT[j].config(bg="Black")
            self.displayLifeBOT[j].place(x=j*50+self.xDisplayLifiBOT-recuo, y=self.yDisplayLifi+60)
        self.lbLifeBOT.place(x=self.xDisplayLifiBOT, y=self.yDisplayLifi)

        for j in range(len(self.displayManaBOT)):
            self.displayManaBOT[j].config(bg="Black")
            self.displayManaBOT[j].place(x=j*50+self.xDisplayManaBOT-recuo, y=self.yDisplayMana+60)
        self.lbManaBOT.place(x=self.xDisplayManaBOT, y=self.yDisplayMana)

        # DISPLAY DL
        for j in range(len(self.displayDanoReal)):
            self.displayDanoReal[j].config(bg="Black")
            self.displayDanoReal[j].place(x=j*50+self.xMargeDisplayDL, y=self.yMargeDisplayDL)

        self.displayLatencia[0].config(bg="Black")
        self.displayLatencia[0].place(x=self.xMargeDisplayDL, y=self.yMargeDisplayDL+70)

        self.lbDanoReal.place(x=self.xMargeLabelDL, y=self.yMargeDisplayDL)
        self.lbLatencia.place(x=self.xMargeLabelDL, y=self.yMargeDisplayDL+70)

        self.canvasAttk.pack(side=BOTTOM, anchor=S)
        self.canvasAttk.config(bg="black")

        attacksPlayer = self.player.sword.getAttack()
        for bt in range(len(self.BTSCommands)):
            if bt < 3:
                self.BTSCommands[bt].place(x=bt*185, y=0)
                self.BTSCommands[bt]["command"] = partial(self.knock, attacksPlayer[bt])
            else:
                self.BTSCommands[bt].place(x=bt * 185, y=0)
                self.BTSCommands[bt]["command"] = self.defensiveMode

        self.canvasStatus.pack(side=TOP, anchor=N)
        self.canvasAttackDica.pack(side=TOP, anchor=CENTER)
        self.setCanvasStatus(1)

        self.setDisplay(str(0), self.displayLatencia)
        self.setDisplay(str(0), self.displayDanoReal)
        self.setDisplay(str(self.player.hp), self.displayLifePlayer)
        self.setDisplay(str(self.bot.hp), self.displayLifeBOT)
        self.setDisplay(str(self.player.mana), self.displayManaBOT)
        self.setDisplay(str(self.bot.mana), self.displayManaPlayer)

        self.root.mainloop()


TelaInicio().construtor()