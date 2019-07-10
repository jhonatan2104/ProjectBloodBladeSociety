from functools import partial
from tkinter import *
from tkinter import font

from fileClass import *


class TelaEscolhaBot:
    def __init__(self):
        self.root = Tk()

        # CONFIG
        self.color = "Black"
        self.btSizeX = 400
        self.btSizeY = 200
        self.margeX = 100
        self.margeY = 200
        self.x = 490
        self.y = 250

        self.p1 = None
        self.BOT = None

        self.imagemLabelBOT = PhotoImage(
            file="DirPNG/ImagemLabelBOT.png")
        self.imagemLabelPlayer = PhotoImage(
            file="DirPNG/ImagemLabelPlayer.png")

        # IMAGENS DOS PLAYER
        self.IchigoKurosakiPNG = PhotoImage(file=System.choosePlayer(0).imageShowChoose)
        self.KillerBeePNG = PhotoImage(file=System.choosePlayer(1).imageShowChoose)
        self.XenaPNG = PhotoImage(file=System.choosePlayer(2).imageShowChoose)
        self.RoronoaZoroPNG = PhotoImage(file=System.choosePlayer(3).imageShowChoose)
        self.GohanPNG = PhotoImage(file=System.choosePlayer(4).imageShowChoose)

        self.backPNG = PhotoImage(file="DirPNG/backPNG.png")
        self.bt1 = Button(self.root, image=self.IchigoKurosakiPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt2 = Button(self.root, image=self.KillerBeePNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt3 = Button(self.root, image=self.XenaPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt4 = Button(self.root, image=self.RoronoaZoroPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt5 = Button(self.root, image=self.GohanPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.lb = Label(self.root, image=self.imagemLabelPlayer, bg=self.color)

        self.btVoltar = Button(self.root, image=self.backPNG, bg="Black")
        self.bts = [[self.bt1, self.bt2, self.bt3], [self.bt4, self.bt5]]

    def choose(self, contCamp):

        # OBJETO Player
        player = System.choosePlayer(contCamp)
        if self.p1 is None:
            # TOCAR ÁUDIO
            player.PlayWAVShow()
            self.p1 = player

            # MUDAR IMAGENS DE TÍTULO
            self.lb["image"] = self.imagemLabelBOT
        elif self.BOT is None:
            # TOCAR ÁUDIO
            player.PlayWAVShow()
            self.BOT = player

            # CHAMAR OUTRA TELA
            self.root.destroy()
            TelaItens(self.p1, self.BOT).construtor()

    def voltar(self):
        self.root.destroy()
        TelaInicio().construtor()

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
        self.root["bg"] = self.color

        # VARIÁVEL AUXILIAR PARA INDEX DO PLAYER { self.choose(contCamp) }
        contCamp = 0

        # GRADEADO DOS BUTTONS
        for line in range(len(self.bts)):
            for column in range(len(self.bts[line])):
                self.bts[line][column]["command"] = partial(self.choose, contCamp)
                contCamp += 1
                self.bts[line][column].place(x=self.x * column + self.margeX, y=self.y * line + self.margeY)

        self.lb.pack(side=TOP)
        self.btVoltar.pack(side=BOTTOM, anchor=SE)
        self.btVoltar["command"] = self.voltar
        self.root.mainloop()


class TelaInicio:
    def __init__(self):
        self.root = Tk()

        # CONFIG
        self.color = "Black"

        self.imagemLabel = PhotoImage(file="DirPNG/bemVindo.png")

        self.imagemPlayerXbot = PhotoImage(file="DirPNG/playerXbotPNG.png")
        self.imageSair = PhotoImage(file="DirPNG/sair.png")
        self.imageTutor = PhotoImage(file="DirPNG/tutorial.png")

        self.bt1 = Button(self.root, image=self.imagemPlayerXbot, border=0, width=400, height=200, relief="groove")
        self.btSair = Button(self.root, image=self.imageSair, border=0, width=400, height=200, relief="groove")
        self.btTutor = Button(self.root, image=self.imageTutor, border=0, width=400, height=200, relief="groove")

        self.lb = Label(self.root, image=self.imagemLabel, bg="Black")

    def abrirTelaEscolhaPlayerBOT(self):
        self.root.destroy()
        TelaEscolhaBot().construtor()

    def sair(self):
        self.root.destroy()
        sys.exit()

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()

        self.root.bind("<Return>", lambda event: self.abrirTelaEscolhaPlayerBOT())
        self.root["bg"] = self.color
        self.lb["bg"] = self.color
        self.lb.pack(side=TOP)
        self.bt1.place(x=555, y=465)
        self.btSair.place(x=125, y=300)
        self.btTutor.place(x=990, y=300)
        self.bt1["command"] = self.abrirTelaEscolhaPlayerBOT
        self.btSair["command"] = self.sair
        self.root.mainloop()


class TelaMain:
    def __init__(self, player, bot, alternar=True, dicDados=None):
        self.root = Tk()

        # Alternar Ataques
        self.Alternar = alternar
        # PLAYER
        self.player = player
        self.bot = bot

        # CRIAR A UMA INSTÂNCIA DA INTALIGÊNCIA BOT
        self.intelBOT = InteligencePlayer(self.bot, self.player, 500,
                                          importanciaDANO=self.bot.personality["importanciaDANO"],
                                          importanciaMANA=self.bot.personality["importanciaMANA"],
                                          importanciaLATENCIA=self.bot.personality["importanciaLATENCIA"],
                                          activeStrategyLatAttk=self.bot.personality["activeStrategyLatAttk"],
                                          activeStrategyMana=self.bot.personality["activeStrategyMana"],
                                          activeStrategyDMC=self.bot.personality["activeStrategyDMC"],
                                          activeStrategyLatDeff=self.bot.personality["activeStrategyLatDeff"])

        # DADOS PLAYER
        if dicDados is None:
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
        else:
            self.damageTotal = dicDados["damageTotal"]
            self.damageMagico = dicDados["damageMagico"]
            self.damageFisico = dicDados["damageFisico"]
            self.CONTAttackFalhos = dicDados["CONTAttackFalhos"]
            self.CONTAttackCriticos = dicDados["CONTAttackCriticos"]
            self.CONTAttackNormais = dicDados["CONTAttackNormais"]
            self.CONTAttack = dicDados["CONTAttack"]
            self.FalhaDefesa = dicDados["FalhaDefesa"]
            self.damageMagicoSofrido = dicDados["damageMagicoSofrido"]
            self.damageFisicoSofrido = dicDados["damageFisicoSofrido"]
            self.damageMagicoDefendido = dicDados["damageMagicoDefendido"]
            self.damageFisicoDefendido = dicDados["damageFisicoDefendido"]
            self.manaRestaurada = dicDados["manaRestaurada"]
            self.manaGasta = dicDados["manaGasta"]

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
        self.lbPlAYER = Label(self.root, image=self.ImageShowPlayer, width=100, height=150, relief="groove")
        self.nomePlAYER = Label(self.root, image=self.ImageIDPlayer, width=200, height=60, bg="Black")
        self.swordPlAYER = Label(self.root, image=self.ImageIDSwordPlayer, width=200, height=60, bg="Black")
        self.shieldPlayer = Label(self.root, image=self.ImageIDShieldPlayer, width=200, height=60, bg="Black")

        # Lb BOT
        self.lbBtBOT = Button(self.root, image=self.ImageShowBOT, width=100, height=150, relief="groove")
        self.nomeBOT = Label(self.root, image=self.ImageIDBOT, width=200, height=60, bg="Black")
        self.swordBOT = Label(self.root, image=self.ImageIDSwordBOT, width=200, height=60, bg="Black")
        self.shieldBOT = Label(self.root, image=self.ImageIDShieldBOT, width=200, height=60, bg="Black")

        self.imageLife1 = PhotoImage(file="DirPNG/life.png")
        self.imageLife2 = PhotoImage(file="DirPNG/life.png")
        self.imageMana1 = PhotoImage(file="DirPNG/mana.png")
        self.imageMana2 = PhotoImage(file="DirPNG/mana.png")

        self.lbLifePlayer = Label(self.root, width=200, height=60, image=self.imageLife1, bg="Black")
        self.lbLifeBOT = Label(self.root, width=200, height=60, image=self.imageLife2, bg="Black")
        self.lbManaPlayer = Label(self.root, width=200, height=60, image=self.imageMana1, bg="Black")
        self.lbManaBOT = Label(self.root, width=200, height=60, image=self.imageMana2, bg="Black")

        # CANVAS STATUS
        self.imageStatusFalhou = PhotoImage(file="DirPNG/ataqueFalhou.png")
        self.imageStatusEfetivo = PhotoImage(file="DirPNG/ataqueEfetivo.png")
        self.imageStatusCritico = PhotoImage(file="DirPNG/critico.png")
        self.imageStatusModoDef = PhotoImage(file="DirPNG/modeDEFF.png")
        self.imageStatusHome = PhotoImage(file="DirPNG/bemVindo.png")
        self.imageStatusManaAlerta = PhotoImage(file="DirPNG/manaAlerta.png")
        self.imageStatusErro = PhotoImage(file="DirPNG/ERRO.png")

        self.canvasStatus = Canvas(self.root, width=725, height=200, highlightbackground="Black")

        # CANVAS ATTACK DICA
        self.canvasAttackDica = Canvas(self.root, width=725, height=200, highlightbackground="Black")
        self.fontFixedsys = font.Font(family='Fixedsys', size=17)
        font.families()
        self.lbDica = Label(self.canvasAttackDica, font=self.fontFixedsys, foreground="white", bg="black")
        self.lbDica.pack(side=TOP, anchor=CENTER)

        # CONFIG DISPLAY
        self.yDisplayLifi = 490
        self.xDisplayLifiPlayer = 50
        self.xDisplayLifiBOT = 1250

        self.yDisplayMana = 635
        self.xDisplayManaPlayer = 50
        self.xDisplayManaBOT = 1250

        # DISPLAY
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

        # IMAGE DANO, LATÊNCIA
        self.imgLatencia = PhotoImage(file="DirPNG/latenciaATTK.png")
        self.imgLatenciaDEF = PhotoImage(file="DirPNG/latenciaDEF.png")
        self.imgDanoReal = PhotoImage(file="DirPNG/danoReal.png")

        # LABEL DANO, LATÊNCIA
        self.lbLatencia = Label(self.root, width=200, height=80, bg="Black", highlightbackground="Black",
                                image=self.imgLatencia)
        self.lbLatenciaDef = Label(self.root, width=200, height=80, bg="Black", highlightbackground="Black",
                                   image=self.imgLatenciaDEF)
        self.lbDanoReal = Label(self.root, width=200, height=80, bg="Black", highlightbackground="Black",
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

        # BOTÕES DE ATTACK
        self.canvasAttk = Canvas(self.root, width=925, height=205, highlightbackground="Black")
        Attacks = self.player.sword.getAttack()
        self.imageATTK1 = PhotoImage(file=Attacks[0].imageBt)
        self.imageATTK2 = PhotoImage(file=Attacks[1].imageBt)
        self.imageATTK3 = PhotoImage(file=Attacks[2].imageBt)
        self.imageDEF = PhotoImage(file="DirPNG/deff.png")
        self.btAttk1 = Button(self.canvasAttk, width=220, height=200, image=self.imageATTK1, bg='Black',
                              highlightbackground="Black")
        self.btAttk2 = Button(self.canvasAttk, width=220, height=200, image=self.imageATTK2, bg='Black',
                              highlightbackground="Black")
        self.btAttk3 = Button(self.canvasAttk, width=220, height=200, image=self.imageATTK3, bg='Black',
                              highlightbackground="Black")
        self.btdef1 = Button(self.canvasAttk, width=220, height=200, image=self.imageDEF, bg='Black',
                             highlightbackground="Black")
        self.BTSCommands = [self.btAttk1, self.btAttk2, self.btAttk3, self.btdef1]
        self.teclasAttkConfig = ["<q>", "<w>", "<e>", "<r>"]
        self.teclasConfig = {
            "Inventário" : "<c>",
            "compraInventário" : "<v>",
            "attkBOT" : "<Return>",
            "attk1-dica" : "<Q>",
            "attk2-dica": "<W>",
            "attk3-dica": "<E>",
            "DadosArmadura": "<k>",
            "DadosEspada": "<j>"
        }

        # TEXTOS DE DICAS
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

    def dadosBot(self, event):
        txt = "INVENTÁRIO\n"
        for item in self.bot.inventory:
            txt += f"{item.name.upper()} x{item.quatidade}\n"
        txt += f"\n{self.bot.money}"
        self.lbDica["text"] = txt

    def alterarBorda(self, vez):
        if vez:
            self.lbPlAYER["border"] = 5
            self.lbBtBOT["border"] = 1
        else:
            self.lbBtBOT["border"] = 5
            self.lbPlAYER["border"] = 1

    def ActionBOT(self):
        if not self.Alternar:
            attacksBOT = self.bot.sword.getAttack()

            self.intelBOT.gerarRanckAttack(self.player)
            value = self.intelBOT.resolverAttack(self.player)

            if value == 3:
                self.setCanvasStatus(4)
                self.limparCanvasDica(None)
                self.bot.restoreMana(0)

                # SET DISPLAY DADOS
                self.setDisplay(self.bot.mana, self.displayManaBOT)
                self.setDisplay(0, self.displayDanoReal)
                self.setDisplay(0, self.displayLatencia)

                self.Alternar = True
                self.alterarBorda(True)
            else:
                attackBOT = attacksBOT[value]
                self.escreverNoCanvasDica(None, f"\n{attackBOT.name}")

                # o numero randomico para a latencia
                randomLatenciaAtaque = randint(0, 9)
                self.setDisplay(randomLatenciaAtaque, self.displayLatencia)

                randomLatenciaDefesa = randint(0, 9)
                self.setDisplay(randomLatenciaDefesa, self.displayLatenciaDef)
                ## COMPRA DE ITEM
                self.intelBOT.buyItems()

                newLatATTK, newLatDEF, textLbDica = randomLatenciaAtaque, randomLatenciaDefesa, "\n"
                for item in self.bot.inventory:
                    if item.ended():
                        info = item.aplicarItem(self.bot, attackBOT, newLatATTK, newLatDEF)
                        newLatATTK, newLatDEF = info[0], info[1]
                        textLbDica += f"\n+ {item.name.upper()}"
                self.escreverNoCanvasDica(None, attackBOT.getDados() + textLbDica, 'red')

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

                        # RESTAURA MONEY
                        self.bot.money += System.calculeteRestareMoney(type="an", dano=danoReal)

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
                            self.setDisplay(self.bot.hp, self.displayLifeBOT)

                            self.Alternar = True
                            self.alterarBorda(True)
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

                        # RESTAURA MONEY
                        self.bot.money += System.calculeteRestareMoney(type="ac", dano=danoReal)

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
                            self.setDisplay(self.bot.hp, self.displayLifeBOT)

                            self.Alternar = True
                            self.alterarBorda(True)

                            if self.bot.mana < 0:
                                self.bot.mana = 0
                                self.setDisplay(self.bot.mana, self.displayManaBOT)
                            else:
                                self.setDisplay(self.bot.mana, self.displayManaBOT)
                else:
                    # ATAQUE NAO EFETIVO
                    self.setCanvasStatus(0)

                    # RESTAURA MONEY
                    self.player.money += System.calculeteRestareMoney(type="f", dano=0)

                    StatusGame = self.verificarGame()
                    if any(StatusGame):
                        self.abrirTelaOption(all(StatusGame))
                    else:
                        # SET DISPLAY DADOS
                        self.setDisplay(0, self.displayDanoReal)
                        self.setDisplay(self.player.hp, self.displayLifePlayer)
                        self.setDisplay(self.bot.hp, self.displayLifeBOT)

                        self.Alternar = True
                        self.alterarBorda(True)

                        if self.bot.mana < 0:
                            self.bot.mana = 0
                            self.setDisplay(self.bot.mana, self.displayManaBOT)
                        else:
                            self.setDisplay(self.bot.mana, self.displayManaBOT)
        else:
            self.lbDica["text"] = '''ERRO - É a sua vez de atacar! Escolha o seu ATTACK'''
            self.setCanvasStatus(-2)

    def setDisplay(self, num, display):
        number = str(num)
        dicImagens = {
            "#": PhotoImage(file="DirPNG/DirPNGnumber/0.png"),
            "0": PhotoImage(file="DirPNG/DirPNGnumber/0.png"),
            "1": PhotoImage(file="DirPNG/DirPNGnumber/1.png"),
            "2": PhotoImage(file="DirPNG/DirPNGnumber/2.png"),
            "3": PhotoImage(file="DirPNG/DirPNGnumber/3.png"),
            "4": PhotoImage(file="DirPNG/DirPNGnumber/4.png"),
            "5": PhotoImage(file="DirPNG/DirPNGnumber/5.png"),
            "6": PhotoImage(file="DirPNG/DirPNGnumber/6.png"),
            "7": PhotoImage(file="DirPNG/DirPNGnumber/7.png"),
            "8": PhotoImage(file="DirPNG/DirPNGnumber/8.png"),
            "9": PhotoImage(file="DirPNG/DirPNGnumber/9.png")
        }
        strNumber = number if len(number) == len(display) else "#" * (len(display) - len(number)) + str(number)
        for elem in range(len(display)):
            imag = dicImagens[strNumber[elem]]
            display[elem].create_image(30, 35, image=imag)
            display[elem].image = imag

    def gerarDic(self):
        return {
            "damageTotal": self.damageTotal,
            "damageMagico": self.damageMagico,
            "damageFisico": self.damageFisico,
            "CONTAttackFalhos": self.CONTAttackFalhos,
            "CONTAttackCriticos": self.CONTAttackCriticos,
            "CONTAttackNormais": self.CONTAttackNormais,
            "CONTAttack": self.CONTAttack,
            "FalhaDefesa": self.FalhaDefesa,
            "damageMagicoSofrido": self.damageMagicoSofrido,
            "damageFisicoSofrido": self.damageFisicoSofrido,
            "damageMagicoDefendido": self.damageMagicoDefendido,
            "damageFisicoDefendido": self.damageFisicoDefendido,
            "manaRestaurada": self.manaRestaurada,
            "manaGasta": self.manaGasta
        }

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

    def setCanvasDICASword(self, event):
        self.lbDica.configure(fg="white")
        self.lbDica["text"] = self.player.sword.getDados()

    def setCanvasDICAShield(self, event):
        self.lbDica.configure(fg="white")
        self.lbDica["text"] = self.player.shield.getDados()

    def setCanvasDICAInventario(self, event):
        txt = "INVENTÁRIO\n"
        for item in self.player.inventory:
            txt += f"{item.name.upper()} x{item.quatidade}\n"
        self.lbDica["text"] = txt

    def gerarRELATORIO(self):
        return [self.damageTotal, self.damageMagico, self.damageFisico, self.CONTAttackFalhos, self.CONTAttackCriticos,
                self.CONTAttackNormais, self.CONTAttack, self.FalhaDefesa, self.damageMagicoSofrido,
                self.damageFisicoSofrido,
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
            return [True, True]
        return [False, False]

    def defensiveMode(self):
        if self.Alternar:
            self.setCanvasStatus(4)
            manaRestore = self.player.restoreMana(0)
            self.lbDica["text"] = f"+{manaRestore}"

            # SET DISPLAY DADOS
            self.setDisplay(self.player.mana if self.player.mana >= 0 else 0, self.displayManaPlayer)
            self.setDisplay(0, self.displayDanoReal)
            self.setDisplay(0, self.displayLatencia)

            # DADOS ARMAZENÁVEIS
            self.manaRestaurada += manaRestore
            self.Alternar = False
            self.alterarBorda(False)
        else:
            self.lbDica["text"] = '''ERRO - Sua vez foi alternada, Click no Icon do BOT
           para ele realizar o ATTACK'''
            self.setCanvasStatus(-2)

    def abrirTelaOption(self, status):
        self.root.destroy()
        TelaOption(self.player, self.gerarRELATORIO(), status).construtor()

    def abrirTelaItens(self, event):
        self.root.destroy()
        TelaItens(self.player, self.bot, self.Alternar, self.gerarDic()).construtor()

    def knock(self, attack):
        if self.Alternar:
            # o numero randomico para a latencia
            randomLatenciaAtaque = randint(0, 9)
            self.setDisplay(randomLatenciaAtaque, self.displayLatencia)

            randomLatenciaDefesa = randint(0, 9)
            self.setDisplay(randomLatenciaDefesa, self.displayLatenciaDef)

            newLatATTK, newLatDEF, manaItens, textLbDica = randomLatenciaAtaque, randomLatenciaDefesa, 0, "\n"
            for item in self.player.inventory:
                if item.ended():
                    info = item.aplicarItem(self.player, attack, newLatATTK, newLatDEF)
                    newLatATTK, newLatDEF = info[0], info[1]
                    manaItens += info[2]
                    textLbDica += f"\n+ {item.name}"
            self.escreverNoCanvasDica(None, attack.getDados() + textLbDica, 'red')
            if attack.latencia <= newLatATTK:
                if self.player.mana < attack.mana:
                    self.setCanvasStatus(3)
                    self.setDisplay(self.player.mana if self.player.mana >= 0 else 0, self.displayManaPlayer)
                    self.setDisplay(self.player.hp if self.player.hp >= 0 else 0, self.displayLifePlayer)

                    self.Alternar = False
                    self.alterarBorda(False)
                else:
                    # ATAQUE EFETIVO
                    if self.bot.shield.latencia <= newLatDEF:
                        # DEFESA EFETIVA
                        self.setCanvasStatus(1)

                        # DADOS JOGÁVEIS
                        danos = System.calculeteDamageShield(self.bot, attack)
                        danoReal = danos[0] + danos[1]
                        self.bot.sufferDamage(danoReal)
                        self.player.userMana(attack.mana)
                        manaRestore = self.player.restoreMana(danoReal)

                        # RESTAURA MONEY
                        self.player.money += System.calculeteRestareMoney(type="an", dano=danoReal)

                        # DADOS ARMAZENÁVEIS
                        self.damageTotal += danoReal
                        self.damageFisico += danos[0]
                        self.damageMagico += danos[1]
                        self.CONTAttack += 1
                        self.CONTAttackNormais += 1
                        self.manaGasta += attack.mana
                        self.manaRestaurada += manaRestore

                        if manaItens > 0:
                            self.manaRestaurada += manaItens
                        else:
                            self.manaGasta += abs(manaItens)

                        StatusGame = self.verificarGame()
                        if any(StatusGame):
                            self.abrirTelaOption(all(StatusGame))
                        else:
                            # SET DISPLAY DADOS
                            self.setDisplay(danoReal, self.displayDanoReal)
                            self.setDisplay(self.player.hp, self.displayLifePlayer)
                            self.setDisplay(self.bot.hp, self.displayLifeBOT)

                            self.Alternar = False
                            self.alterarBorda(False)

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

                        # RESTAURA MONEY
                        self.player.money += System.calculeteRestareMoney(type="ac", dano=danoReal)

                        # DADOS ARMAZENÁVEIS
                        self.damageTotal += danoReal
                        self.damageFisico += danos[0]
                        self.damageMagico += danos[1]
                        self.CONTAttack += 1
                        self.CONTAttackCriticos += 1
                        self.manaGasta += attack.mana
                        self.manaRestaurada += manaRestore

                        if manaItens > 0:
                            self.manaRestaurada += manaItens
                        else:
                            self.manaGasta += abs(manaItens)

                        StatusGame = self.verificarGame()
                        if any(StatusGame):
                            self.abrirTelaOption(all(StatusGame))
                        else:
                            # SET DISPLAY DADOS
                            self.setDisplay(danoReal, self.displayDanoReal)
                            self.setDisplay(self.player.hp, self.displayLifePlayer)
                            self.setDisplay(self.bot.hp, self.displayLifeBOT)

                            self.Alternar = False
                            self.alterarBorda(False)

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

                # RESTAURA MONEY
                self.player.money += System.calculeteRestareMoney(type="f", dano=0)

                StatusGame = self.verificarGame()
                if any(StatusGame):
                    self.abrirTelaOption(all(StatusGame))
                else:
                    # SET DISPLAY DADOS
                    self.setDisplay(0, self.displayDanoReal)
                    self.setDisplay(self.player.hp, self.displayLifePlayer)
                    self.setDisplay(self.bot.hp, self.displayLifeBOT)

                    self.Alternar = False
                    self.alterarBorda(False)

                    if self.player.mana < 0:
                        self.player.mana = 0
                        self.setDisplay(self.player.mana, self.displayManaPlayer)
                    else:
                        self.setDisplay(self.player.mana, self.displayManaPlayer)

        else:
            self.lbDica["text"] = '''ERRO - Sua vez foi alternada, Click no Icon do BOT
    para ele realizar o ATTACK'''
            self.setCanvasStatus(-2)

    def limparCanvasDica(self, event):
        self.lbDica["text"] = ""

    def escreverNoCanvasDica(self, event, txt, cor="white"):
        self.lbDica.configure(fg=cor)
        self.lbDica["text"] = txt

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()

        #List de ataques do player
        attacksPlayer = self.player.sword.getAttack()

        # EVENTOS NO TECLADO
        self.root.bind(self.teclasConfig["Inventário"], self.setCanvasDICAInventario)
        self.root.bind(self.teclasConfig["compraInventário"], self.abrirTelaItens)
        self.root.bind(self.teclasConfig["attkBOT"], lambda event : self.ActionBOT())
        self.root.bind(self.teclasConfig["attk1-dica"],
                       lambda event, atk=attacksPlayer[0]: self.escreverNoCanvasDica(event, atk.getDados()))
        self.root.bind(self.teclasConfig["attk2-dica"],
                       lambda event, atk=attacksPlayer[1]: self.escreverNoCanvasDica(event, atk.getDados()))
        self.root.bind(self.teclasConfig["attk3-dica"],
                       lambda event, atk=attacksPlayer[2]: self.escreverNoCanvasDica(event, atk.getDados()))
        self.root.bind(self.teclasConfig["DadosArmadura"], self.setCanvasDICAShield)
        self.root.bind(self.teclasConfig["DadosEspada"], self.setCanvasDICASword)

        self.root["bg"] = "Black"
        self.lbPlAYER.place(x=self.xDisplayManaPlayer + 50, y=20)

        # Atribuindo a abertura da tela Compra itens a label de imagem do player
        self.lbPlAYER.bind("<Button-1>", self.abrirTelaItens)
        self.lbPlAYER.bind("<Enter>",
                           lambda event, txt="COMPRE NOVOS ITENS\nPARA O INVENTÁRIO": self.escreverNoCanvasDica(event,
                                                                                                                txt))
        self.lbPlAYER.bind("<Leave>", self.limparCanvasDica)

        self.lbBtBOT.place(x=self.xDisplayManaBOT + 50, y=20)

        # Atribuindo a função de ataque ao botão de imagens do bot
        self.lbBtBOT["command"] = self.ActionBOT
        self.lbBtBOT.bind("<Enter>", self.dadosBot)
        self.lbBtBOT.bind("<Leave>", self.limparCanvasDica)

        self.nomePlAYER.place(x=self.xDisplayManaPlayer, y=180)
        self.nomePlAYER.bind("<Enter>", self.setCanvasDICAInventario)
        self.nomePlAYER.bind("<Leave>", self.limparCanvasDica)

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
        # Display LIFE PLAYER
        for j in range(len(self.displayLifePlayer)):
            self.displayLifePlayer[j].config(bg="Black")
            self.displayLifePlayer[j].place(x=j * 50 + self.xDisplayLifiPlayer - recuo, y=self.yDisplayLifi + 60)
        self.lbLifePlayer.place(x=self.xDisplayLifiPlayer, y=self.yDisplayLifi)

        for j in range(len(self.displayManaPlayer)):
            self.displayManaPlayer[j].config(bg="Black")
            self.displayManaPlayer[j].place(x=j * 50 + self.xDisplayManaPlayer - recuo, y=self.yDisplayMana + 60)
        self.lbManaPlayer.place(x=self.xDisplayManaPlayer, y=self.yDisplayMana)

        # Display LIFE BOT
        for j in range(len(self.displayLifeBOT)):
            self.displayLifeBOT[j].config(bg="Black")
            self.displayLifeBOT[j].place(x=j * 50 + self.xDisplayLifiBOT - recuo, y=self.yDisplayLifi + 60)
        self.lbLifeBOT.place(x=self.xDisplayLifiBOT, y=self.yDisplayLifi)

        for j in range(len(self.displayManaBOT)):
            self.displayManaBOT[j].config(bg="Black")
            self.displayManaBOT[j].place(x=j * 50 + self.xDisplayManaBOT - recuo, y=self.yDisplayMana + 60)
        self.lbManaBOT.place(x=self.xDisplayManaBOT, y=self.yDisplayMana)

        # DISPLAY DL
        for j in range(len(self.displayDanoReal)):
            self.displayDanoReal[j].config(bg="Black")
            self.displayDanoReal[j].place(x=j * 50 + self.xMargeDisplayDL, y=self.yMargeDisplayDL)

        self.displayLatencia[0].config(bg="Black")
        self.displayLatencia[0].place(x=self.xMargeDisplayDL - 100, y=self.yMargeDisplayDL + 100)

        self.displayLatenciaDef[0].config(bg="Black")
        self.displayLatenciaDef[0].place(x=self.xMargeDisplayDL + 230, y=self.yMargeDisplayDL + 100)

        self.lbDanoReal.place(x=self.xMargeLabelDL, y=self.yMargeDisplayDL)
        self.lbDanoReal.bind("<Enter>",
                             lambda event, txt=self.stringDanoReal: self.escreverNoCanvasDica(event, txt))
        self.lbDanoReal.bind("<Leave>", self.limparCanvasDica)

        self.lbLatencia.place(x=self.xMargeLabelDL - 100, y=self.yMargeDisplayDL + 90)
        self.lbLatencia.bind("<Enter>",
                             lambda event, txt=self.stringRandLantATK: self.escreverNoCanvasDica(event, txt))
        self.lbLatencia.bind("<Leave>", self.limparCanvasDica)

        self.lbLatenciaDef.place(x=self.xMargeLabelDL + 230, y=self.yMargeDisplayDL + 90)
        self.lbLatenciaDef.bind("<Enter>",
                                lambda event, txt=self.stringRandLantDEF: self.escreverNoCanvasDica(event, txt))
        self.lbLatenciaDef.bind("<Leave>", self.limparCanvasDica)

        self.canvasAttk.pack(side=BOTTOM, anchor=S)
        self.canvasAttk.config(bg="black")

        for bt in range(len(self.BTSCommands)):
            if bt < 3:
                self.BTSCommands[bt].place(x=bt * 230, y=0)
                # Evento onclik
                self.BTSCommands[bt]["command"] = partial(self.knock, attacksPlayer[bt])

                # Evento de teclado
                self.root.bind(self.teclasAttkConfig[bt],
                               lambda event, func=self.knock, par=attacksPlayer[bt]: func(par))

                # Evento entrada e saida da área widget
                self.BTSCommands[bt].bind("<Enter>",
                                          lambda event, atk=attacksPlayer[bt]: self.escreverNoCanvasDica(event,
                                                                                                         atk.getDados()))
                self.BTSCommands[bt].bind("<Leave>", self.limparCanvasDica)
            else:
                self.BTSCommands[bt].place(x=bt * 230, y=0)
                # Evento onclik
                self.BTSCommands[bt]["command"] = self.defensiveMode
                # Evento de teclado
                self.root.bind(self.teclasAttkConfig[bt], lambda event: self.defensiveMode())

                # Evento entrada e saida da área widget
                self.BTSCommands[bt].bind("<Enter>",
                                          lambda event, txt=self.stringMODODEF: self.escreverNoCanvasDica(event, txt))
                self.BTSCommands[bt].bind("<Leave>", self.limparCanvasDica)

        self.canvasStatus.pack(side=TOP, anchor=N)
        self.canvasStatus.config(bg="Black")
        self.canvasAttackDica.pack(side=TOP, anchor=CENTER)
        self.canvasAttackDica.config(bg="Black")
        self.setCanvasStatus(-1)

        self.alterarBorda(self.Alternar)

        self.setDisplay(str(0), self.displayLatencia)
        self.setDisplay(str(0), self.displayLatenciaDef)
        self.setDisplay(str(0), self.displayDanoReal)
        self.setDisplay(str(self.player.hp), self.displayLifePlayer)
        self.setDisplay(str(self.bot.hp), self.displayLifeBOT)
        self.setDisplay(str(self.player.mana), self.displayManaPlayer)
        self.setDisplay(str(self.bot.mana), self.displayManaBOT)

        self.root.mainloop()


class TelaOption:
    def __init__(self, player, dadosDaPatida, status=True):
        self.root = Tk()

        self.player = player
        self.dadosDaPatida = dadosDaPatida

        self.margeX = 0
        self.margeY = 150
        self.x = 265
        self.y = 200
        self.color = "Black"

        self.imagemRelatorio = PhotoImage(
            file="DirPNG/relatorio.png")

        self.imagemContinue = PhotoImage(
            file="DirPNG/OutroDesafio.png")

        self.imagemVitoria = PhotoImage(
            file="DirPNG/vitoria.png")
        self.imagemDerrota = PhotoImage(
            file="DirPNG/derrota.png")

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
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
        self.root["bg"] = self.color
        self.lb["bg"] = self.color
        self.lb.pack(side=TOP)
        self.bt1.place(x=self.x, y=self.y)
        self.bt2.place(x=self.x + self.margeX, y=self.y + self.margeY)
        self.bt1["command"] = self.abrirRelatorio
        self.bt2["command"] = self.abrirChoosePlayer
        self.root.mainloop()


class TelaRelatorio:
    def __init__(self, dadosDaPartida):
        self.root = Tk()

        self.dadosDaPartida = dadosDaPartida

        self.imageLBTitulo = PhotoImage(
            file="DirPNG/relatorioTitulo.png")
        self.lbTitulo = Label(self.root, image=self.imageLBTitulo, highlightbackground="Black", bg="Black")

        # IMAGENS
        self.imageLBDanoTotal = PhotoImage(file="DirPNG/LBTelaRelatorio/danoTotal.png")
        self.imageLBDanoMagico = PhotoImage(file="DirPNG/LBTelaRelatorio/dmagico.png")
        self.imageLBDanoFisico = PhotoImage(file="DirPNG/LBTelaRelatorio/dfisico.png")
        self.imageLBAttacksFalhos = PhotoImage(file="DirPNG/LBTelaRelatorio/atkfalhos.png")
        self.imageLBAttacksCriticos = PhotoImage(file="DirPNG/LBTelaRelatorio/atkcritico.png")
        self.imageLBAttacksNormais = PhotoImage(file="DirPNG/LBTelaRelatorio/atknormal.png")
        self.imageLBTotalAttacks = PhotoImage(file="DirPNG/LBTelaRelatorio/ttAtk.png")
        self.imageLBFalhaDaArmadura = PhotoImage(file="DirPNG/LBTelaRelatorio/falhaArmadura.png")
        self.imageLBDanoMagicoSofrido = PhotoImage(file="DirPNG/LBTelaRelatorio/dmSofrido.png")
        self.imageLBDanoFisicoSofrido = PhotoImage(file="DirPNG/LBTelaRelatorio/dfSofrido.png")
        self.imageLBDanoMagicoDefendido = PhotoImage(file="DirPNG/LBTelaRelatorio/dmDef.png")
        self.imageLBDanoFisicoDefendido = PhotoImage(file="DirPNG/LBTelaRelatorio/dfDef.png")
        self.imageLBManaRestaurada = PhotoImage(file="DirPNG/LBTelaRelatorio/manaRest.png")
        self.imageLBManaGasta = PhotoImage(file="DirPNG/LBTelaRelatorio/manaUsa.png")

        # LABEL
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

        # CONFIG LABEL
        self.xLabel = 500
        self.yLabel = 125
        self.xMargerLabel = 20
        self.yMargerLabel = 150

        self.labels = [[self.LBDanoTotal, self.LBDanoMagico, self.LBDanoFisico, self.LBAttacksFalhos,
                        self.LBAttacksCriticos], [self.LBAttacksNormais, self.LBTotalAttacks, self.LBFalhaDaArmadura,
                                                  self.LBDanoMagicoSofrido, self.LBDanoFisicoSofrido],
                       [self.LBDanoMagicoDefendido,
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
                          self.displayAttacksFalhos, self.displayAttacksCriticos],
                         [self.displayAttacksNormais,self.displayTotalAttacks,self.displayFalhaDaArmadura,
                        self.displayDanoMagicoSofrido,self.displayDanoFisicoSofrido],
                         [self.displayDanoMagicoDefendido, self.displayDanoFisicoDefendido,
                          self.displayManaRestaurada, self.displayManaGasta]]
        self.backPNG = PhotoImage(
            file="DirPNG/backPNG.png")
        self.btVolta = Button(self.root, image=self.backPNG, bg="Black")

    def voltar(self):
        self.root.destroy()
        TelaInicio().construtor()

    def setDisplay(self, num, display):
        number = str(num)
        dicImagens = {
             "#": PhotoImage(file="DirPNG/DirPNGnumber/0.png"),
            "0": PhotoImage(file="DirPNG/DirPNGnumber/0.png"),
            "1": PhotoImage(file="DirPNG/DirPNGnumber/1.png"),
            "2": PhotoImage(file="DirPNG/DirPNGnumber/2.png"),
            "3": PhotoImage(file="DirPNG/DirPNGnumber/3.png"),
            "4": PhotoImage(file="DirPNG/DirPNGnumber/4.png"),
            "5": PhotoImage(file="DirPNG/DirPNGnumber/5.png"),
            "6": PhotoImage(file="DirPNG/DirPNGnumber/6.png"),
            "7": PhotoImage(file="DirPNG/DirPNGnumber/7.png"),
            "8": PhotoImage(file="DirPNG/DirPNGnumber/8.png"),
            "9": PhotoImage(file="DirPNG/DirPNGnumber/9.png")
        }
        strNumber = number if len(number) == len(display) else "#" * (len(display) - len(number)) + str(number)
        for elem in range(len(display)):
            imag = dicImagens[strNumber[elem]]
            display[elem].create_image(30, 35, image=imag)
            display[elem].image = imag

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
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
                infoPartida = self.dadosDaPartida[cont]
                self.setDisplay(infoPartida if infoPartida >= 0 else 0, self.displays[lbx][lby])
                cont += 1
        self.btVolta.pack(side=BOTTOM, anchor=SE)
        self.btVolta["command"] = self.voltar
        self.root.mainloop()


class TelaItens:
    def __init__(self, player, bot, alternar=True, dicInfo=None):
        self.root = Tk()
        self.listItens = System.filterItens()
        self.player = player
        self.bot = bot
        self.alternar = alternar
        self.dicInfo = dicInfo

        # CONFIG
        self.margeEX_x = 50
        self.margeEX_y = 130
        self.margeIN_x = 340
        self.margeIN_y = 210
        self.fontFixedsys15 = font.Font(family='Fixedsys', size=15)
        self.fontFixedsys25 = font.Font(family='Fixedsys', size=17)
        # Caminho diretório
        self.caminhoDirNum = "DirPNG/DirPNGnumber/numberGold/"

        self.canvaLayaot = Canvas(self.root, bg="Black", width=400, height=700, highlightbackground="Black")

        self.imageLb = PhotoImage(
            file="DirPNG/escolhaItens.png"
        )
        self.imageLbSimbol = PhotoImage(
            file="DirPNG/DirPNGnumber/numberGold/u.png"
        )
        self.lbTitulo = Label(self.root, image=self.imageLb, highlightbackground="Black", bg="black")

        self.canvasImage = Canvas(self.canvaLayaot, width=250, height=250, bg="Black", highlightbackground="Black")
        self.lb = Label(self.canvaLayaot, font=self.fontFixedsys25, bg="Black", fg="white")
        self.lbSimbol = Label(self.root, width=80, height=80, image=self.imageLbSimbol, highlightbackground="Black",
                              bg="Black")

        self.bt1 = Button(self.root, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt2 = Button(self.root, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt3 = Button(self.root, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt4 = Button(self.root, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt5 = Button(self.root, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt6 = Button(self.root, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)

        self.listBt = [[self.bt1, self.bt2, self.bt3], [self.bt4, self.bt5, self.bt6]]

        self.c1 = Canvas(self.root, width=80, height=80, highlightbackground="Black", bg="black")
        self.c2 = Canvas(self.root, width=80, height=80, highlightbackground="Black", bg="black")
        self.c3 = Canvas(self.root, width=80, height=80, highlightbackground="Black", bg="black")
        self.c4 = Canvas(self.root, width=80, height=80, highlightbackground="Black", bg="black")
        self.displayMoney = [self.c1, self.c2, self.c3, self.c4]

        self.image = PhotoImage(
            file="DirPNG/continue.png"
        )

        self.btContinuar = Button(self.root, image=self.image, width=400, height=200, bg="black")

        self.backPNG = PhotoImage(
            file="DirPNG/backPNG.png")
        self.btVolta = Button(self.root, image=self.backPNG, bg="Black")

    def voltar(self):
        self.root.destroy()
        TelaEscolhaBot().construtor()

    def dinheiroERRO(self):
        self.lb["text"] = "VOCÊ NÃO POSSUE MOEDAS\nPARA COMPRAR ESSE ITEM"

    def addItem(self, item, bt):
        if self.player.money >= item.valor:
            self.player.addItem(item)
            self.lb["text"] = f"ITEM {item.name}\nCOMPRADO COM SUCESSO!"
            self.setDisplay(str(self.player.money), self.displayMoney)
            bt["bg"] = "Blue"
            bt["command"] = lambda: None
        else:
            self.dinheiroERRO()

    def setLABEitem(self, event, item=None):
        if not item is None:
            self.lb["text"] = item.getDados()
            image = PhotoImage(file=item.image)
            self.canvasImage.create_image(120, 100, image=image)
            self.canvasImage.image = image
        else:
            self.lb["text"] = ""
            self.canvasImage.delete("all")

    def abrirTelaMain(self):
        self.root.destroy()
        TelaMain(self.player, self.bot, alternar=self.alternar, dicDados=self.dicInfo).construtor()

    def setDisplay(self, num, display):
        number = str(num)
        dicImagens = {
            "#": PhotoImage(file=self.caminhoDirNum + "0.png"),
            "0": PhotoImage(file=self.caminhoDirNum + "0.png"),
            "1": PhotoImage(file=self.caminhoDirNum + "1.png"),
            "2": PhotoImage(file=self.caminhoDirNum + "2.png"),
            "3": PhotoImage(file=self.caminhoDirNum + "3.png"),
            "4": PhotoImage(file=self.caminhoDirNum + "4.png"),
            "5": PhotoImage(file=self.caminhoDirNum + "5.png"),
            "6": PhotoImage(file=self.caminhoDirNum + "6.png"),
            "7": PhotoImage(file=self.caminhoDirNum + "7.png"),
            "8": PhotoImage(file=self.caminhoDirNum + "8.png"),
            "9": PhotoImage(file=self.caminhoDirNum + "9.png")

        }
        strNumber = number if len(number) == len(display) else "#" * (len(display) - len(number)) + str(number)
        for elem in range(len(display)):
            imag = dicImagens[strNumber[elem]]
            display[elem].create_image(50, 50, image=imag)
            display[elem].image = imag

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()

        # Eventos TECLADOS
        self.root.bind("<Return>", lambda event: self.abrirTelaMain())

        self.root["bg"] = "Black"
        self.canvaLayaot.place(x=1170, y=150)
        self.canvasImage.pack(anchor=CENTER)
        self.lb.pack(anchor=CENTER)
        self.btContinuar.place(x=320, y=600)
        self.btContinuar["command"] = self.abrirTelaMain
        self.lbTitulo.place(x=280, y=0)
        self.lbSimbol.place(x=1020, y=700)
        cont = 0
        for line in range(len(self.listBt)):
            for colunn in range(len(self.listBt[line])):
                self.listBt[line][colunn].place(x=colunn * self.margeIN_x + self.margeEX_x,
                                                y=line * self.margeIN_y + self.margeEX_y)
                self.listBt[line][colunn]["text"] = f'''{self.listItens[cont].name.upper()}\n\nx{self.listItens[
                    cont].quatidade}\n{self.listItens[cont].valor}U$'''
                self.listBt[line][colunn].bind("<Enter>",
                                               lambda event, item=self.listItens[cont]: self.setLABEitem(event, item))
                self.listBt[line][colunn].bind("<Leave>", self.setLABEitem)
                self.listBt[line][colunn]["command"] = partial(self.addItem, self.listItens[cont],
                                                               self.listBt[line][colunn])
                cont += 1
        for index in range(len(self.displayMoney)):
            self.displayMoney[index].place(x=90 * index + 1110, y=690)

        self.btVolta.pack(side=BOTTOM, anchor=SW)
        self.btVolta["command"] = self.voltar

        self.setDisplay(str(self.player.money), self.displayMoney)
        self.root.mainloop()
