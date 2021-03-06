from functools import partial
from tkinter import *
from tkinter import font,scrolledtext
from fileClass import *
import time

from fileBD import *

userPlayer = User("Tan", "21", "UserTAN.txt","ITENSUserTAN.txt")

class TelaEscolhaBot:
    def __init__(self):
        self.root = Tk()
        # CONFIG
        self.color = "Black"
        self.btSizeX = 400
        self.btSizeY = 200

        self.p1 = None
        self.BOT = None

        self.imagemLabelBOT = PhotoImage(
            file="DirPNG/ImagemLabelBOT.png")
        self.imagemLabelPlayer = PhotoImage(
            file="DirPNG/ImagemLabelPlayer.png")
        self.imagemLabelDESAFIAR1 = PhotoImage(
            file="DirPNG/DESAFIAR1.png")

        #Canvas Desenho
        self.canvas_top = Canvas(self.root, bg="Black", highlightbackground="Black")
        self.canvas_div_top_1 = Canvas(self.canvas_top,width=50, height=5, bg="Black", highlightbackground="Black")
        self.canvas_div_top_2 = Canvas(self.canvas_top, width=50, height=5, bg="Black", highlightbackground="Black")

        self.canvas_div_v_1 = Canvas(self.root,width=5, height=50, bg="Black", highlightbackground="Black")

        self.canvas_line_1 = Canvas(self.root, bg="Black", highlightbackground="Black")
        self.canvas_div_h_line1_1 = Canvas(self.canvas_line_1, width=30, height=5, bg="Black", highlightbackground="Black")
        self.canvas_div_h_line1_2 = Canvas(self.canvas_line_1, width=30, height=5, bg="Black", highlightbackground="Black")

        self.canvas_div_v_2 = Canvas(self.root, width=5, height=50, bg="Black", highlightbackground="Black")

        self.canvas_line_2 = Canvas(self.root, bg="Black", highlightbackground="Black")
        self.canvas_div_h_line2_1 = Canvas(self.canvas_line_2, width=30, height=5, bg="Black",highlightbackground="Black")
        self.canvas_div_h_line2_2 = Canvas(self.canvas_line_2, width=30, height=5, bg="Black",highlightbackground="Black")

        # IMAGENS DOS PLAYER
        self.IchigoKurosakiPNG = PhotoImage(file=System.choosePlayer(0).imageShowChoose)
        self.KillerBeePNG = PhotoImage(file=System.choosePlayer(1).imageShowChoose)
        self.XenaPNG = PhotoImage(file=System.choosePlayer(2).imageShowChoose)
        self.RoronoaZoroPNG = PhotoImage(file=System.choosePlayer(3).imageShowChoose)
        self.GohanPNG = PhotoImage(file=System.choosePlayer(4).imageShowChoose)
        self.backPNG = PhotoImage(file="DirPNG/backPNG.png")

        self.bt1 = Button(self.canvas_line_1, image=self.IchigoKurosakiPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt2 = Button(self.canvas_line_1, image=self.KillerBeePNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt3 = Button(self.canvas_line_1, image=self.XenaPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt4 = Button(self.canvas_line_2, image=self.RoronoaZoroPNG, width=self.btSizeX,
                          height=self.btSizeY)
        self.bt5 = Button(self.canvas_line_2, image=self.GohanPNG, width=self.btSizeX,
                          height=self.btSizeY)


        self.lb = Label(self.canvas_top, image=self.imagemLabelPlayer, bg=self.color)
        self.canvasNamePlayer = Canvas(self.canvas_top, width=200, height=60, bg="black", highlightbackground="Black", border=0)
        self.canvasNameBOT = Canvas(self.canvas_top, width=200, height=60, bg="black", highlightbackground="Black",
                                       border=0)

        self.btVoltar = Button(self.root, image=self.backPNG, bg="Black")

        self.bts = [self.bt1, self.bt2, self.bt3, self.bt4, self.bt5]
        self.matriz = [[self.bt1,self.canvas_div_h_line1_1, self.bt2,self.canvas_div_h_line1_2, self.bt3],
                       [self.bt4,self.canvas_div_h_line2_1, self.bt5, self.canvas_div_h_line2_2]]

        self.canvasStrategy = Canvas(self.root, width=1500, height=40, bg="black", highlightbackground="Black")
        self.canvasStrategyPersonality = Canvas(self.root, width=1000, height=50, bg="black",
                                               highlightbackground="Black")
        self.fontFixedsys15 = font.Font(family='Fixedsys', size=12)

        #Variáveis
        self.alterPersonality = False
        self.personalityAttk = 'None'
        self.strategyVariables = {}
        self.strategyCheckButton = {}

        self.imageBTDesafiar = PhotoImage(file="DirPNG/DESAFIAR.png")

        self.btAlterStrategyBot = Button(self.root, width=25, height=2, bg="#ec352e", fg="black",
                    highlightbackground="#ec352e", font=font.Font(family='Fixedsys', size=15), text="Alterar Estratégia Bot")
        self.btAbrirTelaItens = Button(self.root, width=400, height=200, bg="black",highlightbackground="black",
                                       image=self.imageBTDesafiar, border=0)

        dic = InteligencePlayer(None,None,0).strategyItens

        for estrategia in dic:
            auxC = Checkbutton(self.canvasStrategy, text=dic[estrategia]["name"], font=self.fontFixedsys15, bg="black",
                               fg="#ec352e", activeforeground="#ec352e", activebackground="black", highlightbackground="black")
            self.strategyVariables.update({estrategia : False})
            self.strategyCheckButton.update({estrategia : auxC})

        self.lbCanvasEstrategia = Label(self.root, font=font.Font(family='Fixedsys', size=15),
                                        fg="#ec352e",bg="Black", highlightbackground="black",width=25, height=2,
                                        text="CONFIGURE E ESCOLHA O BOT")
        self.radioAggressive = Radiobutton(self.canvasStrategyPersonality, bg="black", fg="#ec352e", text="Aggressive",
                                            font=font.Font(family='Fixedsys', size=15), value='713',highlightbackground="black",
                                            variable=self.personalityAttk)
        self.radioStrategy = Radiobutton(self.canvasStrategyPersonality, bg="black", fg="#ec352e", text="Strategy",
                                           font=font.Font(family='Fixedsys', size=15), value='432',highlightbackground="black",
                                           variable=self.personalityAttk)
        self.radioFrantic = Radiobutton(self.canvasStrategyPersonality, bg="black", fg="#ec352e", text="Frantic",
                                         font=font.Font(family='Fixedsys', size=15), value='147',highlightbackground="black",
                                         variable=self.personalityAttk)
        self.radioDefault = Radiobutton(self.canvasStrategyPersonality, bg="black", fg="#ec352e", text="Default",
                                        font=font.Font(family='Fixedsys', size=15), value='None',highlightbackground="black",
                                        variable=self.personalityAttk)

        self.lbStrategyItens = Label(self.canvasStrategy, font=font.Font(family='Fixedsys', size=11),
                                        fg="White",bg="Black", highlightbackground="black",width=19, height=2,
                                        text="Strategy Itens")
        self.lbStrategyAttk = Label(self.canvasStrategyPersonality, font=font.Font(family='Fixedsys', size=11),
                                     fg="White", bg="Black", highlightbackground="black", width=19, height=2,
                                     text="Strategy Attack")

    def invertValue(self, variable):
        '''
        Ela inverte o valor do dic self.strategyVariables pela chave passada
        :param variable:
        :return:
        '''
        self.strategyVariables[variable] = not self.strategyVariables[variable]

    def alterPersonalityFunc(self, listValue):
        self.personalityAttk = listValue

    def alterStrategy(self, widget):
        self.alterPersonality = not self.alterPersonality
        if self.alterPersonality:
            self.canvasStrategyPersonality.pack(side=BOTTOM, anchor=S)
            self.canvasStrategy.pack(side=BOTTOM, anchor=S)
            self.lbCanvasEstrategia.pack(side=BOTTOM, anchor=S)
            widget["text"] = "Config Default"
        else:
            self.canvasStrategy.pack_forget()
            self.lbCanvasEstrategia.pack_forget()
            self.canvasStrategyPersonality.pack_forget()
            widget["text"] = "Alterar Estratégia Bot"

    def ADDbtAlterStrategyBot(self):
        self.btAlterStrategyBot.pack(side=BOTTOM, anchor=SE)
        self.btAlterStrategyBot["command"] = lambda widget=self.btAlterStrategyBot: self.alterStrategy(widget)

    def choose(self, contCamp):

        # OBJETO Player
        player = System.choosePlayer(contCamp)
        if self.p1 is None:
            # TOCAR ÁUDIO
            player.PlayWAVShow()
            self.p1 = player

            # MUDAR IMAGENS DE TÍTULO
            self.lb["image"] = self.imagemLabelBOT

            #ADD Image Canvas Nome Player
            self.ADDimageCanvas(self.canvasNamePlayer, self.p1.imageID)

        elif self.BOT is None:
            # TOCAR ÁUDIO
            player.PlayWAVShow()
            self.BOT = player
            self.ADDimageCanvas(self.canvasNameBOT, self.BOT.imageID)

            # Retirando o blocos anteriores
            self.canvas_line_1.pack_forget()
            self.canvas_div_v_2.pack_forget()
            self.canvas_line_2.pack_forget()

            # Aumentando o espacamento anterior
            self.canvas_div_v_1["height"] = 200

            self.btAbrirTelaItens.pack()
            self.btAbrirTelaItens["command"] = self.abrirTelaItens

            self.lb["image"] = self.imagemLabelDESAFIAR1

    def ADDimageCanvas(self, canvas, strImage):
        imag = PhotoImage(file=strImage)
        canvas.create_image(102, 32, image=imag)
        canvas.image = imag

    def abrirTelaItens(self):
        if self.alterPersonality:
            print("Alterada")
            self.BOT.setPersonalityItens(self.strategyVariables)
            if self.personalityAttk != 'None':
                self.BOT.setPersonalityAttk(self.personalityAttk)
        else:
            print("Não alterada")

        # CHAMAR OUTRA TELA
        self.root.destroy()
        TelaItens(self.p1, self.BOT).construtor()

    def voltar(self):
        self.root.destroy()
        TelaInicio().construtor()

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")
        self.root["bg"] = self.color

        self.canvas_top.pack()
        self.canvas_div_v_1.pack()
        self.canvas_line_1.pack()
        self.canvas_div_v_2.pack()
        self.canvas_line_2.pack()

        # VARIÁVEL AUXILIAR PARA INDEX DO PLAYER { self.choose(contCamp) }

        for contCamp in range(5):
            self.bts[contCamp]["command"] = partial(self.choose, contCamp)

        # GRADEADO DOS BUTTONS
        for line in range(len(self.matriz)):
            for column in range(len(self.matriz[line])):
                self.matriz[line][column].pack(side=LEFT)

        self.lbStrategyItens.pack(side=LEFT)
        self.lbStrategyAttk.pack(side=LEFT)

        for nomeStrategy in self.strategyCheckButton:
            self.strategyCheckButton[nomeStrategy].pack(side=LEFT)
            self.strategyCheckButton[nomeStrategy]["command"] = partial(self.invertValue, nomeStrategy)

        self.radioDefault.pack(side=LEFT)
        self.radioDefault["command"] = partial(self.alterPersonalityFunc, self.radioDefault["value"])
        self.radioDefault.select()

        self.radioAggressive.pack(side=LEFT)
        self.radioAggressive["command"] = partial(self.alterPersonalityFunc, self.radioAggressive["value"])

        self.radioStrategy.pack(side=LEFT)
        self.radioStrategy["command"] = partial(self.alterPersonalityFunc, self.radioStrategy["value"])

        self.radioFrantic.pack(side=LEFT)
        self.radioFrantic["command"] = partial(self.alterPersonalityFunc, self.radioFrantic["value"])

        self.canvasNamePlayer.pack(side=LEFT)
        self.canvas_div_top_1.pack(side=LEFT)
        self.lb.pack(side=LEFT)
        self.canvas_div_top_2.pack(side=LEFT)
        self.canvasNameBOT.pack(side=LEFT)

        self.btVoltar.place(x=0,y=0)
        self.ADDbtAlterStrategyBot()
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
        self.imageTutor = PhotoImage(file="DirPNG/TUTORIAL.png")
        self.imagePerfil = PhotoImage(file="DirPNG/PERFILinicio.png")

        self.div_vertical_1 = Canvas(self.root, width=10, height=80, bg="Black", highlightbackground="Black")
        self.div_vertical_2 = Canvas(self.root, width=10, height=30, bg="Black", highlightbackground="Black")

        self.canvas_line_1 = Canvas(self.root, bg="Black",highlightbackground="Black")
        self.div_horizontal_1 = Canvas(self.canvas_line_1, width=25, height=10, bg="Black", highlightbackground="Black")
        self.div_horizantal_2 = Canvas(self.canvas_line_1, width=25, height=10, bg="Black", highlightbackground="Black")

        self.canvas_line_2 = Canvas(self.root, bg="Black", highlightbackground="Black")

        self.bt1 = Button(self.canvas_line_2, image=self.imagemPlayerXbot, border=0, width=400, height=200, relief="groove", bg="Black")
        self.btSair = Button(self.canvas_line_1, image=self.imageSair, border=0, width=400, height=200, relief="groove", bg="Black")
        self.btTutor = Button(self.canvas_line_1, image=self.imageTutor, border=0, width=400, height=200, relief="groove", bg="Black")
        self.btPerfil = Button(self.canvas_line_1, image=self.imagePerfil, border=0, width=400, height=200, relief="groove",
                              bg="Black")

        self.lb = Label(self.root, image=self.imagemLabel, bg="Black")

    def abrirTelaEscolhaPlayerBOT(self):
        self.root.destroy()
        TelaEscolhaBot().construtor()

    def abrirTelaTutor(self):
        self.root.destroy()
        TelaTutor().construtor()
    def abrirTelaPerfil(self):
        self.root.destroy()
        TelaPerfil().construtor()

    def sair(self):
        self.root.destroy()
        TelaLogin().construtor()

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")

        self.root.bind("<Return>", lambda event: self.abrirTelaEscolhaPlayerBOT())
        self.root["bg"] = self.color
        self.lb["bg"] = self.color

        self.btSair.pack(side=LEFT)
        self.div_horizontal_1.pack(side=LEFT)
        self.btPerfil.pack(side=LEFT)
        self.div_horizantal_2.pack(side=LEFT)
        self.btTutor.pack(side=LEFT)

        self.bt1.pack()

        self.lb.pack()
        self.div_vertical_1.pack()
        self.canvas_line_1.pack()
        self.div_vertical_2.pack()
        self.canvas_line_2.pack()

        self.bt1["command"] = self.abrirTelaEscolhaPlayerBOT
        self.btSair["command"] = self.sair
        self.btTutor["command"] = self.abrirTelaTutor
        self.btPerfil["command"] = self.abrirTelaPerfil
        self.root.mainloop()


class TelaMain:
    def __init__(self, player, bot, alternar=True, dicDados=None):
        self.root = Tk()

        ######### Back-End

        # Alternar Ataques
        self.Alternar = alternar
        # PLAYER
        self.player = player
        self.bot = bot
        Attacks = self.player.sword.getAttack()

        # CRIAR A UMA INSTÂNCIA DA INTALIGÊNCIA BOT
        self.intelBOT = InteligencePlayer(self.bot, self.player, self.bot.baseMana)
        for key in self.bot.personality:
            self.intelBOT.__setattr__(key, self.bot.personality[key])


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

        ######### Front-End
        # Canvas Estrutural
        self.canvas_main = Canvas(self.root, bg="Black", highlightbackground="Black")

        self.canvas_player = Canvas(self.canvas_main, bg="Black", highlightbackground="Black")
        self.canvas_line_shop_inve = Canvas(self.canvas_player, bg="Black", highlightbackground="Black")
        self.canvas_display_life_player = Canvas(self.canvas_player, bg="Black", highlightbackground="Black")
        self.canvas_display_mana_player = Canvas(self.canvas_player, bg="Black", highlightbackground="Black")

        self.canvas_mid = Canvas(self.canvas_main, bg="Black", highlightbackground="Black")
        self.canvas_mid_info = Canvas(self.canvas_mid, bg="Black", highlightbackground="Black")
        self.canvas_mid_danoReal = Canvas(self.canvas_mid, bg="Black", highlightbackground="Black")
        self.canvas_mid_random = Canvas(self.canvas_mid, bg="Black", highlightbackground="Black")

        self.canvas_bot = Canvas(self.canvas_main, bg="Black", highlightbackground="Black")
        self.canvas_display_life_bot = Canvas(self.canvas_bot, bg="Black", highlightbackground="Black")
        self.canvas_display_mana_bot = Canvas(self.canvas_bot, bg="Black", highlightbackground="Black")

        ##### Imagens
        ##############################################################
        # LIFE
        self.imageLife1 = PhotoImage(file="DirPNG/life.png")
        self.imageLife2 = PhotoImage(file="DirPNG/life.png")
        # MANA
        self.imageMana1 = PhotoImage(file="DirPNG/mana.png")
        self.imageMana2 = PhotoImage(file="DirPNG/mana.png")
        # STATUS
        self.imageStatusFalhou = PhotoImage(file="DirPNG/ataqueFalhou.png")
        self.imageStatusEfetivo = PhotoImage(file="DirPNG/ataqueEfetivo.png")
        self.imageStatusCritico = PhotoImage(file="DirPNG/critico.png")
        self.imageStatusModoDef = PhotoImage(file="DirPNG/modeDEFF.png")
        self.imageStatusHome = PhotoImage(file="DirPNG/DESAFIAR1.png")
        self.imageStatusManaAlerta = PhotoImage(file="DirPNG/manaAlerta.png")
        self.imageStatusErro = PhotoImage(file="DirPNG/ERRO.png")
        # INVENTARIO E SHOP
        self.imageInventario = PhotoImage(file="DirPNG/inventario.png")
        self.imageShop = PhotoImage(file="DirPNG/shop.png")
        # LATENCIA E DANO REAL
        self.imgLatencia = PhotoImage(file="DirPNG/latenciaATTK.png")
        self.imgLatenciaDEF = PhotoImage(file="DirPNG/latenciaDEF.png")
        self.imgDanoReal = PhotoImage(file="DirPNG/danoReal.png")
        # Attacks
        self.imageATTK1 = PhotoImage(file=Attacks[0].imageBt)
        self.imageATTK2 = PhotoImage(file=Attacks[1].imageBt)
        self.imageATTK3 = PhotoImage(file=Attacks[2].imageBt)
        self.imageDEF = PhotoImage(file="DirPNG/deff.png")
        # IMAGE PLAYER
        self.ImageShowPlayer = PhotoImage(file=self.player.imageShow)
        self.ImageIDPlayer = PhotoImage(file=player.imageID)
        self.ImageIDSwordPlayer = PhotoImage(file=player.sword.imageID)
        self.ImageIDShieldPlayer = PhotoImage(file=player.shield.imageID)
        # IMAGE BOT
        self.ImageShowBOT = PhotoImage(file=self.bot.imageShow)
        self.ImageIDBOT = PhotoImage(file=bot.imageID)
        self.ImageIDSwordBOT = PhotoImage(file=bot.sword.imageID)
        self.ImageIDShieldBOT = PhotoImage(file=bot.shield.imageID)
        # IMAGE TURNO
        self.ImageTurnoYes= PhotoImage(file="DirPNG/iconTurnosYes.png")
        self.ImageTurnoNo = PhotoImage(file="DirPNG/iconTurnosNo.png")
        ##############################################################

        # Lb Player
        self.lbTurnoPlayer = Label(self.canvas_player, bg="Black")
        self.lbPlAYER = Label(self.canvas_player, image=self.ImageShowPlayer, width=100, height=150, relief="groove")
        self.nomePlAYER = Label(self.canvas_player, image=self.ImageIDPlayer, width=200, height=60, bg="Black")
        self.swordPlAYER = Label(self.canvas_player, image=self.ImageIDSwordPlayer, width=200, height=60, bg="Black")
        self.shieldPlayer = Label(self.canvas_player, image=self.ImageIDShieldPlayer, width=200, height=60, bg="Black")

        # Lb BOT
        self.lbTurnoBot = Label(self.canvas_bot, bg="Black")
        self.lbBtBOT = Button(self.canvas_bot, image=self.ImageShowBOT, width=100, height=150, relief="groove")
        self.nomeBOT = Label(self.canvas_bot, image=self.ImageIDBOT, width=200, height=60, bg="Black")
        self.swordBOT = Label(self.canvas_bot, image=self.ImageIDSwordBOT, width=200, height=60, bg="Black")
        self.shieldBOT = Label(self.canvas_bot, image=self.ImageIDShieldBOT, width=200, height=60, bg="Black")

        self.lbLifePlayer = Label(self.canvas_player, width=200, height=60, image=self.imageLife1, bg="Black")
        self.lbLifeBOT = Label(self.canvas_bot, width=200, height=60, image=self.imageLife2, bg="Black")
        self.lbManaPlayer = Label(self.canvas_player, width=200, height=60, image=self.imageMana1, bg="Black")
        self.lbManaBOT = Label(self.canvas_bot, width=200, height=60, image=self.imageMana2, bg="Black")

        # CANVAS STATUS
        self.canvasStatus = Canvas(self.canvas_mid, width=725, height=200, highlightbackground="Black", bg="black")

        # CANVAS ATTACK DICA
        self.canvasAttackDica = Canvas(self.canvas_mid_info, highlightbackground="Black", bg="black")
        self.fontFixedsys = font.Font(family='Fixedsys', size=17)
        font.families()
        self.lbDica = Label(self.canvasAttackDica, font=self.fontFixedsys, width=30, height=15, foreground="white", bg="black")
        self.lbDica.pack(side=TOP, anchor=CENTER)

        #LABEL INVENTÁRIO & LOJA
        self.lbInventarioPlayer = Canvas(self.canvas_line_shop_inve, width=80, height=80, bg="white", highlightbackground="Black")
        self.lbInventarioBOT = Canvas(self.canvas_bot, width=80, height=80, bg="white",  highlightbackground="Black")
        self.lbShop = Canvas(self.canvas_line_shop_inve, width=80, height=80, bg="white",  highlightbackground="Black")

        #LABEL MANA E MONEY RESTAURADO
        self.lbRestareManaMoney = Label(self.canvas_mid_info, font=self.fontFixedsys, width=25, height=15, fg="#ec352e", bg="black")
        self.lbItensUsados = Label(self.canvas_mid_info, font=self.fontFixedsys,width=25, height=15, fg="#ec352e", bg="black")

        # DISPLAY
        self.c1 = Canvas(self.canvas_display_life_player, width=60, height=60, highlightbackground="Black")
        self.c2 = Canvas(self.canvas_display_life_player, width=60, height=60, highlightbackground="Black")
        self.c3 = Canvas(self.canvas_display_life_player, width=60, height=60, highlightbackground="Black")
        self.c4 = Canvas(self.canvas_display_life_player, width=60, height=60, highlightbackground="Black")
        self.c17 = Canvas(self.canvas_display_life_player, width=60, height=60, highlightbackground="Black")
        self.displayLifePlayer = [self.c1, self.c2, self.c3, self.c4, self.c17]

        self.c5 = Canvas(self.canvas_display_life_bot, width=60, height=60, highlightbackground="Black")
        self.c6 = Canvas(self.canvas_display_life_bot, width=60, height=60, highlightbackground="Black")
        self.c7 = Canvas(self.canvas_display_life_bot, width=60, height=60, highlightbackground="Black")
        self.c8 = Canvas(self.canvas_display_life_bot, width=60, height=60, highlightbackground="Black")
        self.c18 = Canvas(self.canvas_display_life_bot, width=60, height=60, highlightbackground="Black")
        self.displayLifeBOT = [self.c5, self.c6, self.c7, self.c8, self.c18]

        self.c9 = Canvas(self.canvas_display_mana_player, width=60, height=60, highlightbackground="Black")
        self.c10 = Canvas(self.canvas_display_mana_player, width=60, height=60, highlightbackground="Black")
        self.c11 = Canvas(self.canvas_display_mana_player, width=60, height=60, highlightbackground="Black")
        self.c12 = Canvas(self.canvas_display_mana_player, width=60, height=60, highlightbackground="Black")
        self.c19 = Canvas(self.canvas_display_mana_player, width=60, height=60, highlightbackground="Black")
        self.displayManaPlayer = [self.c9, self.c10, self.c11, self.c12, self.c19]

        self.c13 = Canvas(self.canvas_display_mana_bot, width=60, height=60, highlightbackground="Black")
        self.c14 = Canvas(self.canvas_display_mana_bot, width=60, height=60, highlightbackground="Black")
        self.c15 = Canvas(self.canvas_display_mana_bot, width=60, height=60, highlightbackground="Black")
        self.c16 = Canvas(self.canvas_display_mana_bot, width=60, height=60, highlightbackground="Black")
        self.c20 = Canvas(self.canvas_display_mana_bot, width=60, height=60, highlightbackground="Black")
        self.displayManaBOT = [self.c13, self.c14, self.c15, self.c16, self.c20]

        # LABEL DANO, LATÊNCIA
        self.lbLatencia = Label(self.canvas_mid_random, width=200, height=80, bg="Black", highlightbackground="Black",
                                image=self.imgLatencia)
        self.lbLatenciaDef = Label(self.canvas_mid_random, width=200, height=80, bg="Black", highlightbackground="Black",
                                   image=self.imgLatenciaDEF)
        self.lbDanoReal = Label(self.canvas_mid_danoReal, width=200, height=80, bg="Black", highlightbackground="Black",
                                image=self.imgDanoReal)

        # DISPLAY DANO
        self.c21 = Canvas(self.canvas_mid_danoReal, width=60, height=60, highlightbackground="Black")
        self.c22 = Canvas(self.canvas_mid_danoReal, width=60, height=60, highlightbackground="Black")
        self.c23 = Canvas(self.canvas_mid_danoReal, width=60, height=60, highlightbackground="Black")
        self.c24 = Canvas(self.canvas_mid_danoReal, width=60, height=60, highlightbackground="Black")
        self.displayDanoReal = [self.c21, self.c22, self.c23, self.c24]

        # DISPLAY LATENCIA
        self.c25 = Canvas(self.canvas_mid_random, width=60, height=60, highlightbackground="Black")
        self.displayLatencia = [self.c25]
        self.c26 = Canvas(self.canvas_mid_random, width=60, height=60, highlightbackground="Black")
        self.displayLatenciaDef = [self.c26]

        # BOTÕES DE ATTACK
        self.canvasAttk = Canvas(self.canvas_mid, width=925, height=205, highlightbackground="Black")
        self.btAttk1 = Button(self.canvasAttk, width=220, height=200, image=self.imageATTK1, bg='Black',
                              highlightbackground="Black")
        self.btAttk2 = Button(self.canvasAttk, width=220, height=200, image=self.imageATTK2, bg='Black',
                              highlightbackground="Black")
        self.btAttk3 = Button(self.canvasAttk, width=220, height=200, image=self.imageATTK3, bg='Black',
                              highlightbackground="Black")
        self.btdef1 = Button(self.canvasAttk, width=220, height=200, image=self.imageDEF, bg='Black',
                             highlightbackground="Black")
        self.BTSCommands = [self.btAttk1, self.btAttk2, self.btAttk3, self.btdef1]
        self.teclasAttkConfig = ["<Q>", "<W>", "<E>", "<R>"]
        self.teclasConfig = {
            "Inventário" : "<v>",
            "compraInventário" : "<b>",
            "attkBOT" : "<Return>",
            "attk1-dica" : "<q>",
            "attk2-dica": "<w>",
            "attk3-dica": "<e>",
            "DadosArmadura": "<f>",
            "DadosEspada": "<g>"
        }

        # TEXTOS DE DICAS
        self.stringMODODEF = '''
Mantenha modo Defensivo
para atacar mais forte
na próxima rodada'''
        self.stringRandLantDEF = '''
Random de DEFESA 
representa o dado lançado 
que definir a falha ou a 
efetividade do bloqueio'''
        self.stringRandLantATK = '''
Random de ATTACK 
representa o dado lançado 
que definir a falha ou a 
efetividade do ataque'''
        self.stringDanoReal = '''
Valor de DANO VERDADEIRO
(Dano Mágico - Amadura Mágica)
+ 
(Dano Físico - Armadura Físico)'''
        self.stringERRO ='''
ERRO - Espera a ação do BOT
Click no Icon do BOT
ou
No botão ENTER
para Atualizar'''

    def setCanvasDICAinfoBOT(self, event):
        self.limparCanvasDica(None)
        txt = "INVENTÁRIO\n"
        for item in self.bot.inventory:
            txt += f"{item.name.upper()} x{item.quatidade}\n"
        txt += f"\nU${self.bot.money}"
        self.lbDica["text"] = txt

    def alterarBorda(self, vez):
        if vez:
            self.lbTurnoPlayer["image"] = self.ImageTurnoYes
            self.lbTurnoBot["image"] = self.ImageTurnoNo
        else:
            self.lbTurnoPlayer["image"] = self.ImageTurnoNo
            self.lbTurnoBot["image"] = self.ImageTurnoYes

    def actionBOT(self):
        #limpar canvas
        self.limparCanvasDica(None)
        if not self.Alternar:
            attacksBOT = self.bot.sword.getAttack()

            self.intelBOT.gerarRanckAttack(self.player)
            value = self.intelBOT.resolverAttack(self.player)

            if value == 3:
                self.setCanvasStatus(4)
                self.limparCanvasDica(None)
                manaRestore = self.bot.restoreMana(0)

                self.lbDica["text"] = f"MODO DEFENSIVO\n\nMana : +{manaRestore}"

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

                newLatATTK, newLatDEF, manaItens, textLbDica = self.bot.userItens(randomLatenciaAtaque, randomLatenciaDefesa, attackBOT)

                self.escreverNoCanvasDica(None, attackBOT.getDados(), '#ec352e')
                self.setLBItensUsados(textLbDica)

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
                        manaRestore = self.bot.restoreMana(danoReal)

                        # RESTAURA MONEY
                        moneyResrore = System.calculeteRestareMoney(type="an", dano=danoReal)
                        self.bot.money += moneyResrore

                        # SET DISLAY MONEY & MANA
                        self.setLBrestareManaMoney(manaRestore, moneyResrore)


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
                        manaRestore = self.bot.restoreMana(danoReal)

                        # RESTAURA MONEY
                        moneyResrore = System.calculeteRestareMoney(type="ac", dano=danoReal)
                        self.bot.money += moneyResrore

                        # SET DISLAY MONEY & MANA
                        self.setLBrestareManaMoney(manaRestore, moneyResrore)

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
                    moneyResrore = System.calculeteRestareMoney(type="f", dano=0)
                    self.player.money += moneyResrore

                    # SET DISLAY MONEY & MANA
                    self.setLBrestareManaMoney(0, moneyResrore)

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
        self.limparCanvasDica(None)
        self.lbDica.configure(fg="white")
        self.lbDica["text"] = self.player.sword.getDados()

    def setCanvasDICAShield(self, event):
        self.limparCanvasDica(None)
        self.lbDica.configure(fg="white")
        self.lbDica["text"] = self.player.shield.getDados()

    def setCanvasDICAInventario(self, event):
        self.limparCanvasDica(None)
        txt = "INVENTÁRIO\n"
        for item in self.player.inventory:
            txt += f"{item.name.upper()} x{item.quatidade}\n"
        txt+=f"\nU${self.player.money}"
        self.lbDica["text"] = txt

    def gerarRelatorio(self):
        return [self.damageTotal, self.damageMagico, self.damageFisico, self.CONTAttackFalhos, self.CONTAttackCriticos,
                self.CONTAttackNormais, self.CONTAttack, self.FalhaDefesa, self.damageMagicoSofrido,
                self.damageFisicoSofrido,
                self.damageMagicoDefendido, self.damageFisicoDefendido, self.manaRestaurada, self.manaGasta]

    def verificarGame(self):
        if self.player.hp <= 0:
            time.sleep(1)
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
            time.sleep(1)
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
            self.lbDica["text"] = f"MODO DEFENSIVO\n\nMana : +{manaRestore}"

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
    def abrirTelaInicio(self, event):
        self.root.destroy()
        TelaInicio().construtor()

    def abrirTelaOption(self, status):
        self.root.destroy()
        d = DAO()
        userPlayer.addPartida(self.player.name, self.bot.name, d.gerarSTR(self.gerarRelatorio()), "win" if status else "low")

        TelaOption(self.player, self.gerarRelatorio(), status).construtor()

    def abrirTelaItens(self, event):
        self.root.destroy()
        tela = TelaItens(self.player, self.bot, self.Alternar, self.gerarDic())
        tela.voltar = None
        tela.btVolta["image"] = PhotoImage(file="DirPNG/#.png")
        tela.construtor()
    def knock(self, attack):
        self.limparCanvasDica(None)
        if self.Alternar:
            # o numero randomico para a latencia
            randomLatenciaAtaque = randint(0, 9)
            self.setDisplay(randomLatenciaAtaque, self.displayLatencia)

            randomLatenciaDefesa = randint(0, 9)
            self.setDisplay(randomLatenciaDefesa, self.displayLatenciaDef)

            newLatATTK, newLatDEF, manaItens, textLbDica = self.player.userItens(randomLatenciaAtaque,randomLatenciaDefesa,attack)

            self.escreverNoCanvasDica(None, attack.getDados(), '#ec352e')
            self.setLBItensUsados(textLbDica)
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
                        moneyResrore = System.calculeteRestareMoney(type="an", dano=danoReal)
                        self.player.money += moneyResrore

                        #SET DISLAY MONEY & MANA
                        self.setLBrestareManaMoney(manaRestore,moneyResrore)

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
                        moneyResrore = System.calculeteRestareMoney(type="ac", dano=danoReal)
                        self.player.money += moneyResrore

                        # SET DISLAY MONEY & MANA
                        self.setLBrestareManaMoney(manaRestore, moneyResrore)

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
                moneyResrore = System.calculeteRestareMoney(type="f", dano=0)
                self.player.money += moneyResrore

                # SET DISLAY MONEY & MANA
                self.setLBrestareManaMoney(0, moneyResrore)

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
            self.lbDica["text"] = self.stringERRO
            self.setCanvasStatus(-2)

    def limparCanvasDica(self, event):
        self.lbDica["text"] = ""
        self.lbRestareManaMoney["text"] = ""
        self.lbItensUsados["text"] = ""

    def setLBrestareManaMoney(self,mana, money):
        txt = f"RESTORE\n\nMANA:{mana}\nMONEY: {money}"
        self.lbRestareManaMoney["text"] = txt
    def setLBItensUsados(self, strItensUsados):
        txt = f"ITENS USADOS\n{strItensUsados}"
        self.lbItensUsados["text"] = txt

    def escreverNoCanvasDica(self, event, txt, cor="white"):
        self.limparCanvasDica(None)
        self.lbDica.configure(fg=cor)
        self.lbDica["text"] = txt

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")

        ## Nivel 1 - Front
        self.canvas_main.pack(side=BOTTOM)
        self.canvas_player.pack(side=LEFT)
        self.canvas_mid.pack(side=LEFT)
        self.canvas_bot.pack(side=LEFT)

        #List de ataques do player
        attacksPlayer = self.player.sword.getAttack()

        # EVENTOS NO TECLADO
        self.root.bind(self.teclasConfig["Inventário"], self.setCanvasDICAInventario)
        self.root.bind(self.teclasConfig["compraInventário"], self.abrirTelaItens)
        self.root.bind(self.teclasConfig["attkBOT"], lambda event : self.actionBOT())
        self.root.bind(self.teclasConfig["attk1-dica"],
                       lambda event, atk=attacksPlayer[0]: self.escreverNoCanvasDica(event, atk.getDados()))
        self.root.bind(self.teclasConfig["attk2-dica"],
                       lambda event, atk=attacksPlayer[1]: self.escreverNoCanvasDica(event, atk.getDados()))
        self.root.bind(self.teclasConfig["attk3-dica"],
                       lambda event, atk=attacksPlayer[2]: self.escreverNoCanvasDica(event, atk.getDados()))
        self.root.bind(self.teclasConfig["DadosArmadura"], self.setCanvasDICAShield)
        self.root.bind(self.teclasConfig["DadosEspada"], self.setCanvasDICASword)

        self.root.bind("<Escape>", self.abrirTelaInicio)

        self.root["bg"] = "Black"


        self.lbTurnoPlayer.pack()
        self.lbPlAYER.pack()

        self.lbTurnoBot.pack()
        self.lbBtBOT.pack()

        # Atribuindo a função de ataque ao botão de imagens do bot
        self.lbBtBOT["command"] = self.actionBOT

        self.nomePlAYER.pack()

        self.nomeBOT.pack()

        self.swordPlAYER.pack()
        self.swordPlAYER.bind("<Enter>", self.setCanvasDICASword)
        self.swordPlAYER.bind("<Leave>", self.limparCanvasDica)

        self.swordBOT.pack()

        self.shieldPlayer.pack()
        self.shieldPlayer.bind("<Enter>", self.setCanvasDICAShield)
        self.shieldPlayer.bind("<Leave>", self.limparCanvasDica)

        self.shieldBOT.pack()

        self.canvas_line_shop_inve.pack()
        self.lbInventarioPlayer.pack(side=LEFT)
        self.lbShop.pack(side=LEFT)
        self.lbInventarioBOT.pack()

        # Atribuindo a abertura da tela Compra itens
        self.lbShop.bind("<Button-1>", self.abrirTelaItens)
        self.lbShop.bind("<Enter>",
                           lambda event, txt="COMPRE NOVOS ITENS\nPARA O INVENTÁRIO": self.escreverNoCanvasDica(event,
                                                                                                                txt))
        self.lbShop.bind("<Leave>", self.limparCanvasDica)

        self.lbInventarioPlayer.bind("<Enter>", self.setCanvasDICAInventario)
        self.lbInventarioPlayer.bind("<Leave>", self.limparCanvasDica)

        self.lbInventarioBOT.bind("<Enter>", self.setCanvasDICAinfoBOT)
        self.lbInventarioBOT.bind("<Leave>", self.limparCanvasDica)

        self.lbRestareManaMoney.pack(side=LEFT)
        self.canvasAttackDica.pack(side=LEFT)
        self.lbItensUsados.pack(side=LEFT)

        #Imagem Inventario & compra itens
        self.lbInventarioPlayer.create_image(41, 41, image=self.imageInventario)
        self.lbInventarioPlayer.image = self.imageInventario

        self.lbShop.create_image(41, 41, image=self.imageShop)
        self.lbShop.image = self.imageShop

        self.lbInventarioBOT.create_image(41,41, image=self.imageInventario)
        self.lbInventarioBOT.image = self.imageInventario

        recuo = 20
        # Display LIFE PLAYER
        self.lbLifePlayer.pack()
        self.canvas_display_life_player.pack()
        for j in range(len(self.displayLifePlayer)):
            self.displayLifePlayer[j].config(bg="Black")
            self.displayLifePlayer[j].pack(side=LEFT)

        self.lbManaPlayer.pack()
        self.canvas_display_mana_player.pack()
        for j in range(len(self.displayManaPlayer)):
            self.displayManaPlayer[j].config(bg="Black")
            self.displayManaPlayer[j].pack(side=LEFT)


        # Display LIFE BOT
        self.lbLifeBOT.pack()
        self.canvas_display_life_bot.pack()
        for j in range(len(self.displayLifeBOT)):
            self.displayLifeBOT[j].config(bg="Black")
            self.displayLifeBOT[j].pack(side=LEFT)

        self.lbManaBOT.pack()
        self.canvas_display_mana_bot.pack()
        for j in range(len(self.displayManaBOT)):
            self.displayManaBOT[j].config(bg="Black")
            self.displayManaBOT[j].pack(side=LEFT)

        # DANO REAL FRONT
        self.lbDanoReal.pack(side=LEFT)
        self.lbDanoReal.bind("<Enter>",
                             lambda event, txt=self.stringDanoReal: self.escreverNoCanvasDica(event, txt))
        self.lbDanoReal.bind("<Leave>", self.limparCanvasDica)
        # DISPLAY DL
        for j in range(len(self.displayDanoReal)):
            self.displayDanoReal[j].config(bg="Black")
            self.displayDanoReal[j].pack(side=LEFT)

        # LATENCIA ATTACK FRONT
        self.lbLatencia.pack(side=LEFT)
        self.lbLatencia.bind("<Enter>",
                             lambda event, txt=self.stringRandLantATK: self.escreverNoCanvasDica(event, txt))
        self.lbLatencia.bind("<Leave>", self.limparCanvasDica)

        self.displayLatencia[0].config(bg="Black")
        self.displayLatencia[0].pack(side=LEFT)

        # LATENCIA DEFF FRONT
        self.lbLatenciaDef.pack(side=LEFT)
        self.lbLatenciaDef.bind("<Enter>",
                                lambda event, txt=self.stringRandLantDEF: self.escreverNoCanvasDica(event, txt))
        self.lbLatenciaDef.bind("<Leave>", self.limparCanvasDica)

        self.displayLatenciaDef[0].config(bg="Black")
        self.displayLatenciaDef[0].pack(side=LEFT)

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

        # Construindo CANVAS MID
        self.canvasStatus.pack(anchor=N)
        self.setCanvasStatus(-1)
        self.canvas_mid_info.pack()
        self.canvas_mid_random.pack(side=BOTTOM)
        self.canvas_mid_danoReal.pack(side=BOTTOM)

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
        self.margeY = 250
        self.x = 565
        self.y = 350
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
        t.p1 = System.choosePlayer(nameChamp=self.player.name)
        t.lb["image"] = t.imagemLabelBOT
        t.ADDbtAlterStrategyBot()
        t.ADDimageCanvas(t.canvasNamePlayer, t.p1.imageID)
        t.construtor()

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")
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
        self.root.title("Blood Blade Society")
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

        ##### Back-End
        ############################################
        self.listItens = []

        self.player = player

        # VARIÁVEIS TEMPORÁRIAS
        self.bot = bot
        self.alternar = alternar
        self.dicInfo = dicInfo

        ## CAMINHO DO DIRETÓRIO PARA O NUMROS GOLD
        self.caminhoDirNum = "DirPNG/DirPNGnumber/numberGold/"
        ############################################

        ##### Front-End
        ############################################

        # Canvas Desenho

        self.canvasMain = Canvas(self.root, bg = "Black", highlightbackground="Black")

        self.canvas_bts = Canvas(self.canvasMain, bg = "Black", highlightbackground="Black")
        self.canvas_div_v_1 = Canvas(self.canvas_bts, width=5,height=15, bg = "Black", highlightbackground="Black")

        self.canvas_line1 = Canvas(self.canvas_bts, bg = "Black", highlightbackground="Black")
        self.canvas_div1_h_1 = Canvas(self.canvas_line1, width=5, height=5, bg="Black", highlightbackground="Black")
        self.canvas_div1_h_2 = Canvas(self.canvas_line1, width=5,height=5, bg="Black", highlightbackground="Black")

        self.canvas_div_v_2 = Canvas(self.canvas_bts,  width=5,height=15, bg="Black", highlightbackground="Black")

        self.canvas_line2 = Canvas(self.canvas_bts, bg="Black", highlightbackground="Black")
        self.canvas_div2_h_1 = Canvas(self.canvas_line2, width=5,height=5, bg="Black", highlightbackground="Black")
        self.canvas_div2_h_2 = Canvas(self.canvas_line2, width=5,height=5, bg="Black", highlightbackground="Black")

        self.canvas_div_v_3 = Canvas(self.canvas_bts,  width=5,height=15, bg="Black", highlightbackground="Black")

        self.canvaLayaot = Canvas(self.canvasMain, bg="Black", highlightbackground="Black")
        self.canvas_line_display = Canvas(self.canvaLayaot, bg="Black", highlightbackground="Black")

        # CONFIG
        self.margeEX_x = 50
        self.margeEX_y = 130
        self.margeIN_x = 340
        self.margeIN_y = 210
        self.fontFixedsys15 = font.Font(family='Fixedsys', size=15)
        self.fontFixedsys25 = font.Font(family='Fixedsys', size=17)

        # IMAGENS
        self.imageLb = PhotoImage(
            file="DirPNG/escolhaItens.png"
        )
        self.lbTitulo = Label(self.canvas_bts, image=self.imageLb, highlightbackground="Black", bg="black")

        self.imageLbSimbol = PhotoImage(
            file="DirPNG/DirPNGnumber/numberGold/u.png"
        )
        self.lbSimbol = Label(self.canvas_line_display, width=80, height=80, image=self.imageLbSimbol, highlightbackground="Black",
                              bg="Black")

        # CANVAS PRINCIPAL DE APRESENTAÇÃO DO ITEM
        self.canvasImage = Canvas(self.canvaLayaot, width=250, height=250, bg="Black", highlightbackground="Black")
        self.lb = Label(self.canvaLayaot, width=25, height=15, font=self.fontFixedsys25, bg="Black", fg="white")

        # BOTÃOES DE COMPRA DOS ITENS
        self.bt1 = Button(self.canvas_line1, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt2 = Button(self.canvas_line1, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt3 = Button(self.canvas_line1, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt4 = Button(self.canvas_line2, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt5 = Button(self.canvas_line2, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)
        self.bt6 = Button(self.canvas_line2, width=25, height=7, bg="#ec352e",
                          fg="Black", font=self.fontFixedsys15)

        # LISTA DE LAYAOT DOS BOTÕES
        self.listBt = [[self.bt1, self.canvas_div1_h_1, self.bt2, self.canvas_div1_h_2,self.bt3],
                       [self.bt4, self.canvas_div2_h_1, self.bt5, self.canvas_div2_h_2, self.bt6]]

        # DISPLAY MONEY
        self.c1 = Canvas(self.canvas_line_display, width=80, height=80, highlightbackground="Black", bg="black")
        self.c2 = Canvas(self.canvas_line_display, width=80, height=80, highlightbackground="Black", bg="black")
        self.c3 = Canvas(self.canvas_line_display, width=80, height=80, highlightbackground="Black", bg="black")
        self.c4 = Canvas(self.canvas_line_display, width=80, height=80, highlightbackground="Black", bg="black")
        self.displayMoney = [self.c1, self.c2, self.c3, self.c4]

        # BOTÃO DE ATUALIZAÇÃO DOS ITENS
        self.imageBtCicle = PhotoImage(file="DirPNG/cicle.png")
        self.btCicle = Button(self.root, width=80, height=80, border=0,bg="black", image=self.imageBtCicle)

        # BOTÃO PARA CONTINUAR
        self.image = PhotoImage(
            file="DirPNG/continue.png"
        )
        self.btContinuar = Button(self.canvas_bts, image=self.image, width=400, height=200, bg="black", border=0)

        # BOTÃO PARA VOLTAR
        self.backPNG = PhotoImage(
            file="DirPNG/backPNG.png")
        self.btVolta = Button(self.root, image=self.backPNG, bg="Black", highlightbackground="Black", border=0)

        ############################################

    def voltar(self):
        '''
        FUNÇÃO PARA ABRIR A TELA DE ESCOLHA DE PLAYER
        :return:
        '''
        self.root.destroy()
        t = TelaEscolhaBot()
        t.p1 = self.player
        t.ADDimageCanvas(t.canvasNamePlayer,self.player.imageID)
        t.construtor()


    def dinheiroERRO(self):
        '''
        FUNÇÃO PARA EXIBIR O ERRO - FALTA DE DINHEIRO- NA COMPRA DOS ITENS
        :return:
        '''
        self.lb["text"] = "VOCÊ NÃO POSSUE MOEDAS\nPARA COMPRAR ESSE ITEM"

    def addItem(self, item, bt):
        if self.player.money >= item.valor:

            userPlayer.addBuyItens(item.name)

            self.player.addItem(item)
            self.lb["text"] = f"ITEM {item.name.upper()}\nCOMPRADO COM SUCESSO!"
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
    def ADDbts(self):
        self.listItens = System.filterItens()
        cont = 0
        for line in range(len(self.listBt)):
            for colunn in range(len(self.listBt[line])):
                if (self.listBt[line][colunn].__class__ is Button):
                    self.listBt[line][colunn]["bg"] = "#ec352e"
                    self.listBt[line][colunn]["text"] = f'''{self.listItens[cont].name.upper()}\n\nx{self.listItens[
                        cont].quatidade}\n{self.listItens[cont].valor}U$'''
                    self.listBt[line][colunn].bind("<Enter>",
                                                   lambda event, item=self.listItens[cont]: self.setLABEitem(event, item))
                    self.listBt[line][colunn].bind("<Leave>", self.setLABEitem)
                    self.listBt[line][colunn]["command"] = partial(self.addItem, self.listItens[cont],
                                                                   self.listBt[line][colunn])
                    cont += 1
                self.listBt[line][colunn].pack(side=LEFT)
    def FORGETbts(self):
        for line in range(len(self.listBt)):
            for colunn in range(len(self.listBt[line])):
                self.listBt[line][colunn].place_forget()

    def SetItensTela(self):
        self.FORGETbts()
        self.ADDbts()

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")
        self.root["bg"] = "Black"

        # Eventos TECLADOS
        self.root.bind("<Return>", lambda event: self.abrirTelaMain())

        self.btCicle.pack(anchor=NE)
        self.canvasMain.pack()
        self.btVolta.pack(side=BOTTOM, anchor=SW)

        self.canvas_bts.pack(side=LEFT)
        self.canvaLayaot.pack(side=LEFT)

        # Canvas BTs
        self.lbTitulo.pack()
        self.canvas_div_v_1.pack()
        self.canvas_line1.pack()
        self.canvas_div_v_2.pack()
        self.canvas_line2.pack()
        self.canvas_div_v_3.pack()
        self.btContinuar.pack()

        # Canvas Itens
        self.canvasImage.pack()
        self.lb.pack()
        self.canvas_line_display.pack()
        self.lbSimbol.pack(side=LEFT)
        for index in range(len(self.displayMoney)):
            self.displayMoney[index].pack(side=LEFT)

        self.btContinuar["command"] = self.abrirTelaMain
        self.btCicle["command"] = self.SetItensTela
        self.btVolta["command"] = self.voltar

        #ADD BUTTONS
        self.ADDbts()

        self.setDisplay(str(self.player.money), self.displayMoney)

        self.root.mainloop()

class TelaTutor:
    def __init__(self):
        self.root = Tk()

        self.fontFixedsys12 = font.Font(family='Fixedsys', size=12)

        self.texto = scrolledtext.ScrolledText(self.root,width=190,height=60, font=self.fontFixedsys12, bg="Black",
                                               fg="white")

        arp = open("TutorialTEXT.txt", "r")
        txt = arp.readlines()
        self.texto.insert(INSERT, txt)
        self.texto.configure(state='disabled')

    def voltar(self):
        self.root.destroy()
        TelaInicio().construtor()

    def construtor(self):
        self.root.attributes('-fullscreen',True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")
        self.root["bg"] = "Black"

        self.root.bind("<Key>", lambda event: self.voltar())

        self.texto.pack()

        self.root.mainloop()

class TelaCadastro:
    def __init__(self):
        self.root = Tk()
        self.dao = DAO()

        self.fontFixedsys12 = font.Font(family='Fixedsys', size=14)
        self.imageLb = PhotoImage(
            file="DirPNG/CADASTRO.png"
        )
        self.lbTitle = Label(self.root, image=self.imageLb, highlightbackground="Black", bg="black")

        self.aux = Canvas(self.root, bg="Black", highlightbackground="Black", width=10, height=200)
        self.aux2 = Canvas(self.root, bg="Black", highlightbackground="Black", width=10, height=20)
        self.canvas_entry_Nome = Canvas(self.root, bg="Black", highlightbackground="Black")
        self.canvas_entry_Senha = Canvas(self.root, bg="Black", highlightbackground="Black")

        self.entryNome = Entry(self.canvas_entry_Nome, width=20, font=self.fontFixedsys12)
        self.lbNome = Label(self.canvas_entry_Nome,width=10,height=1, font=self.fontFixedsys12, bg="Black",
                                               fg="white", text="Nome")
        self.entrySenha = Entry(self.canvas_entry_Senha, width=20, font=self.fontFixedsys12)
        self.lbSenha = Label(self.canvas_entry_Senha, width=10, height=1, font=self.fontFixedsys12, bg="Black",
                            fg="white", text="Senha")
        self.canvas = Canvas(self.root, width=200, height=20, highlightbackground="Black", bg="white")

        self.lbStatus = Label(self.canvas,width=45,height=1, font=font.Font(family='Fixedsys', size=10), bg="Black",
                                               fg="white", text="")

        self.btCadastrar = Button(self.root, width=35,height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                                  text="CADASTRAR", font=font.Font(family='Fixedsys', size=15))
        self.btLogar = Button(self.root, width=30, height=1, bg="#ec352e", fg="Black", highlightbackground="Black",
                                  text="TELA LOGIN", font=font.Font(family='Fixedsys', size=15))

    def cadastrar(self):
        nome = self.entryNome.get().strip()
        senha = self.entrySenha.get().strip()
        if nome == "" or senha == "":
            # CAMPO VAZIO
            self.lbStatus["fg"] = "red"
            self.lbStatus["text"] = "Campo vazio".upper()
        else:
            if self.dao.cadastrar(nome,senha):
                # CADASTRO CONFIRMADO
                self.lbStatus["fg"] = "green"
                self.lbStatus["text"] = "Cadastro confirmado".upper()
            else:
                # NOME JÁ EXISTENTE
                self.lbStatus["fg"] = "red"
                self.lbStatus["text"] = "Nome já existente".upper()

    def abrirTelaLogin(self):
        self.root.destroy()
        TelaLogin().construtor()


    def construtor(self):
        self.root.attributes('-fullscreen', True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")
        self.root["bg"] = "Black"

        self.lbTitle.pack()
        self.aux.pack()
        self.canvas_entry_Nome.pack()
        self.aux2.pack()
        self.canvas_entry_Senha.pack()

        self.entryNome.pack(anchor=NW, side=RIGHT)
        self.lbNome.pack(anchor=NE, side=LEFT)

        self.entrySenha.pack(anchor=NW, side=RIGHT)
        self.lbSenha.pack(anchor=NE, side=LEFT)

        self.canvas.pack()
        self.lbStatus.pack(anchor=CENTER,side=TOP)

        self.btCadastrar.pack()
        self.btCadastrar["command"] = self.cadastrar
        self.root.bind("<Return>", lambda event:self.cadastrar())

        self.btLogar.pack(side=RIGHT,anchor=S)
        self.btLogar["command"] = self.abrirTelaLogin

        self.root.mainloop()

class TelaLogin:
    def __init__(self):
        self.root = Tk()
        self.dao = DAO()

        self.fontFixedsys12 = font.Font(family='Fixedsys', size=14)
        self.imageLb = PhotoImage(
            file="DirPNG/LOGIN.png"
        )
        self.lbTitle = Label(self.root, image=self.imageLb, highlightbackground="Black", bg="black")

        self.aux = Canvas(self.root, bg="Black",highlightbackground="Black", width=10, height=200)
        self.aux2 = Canvas(self.root, bg="Black", highlightbackground="Black", width=10, height=20)
        self.canvas_entry_Nome = Canvas(self.root, bg="Black",highlightbackground="Black")
        self.canvas_entry_Senha = Canvas(self.root, bg="Black", highlightbackground="Black")


        self.entryNome = Entry(self.canvas_entry_Nome, width=20, font=self.fontFixedsys12)
        self.lbNome = Label(self.canvas_entry_Nome, width=10, height=1, font=self.fontFixedsys12, bg="Black",
                            fg="white", text="Nome")

        self.entrySenha = Entry(self.canvas_entry_Senha, width=20, font=self.fontFixedsys12)
        self.lbSenha = Label(self.canvas_entry_Senha, width=10, height=1, font=self.fontFixedsys12, bg="Black",
                             fg="white", text="Senha")

        self.canvas = Canvas(self.root, width=200, height=20, highlightbackground="Black", bg="white")

        self.lbStatus = Label(self.canvas, width=45, height=1, font=font.Font(family='Fixedsys', size=10), bg="Black",
                              fg="white", text="")

        self.btLogar = Button(self.root, width=35, height=2, bg="#ec352e", fg="Black", highlightbackground="Black",
                              text="FAZER LOGIN", font=font.Font(family='Fixedsys', size=15))

        self.btCadastra = Button(self.root, width=30, height=1, bg="#ec352e", fg="Black", highlightbackground="Black",
                              text="TELA DE CADASTRO", font=font.Font(family='Fixedsys', size=15))
        self.btSair = Button(self.root, width=30, height=1, bg="#ec352e", fg="Black", highlightbackground="Black",
                                 text="SAIR", font=font.Font(family='Fixedsys', size=15))
    def logar(self):
        nome = self.entryNome.get().strip()
        senha = self.entrySenha.get().strip()
        if nome == "" or senha == "":
            # CAMPO VAZIO
            self.lbStatus["fg"] = "red"
            self.lbStatus["text"] = "Campo vazio".upper()
        else:
            user = self.dao.getUser(nome)
            if user == None:
                # USER NÃO EXISTENTE
                self.lbStatus["fg"] = "red"
                self.lbStatus["text"] = "usuário não existente".upper()
            elif nome.upper() != user.Nome.upper() or senha.upper() != user.Senha.upper():
                # NOME OU SENHA INCORRETOS
                self.lbStatus["fg"] = "red"
                self.lbStatus["text"] = "senha incorreto".upper()
            else:
                # LOGADO
                global userPlayer
                userPlayer = user
                self.root.destroy()
                TelaInicio().construtor()
    def abrirTelaCadastro(self):
        self.root.destroy()
        TelaCadastro().construtor()

    def sair(self):
        self.root.destroy()
        sys.exit()

    def construtor(self):
        self.root.attributes('-fullscreen', True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")
        self.root["bg"] = "Black"

        self.lbTitle.pack()
        self.aux.pack()
        self.canvas_entry_Nome.pack()
        self.aux2.pack()
        self.canvas_entry_Senha.pack()

        self.entryNome.pack(anchor=NW,side=RIGHT)
        self.lbNome.pack(anchor=NE,side=LEFT)

        self.entrySenha.pack(anchor=NW,side=RIGHT)
        self.lbSenha.pack(anchor=NE,side=LEFT)

        self.canvas.pack()
        self.lbStatus.pack(anchor=CENTER,side=TOP)

        self.btLogar.pack()
        self.btLogar["command"] = self.logar
        self.root.bind("<Return>", lambda event : self.logar())

        self.btSair.pack(side=BOTTOM, anchor=W)
        self.btSair["command"] = self.sair

        self.btCadastra.pack(side=LEFT, anchor=S)
        self.btCadastra["command"] = self.abrirTelaCadastro



        self.root.mainloop()

class TelaPerfil:
    def __init__(self):
        self.root = Tk()
        self.fontFixedsys12 = font.Font(family='Fixedsys', size=17)
        self.imageLb = PhotoImage(
            file="DirPNG/PERFIL.png"
        )
        self.lbTitle = Label(self.root, image=self.imageLb, highlightbackground="Black", bg="black")

        self.imagBack = PhotoImage(file="DirPNG/backperfil.png")
        self.btVoltar = Button(self.root, image=self.imagBack, bg="Black", border=0)

        self.div_perfil = Canvas(self.root, bg="Black", highlightbackground="Black")
        self.div_h_canvas_apt = Canvas(self.root, bg="Black", width=50, height=10, highlightbackground="Black")

        #LABAL DICAS
        self.lbDicaChampFavorito = Label(self.div_perfil, font=self.fontFixedsys12, highlightbackground="Black", bg="black",
                                         fg="#ec352e",text="Player Favorito")

        nomeChamp = userPlayer.getChanpFavorito()

        imagPerfil = System.choosePlayer(nameChamp=nomeChamp).imageShowChoose if nomeChamp != None else "DirPNG/playerPerfil.png"
        self.imagePerfil = PhotoImage(file=imagPerfil)
        self.lbPerfil = Label(self.div_perfil,image=self.imagePerfil,highlightbackground="Black")

        # LABEL DICAS
        self.lbDicaRelatorio = Label(self.root,width=12, height=7, bg="Black", fg="#ec352e", highlightbackground="Black",
                                     font=self.fontFixedsys12)

        # CANVAS DO MENU PERFIL
        self.canvasRelatorio = Canvas(self.root, width=400, height=400, background="black", border=0,
                                      highlightbackground="Black")
        self.canvasOptions = Canvas(self.root, width=400, height=500, background="black", border=0,
                                      highlightbackground="Black")
        width = 24
        height = 2

        # BOTÕES DE RELATÓRIO
        self.bt0 = Button(self.canvasRelatorio, width=width, height=height, border=0, fg="black",background="#ec352e",
                          font=self.fontFixedsys12,highlightbackground="Black")
        self.bt1 = Button(self.canvasRelatorio,  width=width, height=height, border=0, fg="black",background="#ec352e",
                          font=self.fontFixedsys12,highlightbackground="Black")
        self.bt2 = Button(self.canvasRelatorio,  width=width, height=height, border=0, fg="black",background="#ec352e",
                          font=self.fontFixedsys12,highlightbackground="Black")
        self.bt3 = Button(self.canvasRelatorio,  width=width, height=height, border=0, fg="black",background="#ec352e",
                          font=self.fontFixedsys12,highlightbackground="Black")
        self.bt4 = Button(self.canvasRelatorio,  width=width, height=height, border=0, fg="black",background="#ec352e",
                          font=self.fontFixedsys12,highlightbackground="Black")

        # BOTÕES DE OPTIONS
        self.btOp0 = Button(self.canvasOptions, width=width, height=height, border=0, fg="black", background="#ec352e",
                          font=self.fontFixedsys12, highlightbackground="Black", text="WIN & LOW")
        self.btOp1 = Button(self.canvasOptions, width=width, height=height, border=0, fg="black", background="#ec352e",
                            font=self.fontFixedsys12, highlightbackground="Black", text="TYPE DAMEGE")
        self.btOp2 = Button(self.canvasOptions, width=width, height=height, border=0, fg="black", background="#ec352e",
                            font=self.fontFixedsys12, highlightbackground="Black", text="ITENS")


        # CANVAS WIN & LOW
        self.canvasOpWin = Canvas(self.root,bg="black", border=0,highlightbackground="Black")
        self.lbWin = Label(self.canvasOpWin, bg="black", fg="green", border=0, font=font.Font(family='Fixedsys', size=17))
        self.lbLow = Label(self.canvasOpWin, bg="black", fg="red", border=0,
                           font=font.Font(family='Fixedsys', size=17))
        self.photoArt = PhotoImage(file="DirPNG/logo.png")
        self.lbImage = Label(self.canvasOpWin, image=self.photoArt, highlightbackground="Black", bg="black")

        # CANVAS TIPO DANO
        """
        Construção do canvas tipo de dano (dm) e (df) são as variáveis que contem o valor do dano total do User. Com 
        base no dano que for superior é determinado a imagem do tipo de Dano
        
        "DirPNG/atk1.png" : df é meio que dm
        "DirPNG/atk3.png" : dm é meio que df
        "DirPNG/atk2.png" : são parecidos 
        
        coeficiente de variação : 0.8
        """
        self.canvasType = Canvas(self.root, bg="black", border=0, highlightbackground="Black")

        dm = userPlayer.getDM()
        df = userPlayer.getDF()

        strImage = "DirPNG/atk3.png" if dm*0.8 > df else "DirPNG/atk1.png" if df*0.8 > dm else "DirPNG/atk2.png"
        self.imageStr = PhotoImage(file=strImage)

        self.lbImageType = Label(self.canvasType, width=300,image=self.imageStr, highlightbackground="Black", bg="black")

        self.lbDM = Label(self.canvasType, bg="black", fg="#9c27a2", border=0,text=f"DANO MÁGICO\n\n{dm}",
                           font=font.Font(family='Fixedsys', size=17))
        self.lbDF = Label(self.canvasType, bg="black", fg="#d41d16", border=0, text=f"DANO FÍSICO\n\n{df}",
                          font=font.Font(family='Fixedsys', size=17))

        # CANVAS ITENS

        self.canvasItens = Canvas(self.root, bg="black", border=0, highlightbackground="Black")

        rank1,rank2,rank3 = userPlayer.getItensFavorito()

        self.canvasTop = Canvas(self.canvasItens, bg="Black",  border=0, highlightbackground="Black")
        self.canvasBotton = Canvas(self.canvasItens, bg="Black", border=0, highlightbackground="Black")

        self.div_h_itens_top_1 = Canvas(self.canvasTop, bg="Black", width=10, height=2, highlightbackground="Black")
        self.div_h_itens_top_2 = Canvas(self.canvasTop, bg="Black", width=10, height=2, highlightbackground="Black")

        self.div_h_itens_botton_1 = Canvas(self.canvasBotton, bg="Black", width=10, height=2, highlightbackground="Black")
        self.div_h_itens_botton_2 = Canvas(self.canvasBotton, bg="Black", width=10, height=2, highlightbackground="Black")

        item1 = System.getItem(rank1[0])
        item2 = System.getItem(rank2[0])
        item3 = System.getItem(rank3[0])

        self.image1 = PhotoImage(file=item1.image) if item1 is not None else PhotoImage(file="DirPNG/erroItens.png")
        self.image2 = PhotoImage(file=item2.image) if item2 is not None else PhotoImage(file="DirPNG/erroItens.png")
        self.image3 = PhotoImage(file=item3.image) if item3 is not None else PhotoImage(file="DirPNG/erroItens.png")

        txt1 = f"RANK 1\n\nNOME: {item1.name}\nCOMPRAS: {rank1[1]}x" if item1 != None else "COMPRE MAIS ITENS"
        txt2 = f"RANK 2\n\nNOME: {item2.name}\nCOMPRAS: {rank2[1]}x" if item2 != None else "COMPRE MAIS ITENS"
        txt3 = f"RANK 3\n\nNOME: {item3.name}\nCOMPRAS: {rank3[1]}x" if item3 != None else "COMPRE MAIS ITENS"

        lb1 = Label(self.canvasBotton, bg="black", fg="#ec352e", border=0,text=txt1,
                           font=font.Font(family='Fixedsys', size=17))
        lb2 = Label(self.canvasBotton, bg="black", fg="#ec352e", border=0, text=txt2,
                    font=font.Font(family='Fixedsys', size=17))
        lb3 = Label(self.canvasBotton, bg="black", fg="#ec352e", border=0, text=txt3,
                    font=font.Font(family='Fixedsys', size=17))


        lbimage1 = Label(self.canvasTop, bg="black",border=0, image=self.image1, highlightbackground="Black")
        lbimage2 = Label(self.canvasTop, bg="black",border=0, image=self.image2, highlightbackground="Black")
        lbimage3 = Label(self.canvasTop, bg="black",border=0, image=self.image3, highlightbackground="Black")

        x = 280

        lb1.pack(side=LEFT)
        self.div_h_itens_botton_1.pack(side=LEFT)
        lb2.pack(side=LEFT)
        self.div_h_itens_botton_2.pack(side=LEFT)
        lb3.pack(side=LEFT)

        lbimage1.pack(side=LEFT)
        self.div_h_itens_top_1.pack(side=LEFT)
        lbimage2.pack(side=LEFT)
        self.div_h_itens_top_2.pack(side=LEFT)
        lbimage3.pack(side=LEFT)

        self.canvasBotton.pack(side=BOTTOM)
        self.canvasTop.pack(side=TOP)



        self.listBTrelatorio = [self.bt0,self.bt1,self.bt2,self.bt3,self.bt4]

        """
        A lista (self.listBToptions) e (self.listCanvas) estão em sincronia.
        
        Cada elemento da lista (self.listBToptions) apontam para uma instância de um botão e cada elemento da lista 
        (self.listCanvas) para outra lista, composta da seguinte forma [instância de Canvas, cordenada X, cordenada Y]
        
        Cada botão da lista (self.listBToptions) ativa uma chamada da função placeCanvas(canvas, x, y) e de forma 
        sincrona cada Canvas passado como parâmetro é um elemento de mesmo index na lista (self.listCanvas)
        """

        self.listBToptions = [self.btOp0,self.btOp1, self.btOp2]
        self.listCanvas = [[self.canvasOpWin,340], [self.canvasType,250], [self.canvasItens, 180]]

    def selfAbrir(self, tela):
        tela.root.destroy()
        TelaPerfil().construtor()

    def voltar(self):
        self.root.destroy()
        TelaInicio().construtor()

    def abrirTelaRelatorio(self, name):
        global userPlayer
        listRelatorio = userPlayer.getRelatorioChanp(name)
        self.root.destroy()
        t = TelaRelatorio(listRelatorio)

        #GAMBIARA
        t.voltar = lambda :self.selfAbrir(t)

        t.construtor()

    def packCanvas(self, canvas, div_esponse, size_):
        # LIMPAR A ROOT
        for lineClearCanvas in range(len(self.listCanvas)):
            self.listCanvas[lineClearCanvas][0].pack_forget()

        div_esponse["width"] = size_
        canvas.pack(side=LEFT)

    def escreverLBPlayer(self, name):
        # LIMPAR A ROOT
        for lineClearCanvas in range(len(self.listCanvas)):
            self.listCanvas[lineClearCanvas][0].place_forget()

        txt = f"{name}\n\nVITÓRIAS: {userPlayer.getNumberWin(name)}\nDERROTAS: {userPlayer.getNumberLow(name)}\nCOMBATES: {userPlayer.getNumberCombat(name)}"
        self.lbDicaRelatorio["text"] = txt

    def limparDicaRelatorio(self):
        self.lbDicaRelatorio["text"] = ''

    def construtor(self):
        self.root.attributes('-fullscreen', True)
        self.root.focus_force()
        self.root.title("Blood Blade Society")
        self.root["bg"] = "Black"

        self.lbTitle.pack()
        self.div_perfil.pack()
        self.btVoltar.pack(side=BOTTOM, anchor=SW)
        self.btVoltar["command"] = self.voltar

        for index in range(5):
            champ = System.choosePlayer(index)
            self.listBTrelatorio[index]["text"] = champ.name
            self.listBTrelatorio[index].place(x=0,y=65*index)
            self.listBTrelatorio[index]["command"] = partial(self.abrirTelaRelatorio,champ.name)
            self.listBTrelatorio[index].bind("<Enter>", lambda event, name=champ.name: self.escreverLBPlayer(name))
            self.listBTrelatorio[index].bind("<Leave>", lambda event: self.limparDicaRelatorio())

        # CONSTRUINDO CANVAS WIN & LOW
        self.lbWin.pack(side=LEFT)
        self.lbWin["text"] = f"VITÓRIAS\n\n{userPlayer.getNumberWin()}"

        self.lbImage.pack(side=LEFT)
        self.lbLow.pack(side=RIGHT)
        self.lbLow["text"] = f"DERROTAS\n\n{userPlayer.getNumberLow()}"

        # CONSTRUINDO CANVAS TYPE

        self.lbDF.pack(side=LEFT)
        self.lbImageType.pack(side=LEFT)
        self.lbDM.pack(side=RIGHT)

        self.lbDicaRelatorio.pack(anchor=CENTER, side=BOTTOM)


        for index in range(len(self.listBToptions)):
            self.listBToptions[index].pack()
            canvas, size_ = self.listCanvas[index]
            self.listBToptions[index]["command"] = lambda c=canvas, s=size_: self.packCanvas(c, self.div_h_canvas_apt, s)



        self.canvasRelatorio.pack(side=LEFT)
        self.canvasOptions.pack(side=RIGHT)

        self.div_h_canvas_apt.pack(side=LEFT)

        self.lbDicaChampFavorito.pack()
        self.lbPerfil.pack()
        self.root.mainloop()
