from tkinter import font
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
            #TESTE
            self.p1.inventory = System.filterItens()[0:3]
            self.lb["image"] = self.imagemLabelBOT
        elif self.BOT is None:
            player.PlayWAVShow()
            self.BOT = player
            #Alter essa parte do código quando CRIAR A TELA MAIN
            print(self.p1.name, self.BOT.name)
            self.root.destroy()
            TelaItens(self.p1, self.BOT).construtor()

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
        #self.bt2.place(x=self.x+self.margeX, y=self.y+self.margeY)
        self.bt1["command"] = self.abrirTelaEscolhaPlayerBOT
        self.bt2["command"] = self.abrirTelaEscolhaPlayer
        self.root.mainloop()


class TelaMain:
    def __init__(self, player, bot):
        self.root = Tk()

        #Alternar Ataques
        self.Alternar = True
        # PLAYER
        self.player = player
        self.bot = bot

        #CRIAR A UMA INSTÂNCIA DA INTALIGÊNCIA BOT
        self.intelBOT = InteligencePlayer(self.bot, 200)
        self.intelBOT.gerarRanckAttack(self.player)

        # DADOS PLAYER
        self.damageTotal = 0
        self.damageMagico = 0
        self.damageFisico = 0
        self.CONTAttackFalhos = 0
        self.CONTAttackCriticos = 0
        self.CONTAttackNormais = 0
        self.CONTAttack = 0
        self.FalhaDefesa = 0
        self.damageMagicoSofrido = 0
        self.damageFisicoSofrido = 0
        self.damageMagicoDefendido = 0
        self.damageFisicoDefendido = 0
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
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/ataqueFalhou.png")
        self.imageStatusEfetivo = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/ataqueEfetivo.png")
        self.imageStatusCritico = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/critico.png")
        self.imageStatusModoDef = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/modeDEFF.png")
        self.imageStatusHome = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/bemVindo.png")
        self.imageStatusManaAlerta = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/manaAlerta.png")
        self.imageStatusErro = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/ERRO.png")


        self.canvasStatus = Canvas(self.root, width=725, height=200, highlightbackground="Black")

        #CANVAS ATTACK DICA
        self.canvasAttackDica = Canvas(self.root, width=725, height=200, highlightbackground="Black")
        self.fontFixedsys = font.Font(family='Fixedsys', size=15, weight='bold')
        font.families()
        self.lbDica = Label(self.canvasAttackDica, font=self.fontFixedsys, foreground="white", bg="black")
        self.lbDica.pack(side=TOP, anchor=CENTER)

        #CONFIG DISPLAY
        self.yDisplayLifi = 465
        self.xDisplayLifiPlayer = 50
        self.xDisplayLifiBOT = 1250

        self.yDisplayMana = 585
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
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/latenciaATTK.png"
        )
        self.imgLatenciaDEF = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/latenciaDEF.png"
        )
        self.imgDanoReal = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/danoReal.png"
        )

        #LABEL DANO, LATÊNCIA
        self.lbLatencia = Label(self.root, width=200, height=60, bg="Black", highlightbackground="Black",
                                image=self.imgLatencia)
        self.lbLatenciaDef = Label(self.root, width=200, height=60, bg="Black", highlightbackground="Black",
                                image=self.imgLatenciaDEF)
        self.lbDanoReal = Label(self.root, width=200, height=60, bg="Black", highlightbackground="Black",
                                image=self.imgDanoReal)

        # DISPLAY DANO
        self.c21 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c22 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c23 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c24 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoReal = [self.c21, self.c22, self.c23, self.c24]

        # DISPLAY LATENCIA
        self.c25 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayLatencia = [self.c25]
        self.c26 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayLatenciaDef = [self.c26]

        #BOTÕES DE ATTACK
        self.canvasAttk = Canvas(self.root, width=725, height=170, highlightbackground="Black")
        self.imageATTK1 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/atk1.png")
        self.imageATTK2 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/atk2.png")
        self.imageATTK3 = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/atk3.png")
        self.imageDEF = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/deff.png")
        self.btAttk1 = Button(self.canvasAttk, width=175, height=160, image= self.imageATTK1, bg='Black',
                              highlightbackground="Black")
        self.btAttk2 = Button(self.canvasAttk, width=175, height=160, image=self.imageATTK2, bg='Black',
                              highlightbackground="Black")
        self.btAttk3 = Button(self.canvasAttk, width=175, height=160, image=self.imageATTK3, bg='Black',
                              highlightbackground="Black")
        self.btdef1 = Button(self.canvasAttk, width=175, height=160, image=self.imageDEF, bg='Black',
                             highlightbackground="Black")
        self.BTSCommands = [self.btAttk1, self.btAttk2, self.btAttk3, self.btdef1]

        #TEXTOS DE DICAS
        self.stringMODODEF = '''Você pode manter modo defensivo
e recuperar mana para relaizar um ATTACK 
ainda mais forte'''
        self.stringRandLantDEF = '''Esse é o random de DEFESA.
Ele presenta o dado lançado para definir a 
falha ou a efetividade do bloqueio da 
armadura
        '''
        self.stringRandLantATK = '''Esse é o random de ATTACK.
Ele presenta o dado lançado para 
definir a falha ou a efetividade 
do ATTACK escolhido
                '''
        self.stringDanoReal = '''Valor de DANO VERDADEIRO
(Dano Mágico - Amadura Mágica) + (Dano Físico - Armadura Físico)'''

    def ActionBOT(self):
        if not self.Alternar:
            attacksBOT = self.bot.sword.getAttack()
            value = self.intelBOT.resolverAttack(self.player)

            if value == 3:
                self.setCanvasStatus(4)
                self.bot.restoreMana(0)

                # SET DISPLAY DADOS
                self.setDisplay(self.bot.mana, self.displayManaBOT)
                self.setDisplay(0, self.displayDanoReal)
                self.setDisplay(0, self.displayLatencia)
            else:
                attackBOT = attacksBOT[value]
                self.lbDica["text"] = attackBOT.name


                # o numero randomico para a latencia
                randomLatenciaAtaque = randint(0, 9)
                self.setDisplay(randomLatenciaAtaque, self.displayLatencia)

                randomLatenciaDefesa = randint(0, 9)
                self.setDisplay(randomLatenciaDefesa, self.displayLatenciaDef)

                newLatATTK, newLatDEF = randomLatenciaAtaque, randomLatenciaDefesa
                for item in self.player.inventory:
                    if item.ended():
                        newLatATTK, newLatDEF = item.aplicarItem(self.bot, attackBOT, newLatATTK, newLatDEF)
                        print(item.getDados())

                if attackBOT.latencia <= newLatATTK:
                    # ATAQUE EFETIVO
                    if self.player.shield.latencia <= newLatDEF:
                        # DEFESA EFETIVA
                        self.setCanvasStatus(1)

                        # DADOS JOGÁVEIS
                        danos = System.calculeteDamageShield(self.player, attackBOT)
                        danoReal = danos[0] + danos[1]
                        self.player.sufferDamage(danoReal)
                        self.bot.userMana(attackBOT.mana)
                        self.bot.restoreMana(danoReal)

                        # DADOS ARMAZENÁVEIS
                        self.damageFisicoSofrido += danos[0]
                        self.damageMagicoSofrido += danos[1]
                        self.damageMagicoDefendido += attackBOT.danoMagico - danos[1]
                        self.damageFisicoDefendido += attackBOT.danoFisico - danos[0]

                        StatusGame = self.verificarGame()
                        if any(StatusGame):
                            self.abrirTelaOption(all(StatusGame))
                        else:
                            # SET DISPLAY DADOS
                            self.setDisplay(danoReal, self.displayDanoReal)
                            self.setDisplay(self.player.hp, self.displayLifePlayer)
                            if self.bot.mana < 0:
                                self.bot.mana = 0
                                self.setDisplay(self.bot.mana, self.displayManaBOT)
                            else:
                                self.setDisplay(self.bot.mana, self.displayManaBOT)
                    else:
                        # DEFESA NAO EFETIVA
                        self.setCanvasStatus(2)

                        # DADOS JOGÁVEIS
                        danos = System.calculeteDamage(attackBOT)
                        danoReal = danos[0] + danos[1]
                        self.player.sufferDamage(danoReal)
                        self.bot.userMana(attackBOT.mana)
                        self.bot.restoreMana(danoReal)

                        # DADOS ARMAZENÁVEIS
                        self.damageFisicoSofrido += danos[0]
                        self.damageMagicoSofrido += danos[1]
                        self.FalhaDefesa += 1

                        StatusGame = self.verificarGame()
                        if any(StatusGame):
                            self.abrirTelaOption(all(StatusGame))
                        else:
                            # SET DISPLAY DADOS
                            self.setDisplay(danoReal, self.displayDanoReal)
                            self.setDisplay(self.player.hp, self.displayLifePlayer)
                            if self.bot.mana < 0:
                                self.bot.mana = 0
                                self.setDisplay(self.bot.mana, self.displayManaBOT)
                            else:
                                self.setDisplay(self.bot.mana, self.displayManaBOT)
                else:
                    # ATAQUE NAO EFETIVO
                    self.setCanvasStatus(0)

                    StatusGame = self.verificarGame()
                    if any(StatusGame):
                        self.abrirTelaOption(all(StatusGame))
                    else:
                        # SET DISPLAY DADOS
                        self.setDisplay(0, self.displayDanoReal)
            self.Alternar = True
        else:
            self.lbDica["text"] = '''ERRO - É a sua vez de atacar! Escolha o seu ATTACK'''
            self.setCanvasStatus(-2)

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
        :param status: -2 - erro; -1 - bem-vindo; 0 - falhou ;1 - efetivo; 2 - crítico; 3 - Mana insuficiente
        :return: Void
        '''
        self.canvasStatus.delete("all")
        if status == -2:
            self.canvasStatus.create_image(365, 100, image=self.imageStatusErro)
            self.canvasStatus.image = self.imageStatusErro
        elif status == -1:
            self.canvasStatus.create_image(365, 100, image=self.imageStatusHome)
            self.canvasStatus.image = self.imageStatusHome
        elif status == 0:
            self.canvasStatus.create_image(365, 100, image=self.imageStatusFalhou)
            self.canvasStatus.image = self.imageStatusFalhou
        elif status == 1:
            self.canvasStatus.create_image(365, 100, image=self.imageStatusEfetivo)
            self.canvasStatus.image = self.imageStatusEfetivo
        elif status == 2:
            self.canvasStatus.create_image(365, 100, image=self.imageStatusCritico)
            self.canvasStatus.image = self.imageStatusCritico
        elif status == 3:
            self.canvasStatus.create_image(365, 100, image=self.imageStatusManaAlerta)
            self.canvasStatus.image = self.imageStatusManaAlerta
        elif status == 4:
            self.canvasStatus.create_image(365, 100, image=self.imageStatusModoDef)
            self.canvasStatus.image = self.imageStatusModoDef

    def setCanvasDICAAttack(self,event, attack):
        self.lbDica["text"] = attack.getDados()

    def setCanvasDICASword(self, event):
        self.lbDica["text"] = self.player.sword.getDados()

    def setCanvasDICAShield(self, event):
        self.lbDica["text"] = self.player.shield.getDados()

    def gerarRELATORIO(self):
        return [self.damageTotal, self.damageMagico, self.damageFisico, self.CONTAttackFalhos, self.CONTAttackCriticos,
        self.CONTAttackNormais, self.CONTAttack, self.FalhaDefesa, self.damageMagicoSofrido, self.damageFisicoSofrido,
        self.damageMagicoDefendido, self.damageFisicoDefendido, self.manaRestaurada, self.manaGasta]

    def verificarGame(self):
        if self.player.hp <= 0:
            print(f'''
                        VOCÊ PERDEU!1
                    {self.player.name} x {self.bot.name}
                    Dano Total : {self.damageTotal}
                    Dano Mágico : {self.damageMagico}
                    Dano Físico : {self.damageFisico}
                    Attacks Falhos : {self.CONTAttackFalhos} 
                    Attacks Críticos : {self.CONTAttackCriticos}
                    Attacks Normais : {self.CONTAttackNormais}
                    Total Attacks : {self.CONTAttack}
                    Falaha Da Armadura : {self.FalhaDefesa}
                    Dano Mágico Sofrido : {self.damageMagicoSofrido}
                    Dano Físico Sofrido : {self.damageFisicoSofrido}
                    Dado Mágico Defendido : {self.damageMagicoDefendido}
                    Dano Físico Defendido : {self.damageFisicoDefendido}
                    Mana Restaurada : {self.manaRestaurada}
                    Mana Gasta : {self.manaGasta}
                        ''')
            # index 1 : se o jogo acabou ou não
            # index 2 : se o ele venceu ou não
            return [True, False]
        if self.bot.hp <= 0:
            print(f'''
                        VOCÊ GANHOU!!1
                    {self.player.name} x {self.bot.name}
                    Dano Total : {self.damageTotal}
                    Dano Mágico : {self.damageMagico}
                    Dano Físico : {self.damageFisico}
                    Attacks Falhos : {self.CONTAttackFalhos} 
                    Attacks Críticos : {self.CONTAttackCriticos}
                    Attacks Normais : {self.CONTAttackNormais}
                    Total Attacks : {self.CONTAttack}
                    Falaha Da Armadura : {self.FalhaDefesa}
                    Dano Mágico Sofrido : {self.damageMagicoSofrido}
                    Dano Físico Sofrido : {self.damageFisicoSofrido}
                    Dado Mágico Defendido : {self.damageMagicoDefendido}
                    Dano Físico Defendido : {self.damageFisicoDefendido}
                    Mana Restaurada : {self.manaRestaurada}
                    Mana Gasta : {self.manaGasta}
                        ''')
            return [True , True]
        return [False, False]

    def defensiveMode(self):
        if self.Alternar:
            self.setCanvasStatus(4)
            manaRestore = self.player.restoreMana(0)
            self.lbDica["text"] = f"+{manaRestore}"

            #SET DISPLAY DADOS
            self.setDisplay(self.player.mana, self.displayManaPlayer)
            self.setDisplay(0, self.displayDanoReal)
            self.setDisplay(0, self.displayLatencia)

            # DADOS ARMAZENÁVEIS
            self.manaRestaurada += manaRestore
            self.Alternar = False
        else:
            self.lbDica["text"] = '''ERRO - Sua vez foi alternada, Click no Icon do BOT
           para ele realizar o ATTACK'''
            self.setCanvasStatus(-2)

    def abrirTelaOption(self, status):
        self.root.destroy()
        TelaOption(self.player, self.gerarRELATORIO(), status).construtor()

    def knock(self, attack):
        if self.Alternar:
            self.lbDica["text"] = attack.name
            # o numero randomico para a latencia
            randomLatenciaAtaque = randint(0, 9)
            self.setDisplay(randomLatenciaAtaque, self.displayLatencia)

            randomLatenciaDefesa = randint(0, 9)
            self.setDisplay(randomLatenciaDefesa, self.displayLatenciaDef)

            newLatATTK, newLatDEF = randomLatenciaAtaque, randomLatenciaDefesa
            for item in self.player.inventory:
                if item.ended():
                    newLatATTK, newLatDEF = item.aplicarItem(self.player, attack, newLatATTK, newLatDEF)
                    print(item.getDados())

            if attack.latencia <= newLatATTK:
                if self.player.mana <= attack.mana:
                    self.setCanvasStatus(3)
                else:
                    # ATAQUE EFETIVO
                    if self.bot.shield.latencia <= newLatDEF:
                        # DEFESA EFETIVA
                        self.setCanvasStatus(1)

                        #DADOS JOGÁVEIS
                        danos = System.calculeteDamageShield(self.bot, attack)
                        danoReal = danos[0] + danos[1]
                        self.bot.sufferDamage(danoReal)
                        self.player.userMana(attack.mana)
                        manaRestore = self.player.restoreMana(danoReal)

                        # DADOS ARMAZENÁVEIS
                        self.damageTotal += danoReal
                        self.damageFisico += danos[0]
                        self.damageMagico += danos[1]
                        self.CONTAttack += 1
                        self.CONTAttackNormais += 1
                        self.manaGasta += attack.mana
                        self.manaRestaurada += manaRestore

                        StatusGame = self.verificarGame()
                        if any(StatusGame):
                            self.abrirTelaOption(all(StatusGame))
                        else:
                            #SET DISPLAY DADOS
                            self.setDisplay(danoReal, self.displayDanoReal)
                            self.setDisplay(self.bot.hp, self.displayLifeBOT)
                            if self.player.mana < 0:
                                self.player.mana = 0
                                self.setDisplay(self.player.mana, self.displayManaPlayer)
                            else:
                                self.setDisplay(self.player.mana, self.displayManaPlayer)
                    else:
                        # DEFESA NAO EFETIVA
                        self.setCanvasStatus(2)

                        # DADOS JOGÁVEIS
                        danos = System.calculeteDamage(attack)
                        danoReal = danos[0] + danos[1]
                        self.bot.sufferDamage(danoReal)
                        self.player.userMana(attack.mana)
                        manaRestore = self.player.restoreMana(danoReal)

                        # DADOS ARMAZENÁVEIS
                        self.damageTotal += danoReal
                        self.damageFisico += danos[0]
                        self.damageMagico += danos[1]
                        self.CONTAttack += 1
                        self.CONTAttackCriticos += 1
                        self.manaGasta += attack.mana
                        self.manaRestaurada += manaRestore

                        StatusGame = self.verificarGame()
                        if any(StatusGame):
                            self.abrirTelaOption(all(StatusGame))
                        else:
                            # SET DISPLAY DADOS
                            self.setDisplay(danoReal, self.displayDanoReal)
                            self.setDisplay(self.bot.hp, self.displayLifeBOT)
                            if self.player.mana < 0:
                                self.player.mana = 0
                                self.setDisplay(self.player.mana, self.displayManaPlayer)
                            else:
                                self.setDisplay(self.player.mana, self.displayManaPlayer)
            else:
                # ATAQUE NAO EFETIVO
                self.setCanvasStatus(0)

                # DADOS ARMAZENÁVEIS
                self.CONTAttack += 1
                self.CONTAttackFalhos += 1

                StatusGame = self.verificarGame()
                if any(StatusGame):
                    self.abrirTelaOption(all(StatusGame))
                else:
                    # SET DISPLAY DADOS
                    self.setDisplay(0, self.displayDanoReal)
            self.Alternar = False
        else:
            self.lbDica["text"] = '''ERRO - Sua vez foi alternada, Click no Icon do BOT
    para ele realizar o ATTACK'''
            self.setCanvasStatus(-2)

    def limparCanvasDica(self,event):
        self.lbDica["text"] = ""

    def escreverNoCanvasDica(self, event, txt):
        self.lbDica["text"] = txt

    def construtor(self):
        self.root.geometry("1500x780+12+0")
        self.root["bg"] = "Black"
        self.lbPlAYER.place(x=self.xDisplayManaPlayer+50, y=20)
        self.lbBtBOT.place(x=self.xDisplayManaBOT+50, y=20)
        self.lbBtBOT["command"] = self.ActionBOT

        self.nomePlAYER.place(x=self.xDisplayManaPlayer, y=180)
        self.nomeBOT.place(x=self.xDisplayManaBOT, y=180)

        self.swordPlAYER.place(x=self.xDisplayManaPlayer, y=250)
        self.swordPlAYER.bind("<Enter>", self.setCanvasDICASword)
        self.swordPlAYER.bind("<Leave>", self.limparCanvasDica)

        self.swordBOT.place(x=self.xDisplayManaBOT, y=250)

        self.shieldPlayer.place(x=self.xDisplayManaPlayer, y=320)
        self.shieldPlayer.bind("<Enter>", self.setCanvasDICAShield)
        self.shieldPlayer.bind("<Leave>", self.limparCanvasDica)

        self.shieldBOT.place(x=self.xDisplayManaBOT, y=320)

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
        self.displayLatencia[0].place(x=self.xMargeDisplayDL-100, y=self.yMargeDisplayDL+70)

        self.displayLatenciaDef[0].config(bg="Black")
        self.displayLatenciaDef[0].place(x=self.xMargeDisplayDL + 230, y=self.yMargeDisplayDL + 70)

        self.lbDanoReal.place(x=self.xMargeLabelDL, y=self.yMargeDisplayDL)
        self.lbDanoReal.bind("<Enter>",
                             lambda event, txt=self.stringDanoReal: self.escreverNoCanvasDica(event, txt))
        self.lbDanoReal.bind("<Leave>", self.limparCanvasDica)

        self.lbLatencia.place(x=self.xMargeLabelDL-100, y=self.yMargeDisplayDL+70)
        self.lbLatencia.bind("<Enter>",
                                lambda event, txt=self.stringRandLantATK: self.escreverNoCanvasDica(event, txt))
        self.lbLatencia.bind("<Leave>", self.limparCanvasDica)

        self.lbLatenciaDef.place(x=self.xMargeLabelDL + 230, y=self.yMargeDisplayDL + 70)
        self.lbLatenciaDef.bind("<Enter>",
                                  lambda event, txt=self.stringRandLantDEF: self.escreverNoCanvasDica(event, txt))
        self.lbLatenciaDef.bind("<Leave>", self.limparCanvasDica)

        self.canvasAttk.pack(side=BOTTOM, anchor=S)
        self.canvasAttk.config(bg="black")

        attacksPlayer = self.player.sword.getAttack()
        for bt in range(len(self.BTSCommands)):
            if bt < 3:
                self.BTSCommands[bt].place(x=bt*185, y=0)
                self.BTSCommands[bt]["command"] = partial(self.knock, attacksPlayer[bt])
                self.BTSCommands[bt].bind("<Enter>",
                                          lambda event, atk=attacksPlayer[bt]: self.setCanvasDICAAttack(event, atk))
                self.BTSCommands[bt].bind("<Leave>", self.limparCanvasDica)
            else:
                self.BTSCommands[bt].place(x=bt * 185, y=0)
                self.BTSCommands[bt]["command"] = self.defensiveMode
                self.BTSCommands[bt].bind("<Enter>",
                                          lambda event, txt=self.stringMODODEF: self.escreverNoCanvasDica(event, txt))
                self.BTSCommands[bt].bind("<Leave>", self.limparCanvasDica)

        self.canvasStatus.pack(side=TOP, anchor=N)
        self.canvasStatus.config(bg="Black")
        self.canvasAttackDica.pack(side=TOP, anchor=CENTER)
        self.canvasAttackDica.config(bg="Black")
        self.setCanvasStatus(-1)

        self.setDisplay(str(0), self.displayLatencia)
        self.setDisplay(str(0), self.displayLatenciaDef)
        self.setDisplay(str(0), self.displayDanoReal)
        self.setDisplay(str(self.player.hp), self.displayLifePlayer)
        self.setDisplay(str(self.bot.hp), self.displayLifeBOT)
        self.setDisplay(str(self.player.mana), self.displayManaPlayer)
        self.setDisplay(str(self.bot.mana), self.displayManaBOT)

        self.root.mainloop()


class TelaOption:
    def __init__(self, player, dadosDaPatida, status=True ):
        self.root = Tk()

        self.player = player
        self.dadosDaPatida = dadosDaPatida

        self.margeX = 0
        self.margeY = 150
        self.x = 265
        self.y = 200
        self.color = "Black"

        self.imagemRelatorio = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/relatorio.png")

        self.imagemContinue = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/OutroDesafio.png")

        self.imagemVitoria = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/vitoria.png")
        self.imagemDerrota = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/derrota.png")

        self.bt1 = Button(self.root, image=self.imagemRelatorio)
        self.bt2 = Button(self.root, image=self.imagemContinue)
        if status:
            self.lb = Label(self.root, image=self.imagemVitoria)
        else:
            self.lb = Label(self.root, image=self.imagemDerrota)

    def abrirRelatorio(self):
        self.root.destroy()
        TelaRelatorio(self.dadosDaPatida).construtor()

    def abrirChoosePlayer(self):

        self.root.destroy()
        t = TelaEscolhaBot()
        t.p1 = System.choosePlayer(System.listPlayer().index(self.player.name))
        t.lb["image"] = t.imagemLabelBOT
        t.construtor()

    def construtor(self):
        self.root.geometry("800x500+300+100")
        self.root["bg"] = self.color
        self.lb["bg"] = self.color
        self.lb.pack(side=TOP)
        self.bt1.place(x=self.x, y=self.y)
        self.bt2.place(x=self.x+self.margeX, y=self.y+self.margeY)
        self.bt1["command"] = self.abrirRelatorio
        self.bt2["command"] = self.abrirChoosePlayer
        self.root.mainloop()


class TelaRelatorio:
    def __init__(self, dadosDaPartida):
        self.root = Tk()

        self.dadosDaPartida = dadosDaPartida

        self.imageLBTitulo = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/relatorioTitulo.png")
        self.lbTitulo = Label(self.root, image=self.imageLBTitulo, highlightbackground="Black", bg="Black")

        #IMAGENS
        self.imageLBDanoTotal = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/danoTotal.png")
        self.imageLBDanoMagico = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/dmagico.png")
        self.imageLBDanoFisico = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/dfisico.png")
        self.imageLBAttacksFalhos = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/atkfalhos.png")
        self.imageLBAttacksCriticos = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/atkcritico.png")
        self.imageLBAttacksNormais = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/atknormal.png")
        self.imageLBTotalAttacks = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/ttAtk.png")
        self.imageLBFalhaDaArmadura = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/falhaArmadura.png")
        self.imageLBDanoMagicoSofrido = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/dmSofrido.png")
        self.imageLBDanoFisicoSofrido = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/dfSofrido.png")
        self.imageLBDanoMagicoDefendido = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/dmDef.png")
        self.imageLBDanoFisicoDefendido = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/dfDef.png")
        self.imageLBManaRestaurada = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/manaRest.png")
        self.imageLBManaGasta = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/LBTelaRelatorio/manaUsa.png")

        #LABEL
        self.LBDanoTotal = Label(self.root, image=self.imageLBDanoTotal, width=200, height=60)
        self.LBDanoMagico = Label(self.root, image=self.imageLBDanoMagico, width=200, height=60)
        self.LBDanoFisico = Label(self.root, image=self.imageLBDanoFisico, width=200, height=60)
        self.LBAttacksFalhos = Label(self.root, image=self.imageLBAttacksFalhos, width=200, height=60)
        self.LBAttacksCriticos = Label(self.root, image=self.imageLBAttacksCriticos, width=200, height=60)
        self.LBAttacksNormais = Label(self.root, image=self.imageLBAttacksNormais, width=200, height=60)
        self.LBTotalAttacks = Label(self.root, image=self.imageLBTotalAttacks, width=200, height=60)
        self.LBFalhaDaArmadura = Label(self.root, image=self.imageLBFalhaDaArmadura, width=200, height=60)
        self.LBDanoMagicoSofrido = Label(self.root, image=self.imageLBDanoMagicoSofrido, width=200, height=60)
        self.LBDanoFisicoSofrido = Label(self.root, image=self.imageLBDanoFisicoSofrido, width=200, height=60)
        self.LBDanoMagicoDefendido = Label(self.root, image=self.imageLBDanoMagicoDefendido, width=200, height=60)
        self.LBDanoFisicoDefendido = Label(self.root, image=self.imageLBDanoFisicoDefendido, width=200, height=60)
        self.LBManaRestaurada = Label(self.root, image=self.imageLBManaRestaurada, width=200, height=60)
        self.LBManaGasta = Label(self.root, image=self.imageLBManaGasta, width=200, height=60)

        #CONFIG LABEL
        self.xLabel = 500
        self.yLabel = 125
        self.xMargerLabel = 20
        self.yMargerLabel = 150

        self.labels = [[self.LBDanoTotal, self.LBDanoMagico, self.LBDanoFisico, self.LBAttacksFalhos,
                       self.LBAttacksCriticos], [self.LBAttacksNormais, self.LBTotalAttacks, self.LBFalhaDaArmadura,
                       self.LBDanoMagicoSofrido, self.LBDanoFisicoSofrido], [self.LBDanoMagicoDefendido,
                       self.LBDanoFisicoDefendido, self.LBManaRestaurada, self.LBManaGasta]]

        # DISPLAY
        self.c1 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c2 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c3 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c4 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c5 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoTotal = [self.c1, self.c2, self.c3, self.c4, self.c5]

        self.c6 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c7 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c8 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c9 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c10 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoMagico = [self.c6, self.c7, self.c8, self.c9, self.c10]

        self.c11 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c12 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c13 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c14 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c15 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoFisico = [self.c11, self.c12, self.c13, self.c14, self.c15]

        self.c16 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c17 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c18 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c19 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c20 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayAttacksFalhos = [self.c16, self.c17, self.c18, self.c19, self.c20]

        self.c21 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c22 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c23 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c24 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c25 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayAttacksCriticos = [self.c21, self.c22, self.c23, self.c24, self.c25]

        self.c26 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c27 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c28 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c29 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c30 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayAttacksNormais = [self.c26, self.c27, self.c28, self.c29, self.c30]

        self.c31 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c32 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c33 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c34 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c35 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayTotalAttacks = [self.c31, self.c32, self.c33, self.c34, self.c35]

        self.c36 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c37 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c38 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c39 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c40 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayFalhaDaArmadura = [self.c36, self.c37, self.c38, self.c39, self.c40]

        self.c41 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c42 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c43 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c44 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c45 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoMagicoSofrido = [self.c41, self.c42, self.c43, self.c44, self.c45]

        self.c46 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c47 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c48 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c49 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c50 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoFisicoSofrido = [self.c46, self.c47, self.c48, self.c49, self.c50]

        self.c51 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c52 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c53 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c54 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c55 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoMagicoDefendido = [self.c51, self.c52, self.c53, self.c54, self.c55]

        self.c56 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c57 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c58 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c59 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c60 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayDanoFisicoDefendido = [self.c56, self.c57, self.c58, self.c59, self.c60]

        self.c61 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c62 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c63 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c64 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c65 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayManaRestaurada = [self.c61, self.c62, self.c63, self.c64, self.c65]

        self.c66 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c67 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c68 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c69 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.c70 = Canvas(self.root, width=60, height=60, highlightbackground="Black")
        self.displayManaGasta = [self.c66, self.c67, self.c68, self.c69, self.c70]

        self.displays = [[self.displayDanoTotal, self.displayDanoMagico, self.displayDanoFisico,
                         self.displayAttacksFalhos, self.displayAttacksCriticos], [self.displayAttacksNormais,
                         self.displayTotalAttacks, self.displayFalhaDaArmadura,
                         self.displayDanoMagicoSofrido, self.displayDanoFisicoSofrido],
                         [self.displayDanoMagicoDefendido, self.displayDanoFisicoDefendido,
                         self.displayManaRestaurada, self.displayManaGasta]]
        self.backPNG = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/backPNG.png")
        self.btVolta = Button(self.root, image=self.backPNG, bg="Black")

    def voltar(self):
        self.root.destroy()
        TelaInicio().construtor()

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
        strNumber = number if len(number) == len(display) else "#" * (len(display) - len(number)) + str(number)
        for elem in range(len(display)):
            imag = dicImagens[strNumber[elem]]
            display[elem].create_image(30, 35, image=imag)
            display[elem].image = imag

    def construtor(self):
        self.root.geometry("1500x780+12+0")
        self.root["bg"] = "Black"
        self.lbTitulo.pack(side=TOP)
        cont = 0
        for lbx in range(len(self.labels)):
            for lby in range(len(self.labels[lbx])):
                x = self.xLabel * lbx + self.xMargerLabel
                y = self.yLabel * lby + self.yMargerLabel
                self.labels[lbx][lby].place(x=x, y=y)
                self.labels[lbx][lby]["bg"] = "Black"
                for j in range(len(self.displays[lbx][lby])):
                    self.displays[lbx][lby][j].config(bg="Black")
                    self.displays[lbx][lby][j].place(x=j * 50 + x + 220, y=y)
                self.setDisplay(self.dadosDaPartida[cont], self.displays[lbx][lby])
                cont += 1
        self.btVolta.pack(side=BOTTOM, anchor=SE)
        self.btVolta["command"] = self.voltar
        self.root.mainloop()


class TelaItens:
    def __init__(self, player, bot):
        self.root = Tk()
        self.listItens = System.filterItens()
        self.player = player
        self.bot = bot
        self.money = 600

        #CONFIG
        self.margeEX_x = 50
        self.margeEX_y = 70
        self.margeIN_x = 340
        self.margeIN_y = 210
        self.fontFixedsys15 = font.Font(family='Fixedsys', size=15, weight='bold')
        self.fontFixedsys25 = font.Font(family='Fixedsys', size=17, weight='bold')

        self.lb = Label(self.root, font=self.fontFixedsys25,  bg="Black", fg="white")

        self.bt1 = Button(self.root, width=25, height=7, bg="Black",
                          fg="white", font=self.fontFixedsys15)
        self.bt2 = Button(self.root, width=25, height=7, bg="Black",
                          fg="white", font=self.fontFixedsys15)
        self.bt3 = Button(self.root, width=25, height=7, bg="Black",
                          fg="white", font=self.fontFixedsys15)
        self.bt4 = Button(self.root, width=25, height=7, bg="Black",
                          fg="white", font=self.fontFixedsys15)
        self.bt5 = Button(self.root, width=25, height=7, bg="Black",
                          fg="white", font=self.fontFixedsys15)
        self.bt6 = Button(self.root, width=25, height=7, bg="Black",
                          fg="white", font=self.fontFixedsys15)

        self.listBt = [[self.bt1, self.bt2, self.bt3], [self.bt4, self.bt5, self.bt6]]

        self.c1 = Canvas(self.root, width=60, height=60, highlightbackground="Black", bg="black")
        self.c2 = Canvas(self.root, width=60, height=60, highlightbackground="Black", bg="black")
        self.c3 = Canvas(self.root, width=60, height=60, highlightbackground="Black", bg="black")
        self.c4 = Canvas(self.root, width=60, height=60, highlightbackground="Black", bg="black")
        self.c5 = Canvas(self.root, width=60, height=60, highlightbackground="Black", bg="black")
        self.displayMoney = [self.c1, self.c2, self.c3, self.c4, self.c5]

        self.image = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/continue.png"
        )

        self.btContinuar = Button(self.root, image=self.image, width=300, height=150)

        self.backPNG = PhotoImage(
            file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/backPNG.png")
        self.btVolta = Button(self.root, image=self.backPNG, bg="Black")

    def voltar(self):
        self.root.destroy()
        TelaEscolhaBot().construtor()

    def dinheiroERRO(self):
        self.lb["text"] = "VOCÊ NÃO POSSUE MOEDAS\nPARA COMPRAR ESSE ITEM"

    def addItem(self, item):
        if self.money >= item.valor:
            self.player.addItem(item)
            self.lb["text"] = f"ITEM {item.name}\nCOMPRADO COM SUCESSO!"
            self.money -= item.valor
            self.setDisplay(str(self.money), self.displayMoney)
        else:
            self.dinheiroERRO()

    def setLABEitem(self, event, item):
        self.lb["text"] = item.getDados()

    def resetarLabelitem(self,event):
        self.lb["text"] = ""

    def abrirTelaMain(self):
        self.root.destroy()
        TelaMain(self.player, self.bot).construtor()

    def setDisplay(self, num, display):
        number = str(num)
        dicImagens = {
            "#": PhotoImage(file="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/DirPNGnumber/#.png"),
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
        strNumber = number if len(number) == len(display) else "#" * (len(display) - len(number)) + str(number)
        for elem in range(len(display)):
            imag = dicImagens[strNumber[elem]]
            display[elem].create_image(30, 35, image=imag)
            display[elem].image = imag

    def construtor(self):
        self.root.geometry("1500x780+20+0")
        self.root["bg"] = "Black"
        self.lb.place(x=1150, y=250)
        self.btContinuar.place(x=380, y=600)
        self.btContinuar["command"] = self.abrirTelaMain
        cont = 0
        for line in range(len(self.listBt)):
            for colunn in range(len(self.listBt[line])):
                self.listBt[line][colunn].place(x=colunn*self.margeIN_x+self.margeEX_x,
                                                y=line*self.margeIN_y+self.margeEX_y)
                self.listBt[line][colunn]["text"] = f'''{self.listItens[cont].name}\n\nx{self.listItens[cont].quatidade}\n{self.listItens[cont].valor}U$'''
                self.listBt[line][colunn].bind("<Enter>",
                                               lambda event, item=self.listItens[cont]: self.setLABEitem(event,item))
                self.listBt[line][colunn].bind("<Leave>", self.resetarLabelitem)
                self.listBt[line][colunn]["command"] = partial(self.addItem, self.listItens[cont])
                cont += 1
        for index in range(len(self.displayMoney)):
            self.displayMoney[index].place(x=70*index+300, y=450)

        self.btVolta.pack(side=BOTTOM, anchor=SW)
        self.btVolta["command"] = self.voltar

        self.setDisplay(str(self.money),self.displayMoney)
        self.root.mainloop()

TelaInicio().construtor()