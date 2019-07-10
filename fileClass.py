from random import randint, shuffle
from operator import itemgetter
import winsound
import sys

Config = {
    "RED": '\033[31m',
    "GREEN": '\033[32m',
    "BLUE": '\033[34m',
    "CIANO": '\033[36m',
    "MAGETA": '\033[35m',
    "YELLOW": '\033[33m',
    "BLACK": '\033[30m',
    "WHITE": '\033[37m',
    'NEGRITO': '\033[1m',
    'RESET': '\033[0;0m'
}


class System:
    @staticmethod
    def listPlayer():
        return ["Ichigo Kurosaki", "Killer Bee", "Xena", "Roronoa Zoro", "Gohan"]

    @staticmethod
    def printPlayers():
        player = System.listPlayer()
        for index in range(len(player)):
            print("%i - %s \n" % (index, player[index]))

    @staticmethod
    def printPlayer(player, flagConfig):
        print(Config[flagConfig], end="")
        print('''

            Nome : {}
            Vida : {}
            Mana : {}
            Sword : {}
            Shield : {}

        '''.format(player.name, player.hp, player.mana, player.sword.name, player.shield.name))
        print(Config['RESET'], end="")

    @staticmethod
    def print(st, flagConfig):
        print(Config[flagConfig])
        print(st)
        print(Config['RESET'])

    @staticmethod
    def printKnock(danoVerdadeiro, mana, attack, player, advPlayer):
        print(Config["BLACK"], Config['NEGRITO'], end='')
        print(''' {} 
        Utiliza {} para atacar {} '''.format(player.name.upper(), attack.name.upper(), advPlayer.name.upper()))

        print(Config["BLACK"], Config['NEGRITO'], end='')
        print("Dano verdadeiro :", end='')
        print(Config["RED"], end='')
        print(danoVerdadeiro)

        print(Config["CIANO"])
        print('''
        HP {} : {}
        '''.format(advPlayer.name.upper(), advPlayer.hp))

        print(Config["BLUE"], end='')
        print("MANA RESTAURADA : {}".format(mana))
        print(Config['RESET'])

    @staticmethod
    def choosePlayer(indexPlayer):
        nameChamp = System.listPlayer()[indexPlayer]
        if nameChamp == 'Ichigo Kurosaki':
            at1 = Attack(name="Getsuga Tenshou", mana=400, latencia=5, danoFisico=300, danoMagico=2000,
                         imageBT="DirPNG/atk3.png")
            at2 = Attack(name="Piercer of Heaven", mana=200, latencia=2, danoFisico=100, danoMagico=1000,
                         imageBT="DirPNG/atk3.png")
            at3 = Attack(name="Getsuga Jūjishō", mana=350, latencia=2, danoFisico=250, danoMagico=1500,
                         imageBT="DirPNG/atk3.png")

            sword = Sword("Zanpakutō", at1, at2, at3,
                          imageID="DirPNG/Sword/zampakuto.png")

            shield = Shield(name="Armor Berserker", latencia=2, defesaFisica=400, defesaMagica=1500,
                            imageID="DirPNG/Shield/berserker.png")

            player = Player(name="Ichigo Kurosaki", hp=10000, mana=600, sword=sword, shield=shield, personality=[5,4,1],
                            activeStrategyMana=True,
                            activeStrategyLatAttk=False,
                            activeStrategyDMC=False,
                            activeStrategyLatDeff=True,
                            activeStrategyLife=True,
                            activeStrategyDF=False,
                            imageShow="DirPNG/Personagens/ichico.png",
                            imageID="DirPNG/Personagens/nIchigo.png",
                            imageShowChoose="DirPNG/Personagens/ICHIGO-show.png")

            player.setWAVShow("DirWAV/ICHIGOPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Killer Bee':
            at1 = Attack(name="Crumbling the skin", mana=800, latencia=6, danoFisico=3000, danoMagico=600,
                         imageBT="DirPNG/atk1.png")
            at2 = Attack(name="Life Theft", mana=250, latencia=3, danoFisico=400, danoMagico=1500,
                         imageBT="DirPNG/atk3.png")
            at3 = Attack(name="Samehada and the 7 swords", mana=500, latencia=3, danoFisico=1000,
                         danoMagico=1500,
                         imageBT="DirPNG/atk2.png")

            sword = Sword("Samehada", at1, at2, at3,
                          imageID="DirPNG/Sword/samehada.png")

            shield = Shield(name="Armor of Gemini", latencia=4, defesaFisica=500, defesaMagica=1200,
                            imageID="DirPNG/Shield/gemeos.png")

            player = Player(name="Killer Bee", hp=12500, mana=1000, sword=sword, shield=shield, personality=[6,3,4],
                            activeStrategyMana=True,
                            activeStrategyLatAttk=True,
                            activeStrategyDMC=True,
                            activeStrategyLatDeff=True,
                            activeStrategyLife=True,
                            activeStrategyDF=True,
                            imageShow="DirPNG/Personagens/bee.png",
                            imageID="DirPNG/Personagens/nBee.png",
                            imageShowChoose="DirPNG/Personagens/BEE-show.png")

            player.setWAVShow("DirWAV/KILLERBEEPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Xena':
            at1 = Attack(name="Full Counter", mana=700, latencia=3, danoFisico=3000, danoMagico=500,
                         imageBT="DirPNG/atk1.png")
            at2 = Attack(name="Counter Vanish", mana=200, latencia=1, danoFisico=2000, danoMagico=0,
                         imageBT="DirPNG/atk1.png")
            at3 = Attack(name="Hellblaze", mana=400, latencia=4, danoFisico=1500, danoMagico=300,
                         imageBT="DirPNG/atk1.png")

            sword = Sword("Excalibur", at1, at2, at3,
                          imageID="DirPNG/Sword/excalibur.png")

            shield = Shield(name="Armor Knight", latencia=3, defesaFisica=1600, defesaMagica=300,
                            imageID="DirPNG/Shield/knight.png")

            player = Player(name="Xena", hp=9900, mana=1500, sword=sword, shield=shield, personality=[6,3,3],
                            activeStrategyMana=False,
                            activeStrategyLatAttk=False,
                            activeStrategyDMC=False,
                            activeStrategyLatDeff=True,
                            activeStrategyLife=True,
                            activeStrategyDF=True,
                            imageShow="DirPNG/Personagens/xena.png",
                            imageID="DirPNG/Personagens/nXena.png",
                            imageShowChoose="DirPNG/Personagens/XENA-show.png")

            player.setWAVShow("DirWAV/XENAPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Roronoa Zoro':
            at1 = Attack(name="Shishi SonSon", mana=50, latencia=1, danoFisico=1500, danoMagico=0,
                         imageBT="DirPNG/atk1.png")
            at2 = Attack(name="Sanjuroku Pound Ho", mana=200, latencia=3, danoFisico=3500, danoMagico=30,
                         imageBT="DirPNG/atk1.png")
            at3 = Attack(name="Yakkodori", mana=100, latencia=2, danoFisico=3000, danoMagico=10,
                         imageBT="DirPNG/atk1.png")

            sword = Sword("Sandai Kitetsu", at1, at2, at3,
                          imageID="DirPNG/Sword/sandaiKitetsu.png")

            shield = Shield(name="Black Armor", latencia=1, defesaFisica=2000, defesaMagica=0,
                            imageID="DirPNG/Shield/negra.png")

            player = Player(name="Roronoa Zoro", hp=11000, mana=1000, sword=sword, shield=shield, personality=[5,2,1],
                            activeStrategyMana=False,
                            activeStrategyLatAttk=True,
                            activeStrategyDMC=False,
                            activeStrategyLatDeff=True,
                            activeStrategyLife=False,
                            activeStrategyDF=True,
                            imageShow="DirPNG/Personagens/zoro.png",
                            imageID="DirPNG/Personagens/nZoro.png",
                            imageShowChoose="DirPNG/Personagens/ZORO-show.png")

            player.setWAVShow("DirWAV/ZOROPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Gohan':
            at1 = Attack(name="Fulminant Strike", mana=900, latencia=4, danoFisico=900, danoMagico=3000,
                         imageBT="DirPNG/atk3.png")
            at2 = Attack(name="Blade Combo", mana=700, latencia=1, danoFisico=920, danoMagico=1100,
                         imageBT="DirPNG/atk2.png")
            at3 = Attack(name="Rage of the Blade", mana=500, latencia=1, danoFisico=500, danoMagico=900,
                         imageBT="DirPNG/atk2.png")

            sword = Sword("Espada Z", at1, at2, at3,
                          imageID="DirPNG/Sword/espadaZ.png")

            shield = Shield(name="Metal Tech", latencia=4, defesaFisica=700, defesaMagica=600,
                            imageID="DirPNG/Shield/metalTech.png")

            player = Player(name="Gohan", hp=14000, mana=1800, sword=sword, shield=shield, personality=[5,4,2],
                            activeStrategyMana=True,
                            activeStrategyLatAttk=True,
                            activeStrategyDMC=True,
                            activeStrategyLatDeff=True,
                            activeStrategyLife=False,
                            activeStrategyDF=True,
                            imageShow="DirPNG/Personagens/gohan.png",
                            imageID="DirPNG/Personagens/nGohan.png",
                            imageShowChoose="DirPNG/Personagens/GOHAN-show.png")

            player.setWAVShow("DirWAV/GOHANPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player

    @staticmethod
    def allItens():
        return [
            Item("Dragon claws",150,5,alterDanoMagico=200,alterLatenciaAttk=9, image="DirPNG/Itens/Dragonclaws.png"),
            Item("3 warriors of David",600,3,alterLatenciaDeff=-5,alterDanoFisico=700, alterDanoMagico=300,
                 image="DirPNG/Itens/3warriorsofDavid.png"),
            Item("Adam's ring",200,5,alterLatenciaAttk=9,alterLatenciaDeff=4, alterLife=150,
                 image="DirPNG/Itens/Adamsring.png"),
            Item("living shield", 200, 1,alterLife=2500, alterDefesaMagica=550,alterLatenciaAttk=-1,
            image="DirPNG/Itens/livingshield.png"),
            Item("helmet of Ulysses", 250, 1, alterDefesaFisica=1000, image="DirPNG/Itens/helmetofUlysses.png"),
            Item("Loki's dagger", 350, 1, alterLife=3000, alterMana=1000, image="DirPNG/Itens/Lokisdagger.png"),
            Item("breastplate", 400, 1, alterLife=5000,alterDefesaMagica=500, alterDefesaFisica=500,
                 image="DirPNG/Itens/breastplate.png"),
            Item("hermes dagger", 50, 1, alterLatenciaDeff=-5, image="DirPNG/Itens/hermesdagger.png"),
            Item("apollo dagger", 250, 3, alterLatenciaAttk=9, alterDefesaFisica=-50, alterLatenciaDeff=2,
                 alterDanoFisico=200, image="DirPNG/Itens/apollodagger.png"),
            Item("Spiked Shoulder Armor", 350, 1, alterDanoFisico=500,alterLatenciaAttk=6,alterMana=200,alterDefesaFisica=400,
                 image="DirPNG/Itens/spikedshoulderarmor.png"),
            Item("trident of jaime", 450, 1, alterDanoMagico=1500, alterLatenciaDeff=-9, alterMana=-400, image="DirPNG/Itens/tridentofjaime.png"),
        ]

    @staticmethod
    def filterItens():
        lista = System.allItens()
        shuffle(lista)
        return lista[0:6]

    @staticmethod
    def calculeteRestareMoney(type="f",dano=0):
        base = 25
        extraType = 5 if type == "f" else 25 if type == "an" else 55 if type == "ac" else 0
        extraDano = 5 if dano < 1000 else 7 if dano < 2000 else 10 if dano < 3000 else 15 if dano < 4000 else 30 if dano < 5000 else 45
        return base+extraType+extraDano

    @staticmethod
    def calculeteDamageShield(player, attack):
        '''
        Funcao responsavel por CALCULAR o dano com base na ARMADURA do adversario
        player : Type (Player)
        attack : Type (Attack)
        return: INT
        '''
        # obter valores de armadura do jogador adversario
        defesaMagica = player.shield.defesaMagica
        defesaFisica = player.shield.defesaFisica
        # obter valores do dano causado pelo ataque
        danoMagico = attack.danoMagico
        danoFisico = attack.danoFisico
        # calculando valores de dano ao hp adversario pela subtracoo (dano - armadura)
        danoRealMagico = danoMagico - defesaMagica
        danoRealFisico = danoFisico - defesaFisica

        # validando os valores de retorno da funcao
        if danoRealMagico >= 0 and danoRealFisico >= 0:
            # significa que o ataque foi efetivo tanto de modo magico como fisico
            danoReal = [danoRealFisico, danoRealMagico]
            return danoReal
        elif danoRealMagico < 0 and danoRealFisico < 0:
            # significa que o ataque foi totalmente defendido
            return [0,0]
        else:
            # significa que apenas uma das formas foi efetiva ao realizar o dano
            if danoRealMagico < 0:
                # Dano Fisico foi efetivo
                return [danoRealFisico, 0]
            else:
                # Dano Magico foi efetivo
                return [0, danoRealMagico]

    @staticmethod
    def calculeteDamage(attack):
        '''
        Funcao responsavel por CALCULAR o dano sem a ARMADURA do adversario
        attack : Type (Attack)
        return: INT
        '''
        # obter valores do dano causado pelo ataque
        danoMagico = attack.danoMagico
        danoFisico = attack.danoFisico

        danoReal = [danoFisico, danoMagico]

        return danoReal


class Player:
    def __init__(self, name, hp, mana, sword, shield, personality=[4,1,3],
                 activeStrategyMana = False,
                 activeStrategyLatAttk=False,
                 activeStrategyDMC=False,
                 activeStrategyLatDeff=False,
                 activeStrategyLife=False,
                 activeStrategyDF=False,
                 imageShow = "DirPNG/matrix-wallpaper.png",imageID="DirPNG/matrix-wallpaper.png",
                 imageShowChoose = "DirPNG/matrix-wallpaper.png"):
        self.name = name
        self.hp = hp
        self.sword = sword
        self.shield = shield
        self.mana = mana
        self.imageShow = imageShow
        self.imageID = imageID
        self.imageShowChoose = imageShowChoose
        self.arqWAV = ["", ""]
        self.inventory = []
        self.money = 600
        self.personality = {"importanciaDANO": personality[0],
                            "importanciaMANA": personality[1],
                            "importanciaLATENCIA": personality[2],
                            "activeStrategyMana" : activeStrategyMana,
                            "activeStrategyLatAttk": activeStrategyLatAttk,
                            "activeStrategyDMC" : activeStrategyDMC,
                            "activeStrategyLatDeff": activeStrategyLatDeff,
                            "activeStrategyLife":activeStrategyLife,
                            "activeStrategyDF":activeStrategyDF
                            }

    def __str__(self, ):
        return ("Nome: " + str(self.name) + "\nHP: " + str(self.hp) + "\nSword: " + str(
            self.sword.name) + "\nShield: " + str(self.shield.name) + "\nMana: " + str(self.mana))

    def sufferDamage(self, damage):
        '''
        Funcao responsavel subtrair o dano sofrido no HP
        damage : Type (INT)
        return: VOID
        '''

        self.hp -= damage

    def setWAVSlang(self, nomeArquivoWAV):
        '''
        Atualizar o arquivo inicializado como ('') vazio
        :param nomeArquivoWAV:
        :return: void
        '''
        self.arqWAV[0] = nomeArquivoWAV

    def PlayWAVSlang(self):
        winsound.PlaySound(self.arqWAV[0], winsound.SND_NOSTOP)

    def setWAVShow(self, nomeArquivoWAV):
        '''
        Atualizar o arquivo inicializado como ('') vazio
        :param nomeArquivoWAV:
        :return: void
        '''
        self.arqWAV[1] = nomeArquivoWAV

    def PlayWAVShow(self):
        winsound.PlaySound(self.arqWAV[1], winsound.SND_NOSTOP)

    def userMana(self, mana):
        '''
        Funcao responsavel subtrair a MANA utlizada para realizar o ataque
        :param Type (INT)
        :return: VOID
        '''

        self.mana -= mana

    def knock(self, playerAdversario, attack):
        '''
        Realizar o Ataque. Calcular latência.
        :param playerAdversario: Player
        :param attack: Attack
        :return: void
        '''
        # o numero randomico para a latencia
        randomLatenciaAtaque = randint(0, 9)
        # ESTRUTURA DA LATENCIA
        '''
                A latencia e a possibilidade de erro do ataque. Entao, e jagado um random e comparado esse o valor do random com a latencia do Player
                Se a latencia do individuo for 5, significa que ele tem uma margem de erro [0,5[. 
                Quando comparado com o valor randomico, se o valor estiver fora dessa margem o ataque foi efetivo
                QUANTO MENOR A LATENCIA, MAIS MAIOR E A POSSIBILIDADE DE ATQUE EFETIVO
                #ESTRUTURA DA LATENCIA
                A latencia e a possibilidade de erro do ataque. Entao, e jagado um random e comparado esse o valor do random com a latencia do Player
                Se a latencia do individuo for 5, significa que ele tem uma margem de erro [0,5[. 
                Quando comparado com o valor randomico, se o valor estiver fora dessa margem o ataque foi efetivo
                QUANTO MENOR A LATENCIA, MAIS MAIOR E A POSSIBILIDADE DE ATQUE EFETIVO
        '''
        if (attack.latencia <= randomLatenciaAtaque):
            # ATAQUE EFETIVO
            System.print('''SEU ATAQUE FOI EFETIVO
            -------------RANDOM LATENCIA: {}'''.format(str(randomLatenciaAtaque)), "GREEN")
            randomLatenciaDefesa = randint(0, 9)

            if (playerAdversario.shield.latencia <= randomLatenciaDefesa):
                # DEFESA EFETIVA
                danos = System.calculeteDamageShield(playerAdversario, attack)
                danoReal = danos[0] + danos[1]
                playerAdversario.sufferDamage(danoReal)
                self.userMana(attack.mana)
                manaRestore = self.restoreMana(danoReal)
                System.printKnock(danoReal, manaRestore, attack, self, playerAdversario)

            else:
                # DEFESA NAO EFETIVA
                System.print("DANO CRITICO", 'NEGRITO')
                danos = System.calculeteDamage(attack)
                danoReal = danos[0]+danos[1]
                playerAdversario.sufferDamage(danoReal)
                self.userMana(attack.mana)
                manaRestore = self.restoreMana(danoReal)
                System.printKnock(danoReal, manaRestore, attack, self, playerAdversario)
        else:
            # ATAQUE NAO EFETIVO
            System.print('''SEU ATAQUE FALHOU
            -------------RANDOM LATENCIA: {}'''.format(str(randomLatenciaAtaque)), "RED")

    def restoreMana(self, dano):
        """
        :param dano: int
        :return: int
        """
        # quanto maior e o dano menos se recupera a mana
        if dano >= 400:
            mana = int(1000 * (100 / dano))
            self.mana += mana
            return mana
        else:
            self.mana += 300
            return 300

    @staticmethod
    def printAttacks(player):
        '''
        Metodo estático. Imprime os ataques.
        :param player: Player
        :return: void
        '''
        attacksUser = player.sword.getAttack()
        for attackIndice in range(4):
            if attackIndice == 3:
                print(str(attackIndice) + " - Manter modo defensivo")
                break
            print(str(attackIndice) + " - " + str(attacksUser[attackIndice]) + "\n")
    def addItem(self, item):
        self.inventory.append(item)
        self.money -= item.valor


class InteligencePlayer:
    def __init__(self, player, adv, baseDeMana, importanciaDANO=4,importanciaMANA=1, importanciaLATENCIA=3,
                 activeStrategyMana = False, activeStrategyLatAttk= False, activeStrategyDMC=False,
                 activeStrategyLatDeff=False, activeStrategyLife=False, activeStrategyDF=False):
        self.player = player
        self.adv = adv
        self.importanciaDANO = importanciaDANO
        self.importanciaMANA = importanciaMANA
        self.importanciaLATENCIA = importanciaLATENCIA
        self.baseDeMana = baseDeMana

        self.rankAttack = list()

        # Estratégias de Mana
        self.strategyItens = {
            # Nome da Estratégia
            "Mana" : {
                # Estratégia Ativa
                "active" : activeStrategyMana,
                # Condição de Ativação Durante a Partida
                "condition" : lambda : self.player.mana < self.baseDeMana,
                # Atributos para o Rankamento
                "attribute" : {
                    "alterMana": {
                        "priority":1,
                        "reverse" :  False
                    }
                }
            },
            "Latência Attk": {
                "active": activeStrategyLatAttk,
                "condition": lambda : self.player.sword.getAttack()[self.resolverAttack(self.adv)].latencia > 5,
                "attribute": {
                    "alterLatenciaAttk": {
                        "priority": 1,
                        "reverse": False
                    }
                }
            },
            "Dano Mágico Críticos": {
                "active": activeStrategyDMC,
                "condition": lambda : True,
                "attribute": {
                    "alterDanoMagico": {
                        "priority": 4,
                        "reverse": False
                    },
                    "alterLatenciaDeff": {
                        "priority": 2,
                        "reverse": True
                    }
                }
            },
            "Latência Deff": {
                "active": activeStrategyLatDeff,
                "condition": lambda: self.adv.shield.latencia < 4,
                "attribute": {
                    "alterLatenciaAttk": {
                        "priority": 1,
                        "reverse": False
                    },
                    "alterLatenciaDeff": {
                        "priority": 5,
                        "reverse": True
                    }
                }
            },
            "Vida": {
                "active": activeStrategyLife,
                "condition": lambda: self.player.hp < 1000,
                "attribute": {
                    "alterLife": {
                        "priority": 1,
                        "reverse": False
                    }
                }
            },
            "Dano Físico": {
                "active": activeStrategyDF,
                "condition": lambda: True,
                "attribute": {
                    "alterDanoFisico": {
                        "priority": 1,
                        "reverse": False
                    }
                }
            }
        }

    def buscaIndexItem(self, item, matriz):
        for l in range(len(matriz)):
            if matriz[l][0].name == item.name:
                return l
        print("ERRO NÃO ENCONTRADO O ITEM")
        sys.exit()

    def gerarRankItensAttr(self, attributeKey, attributeDic, listaPoint=[]):
        allItens = System.allItens()
        listaPontosGeralItens = [[item, 0] for item in allItens] if len(listaPoint) == 0 else listaPoint
        auxListaAttributeItens = []
        #GERAR MATRIZ COM O ATRIBUTO
        for item in allItens:
            auxListaAttributeItens.append([item, item.__getattribute__(attributeKey)])

        rank = sorted(auxListaAttributeItens, key=itemgetter(1), reverse=attributeDic["reverse"])

        cont = 0
        for listItemRank in rank:
            index = self.buscaIndexItem(listItemRank[0],listaPontosGeralItens)
            listaPontosGeralItens[index][1] += cont
            cont  += attributeDic["priority"]

        return listaPontosGeralItens

    def resolverListCompraItens(self):
        listaPontosGeralItens = []
        for strategy in self.strategyItens:
            # Verica se a estratégia está ativada e a sua condição está presente
            if self.strategyItens[strategy]["active"] and self.strategyItens[strategy]["condition"]():
                print(strategy)
                # Add pontuação para todos os atributos dessa estratégia
                for attr in self.strategyItens[strategy]["attribute"]:
                    listaPontosGeralItens = self.gerarRankItensAttr(attr, self.strategyItens[strategy]["attribute"][attr],
                                                                listaPontosGeralItens)
        listaPontosGeralItens = sorted(listaPontosGeralItens, key=itemgetter(1), reverse=True)

        return listaPontosGeralItens

    def buyItems(self):
        for listItem in self.resolverListCompraItens():
            if listItem[0].valor <= self.player.money:
                self.player.addItem(listItem[0])

    def gerarRanckAttack(self, playerAdv):
        ListAttack = self.player.sword.getAttack()
        listaPontosAttack = []
        for indexAttack in range(len(ListAttack)):
            danos = System.calculeteDamageShield(playerAdv, ListAttack[indexAttack])
            danoReal = danos[0] + danos[1]
            attk = ListAttack[indexAttack]
            listaPontosAttack.append([attk,danoReal,attk.mana,attk.latencia, indexAttack, 0])

        rankDano = self.ADDpontos(sorted(listaPontosAttack, key=itemgetter(1)),self.importanciaDANO)
        rankMana = self.ADDpontos(sorted(rankDano, key=itemgetter(2),  reverse=True),self.importanciaMANA)
        rankLantancia = self.ADDpontos(sorted(rankMana, key=itemgetter(3),  reverse=True),self.importanciaLATENCIA)

        self.rankAttack = sorted(rankLantancia, key=itemgetter(5))

    def ADDpontos(self, matriz, pontos, index=5):
        cont = 0
        for line in matriz:
            line[index] += cont
            cont += pontos
        return matriz

    def resolverAttack(self, PlayerAdv):
        '''
        Funcao responsavel por retorna o index do ataque mais recomendado
        :param PlayerAdv: Player
        :return: int [0:3]
        '''
        if self.player.mana == 0:
            return 3
        if self.player.mana <= self.baseDeMana:
            for linhaMatrizAttack in self.rankAttack:
                if self.player.mana > linhaMatrizAttack[0].mana:
                    return linhaMatrizAttack[4]
            return 3
        else:
            for linhaMatrizAttack in self.rankAttack[::-1]:
                if self.player.mana > linhaMatrizAttack[0].mana:
                    return linhaMatrizAttack[4]
            return 3


class Sword:
    def __init__(self, name, attackI, attackII, attackIII,
                 imageID="DirPNG/matrix-wallpaper.png"):
        self.name = name
        self.imageID = imageID
        self.attackI = attackI
        self.attackII = attackII
        self.attackIII = attackIII

    def __str__(self):
        ataques = self.getAttack()
        somaDanoMagico = 0
        somaDanoFisico = 0
        somaMana = 0
        samaLatencia = 0

        for attack in ataques:
            somaDanoMagico += attack.danoMagico
            somaDanoFisico += attack.danoFisico
            samaLatencia += attack.latencia
            somaMana += attack.mana
        mediaDanoMagico = somaDanoMagico / 3
        mediaDanoFisico = somaDanoFisico / 3
        mediaLatencia = samaLatencia / 3
        mediaMana = somaMana/3

        return '''Nome: {}
Média DM : {:.2f}
Média DF : {:.2f}
Média Latência : {:.2f}
Média Mana: {:.2f}'''.format(self.name,mediaDanoMagico, mediaDanoFisico,mediaLatencia, mediaMana)

    def getDados(self):
        ataques = self.getAttack()
        somaDanoMagico = 0
        somaDanoFisico = 0
        somaMana = 0
        samaLatencia = 0

        for attack in ataques:
            somaDanoMagico += attack.danoMagico
            somaDanoFisico += attack.danoFisico
            samaLatencia += attack.latencia
            somaMana += attack.mana
        mediaDanoMagico = somaDanoMagico / 3
        mediaDanoFisico = somaDanoFisico / 3
        mediaLatencia = samaLatencia / 3
        mediaMana = somaMana / 3

        return '''Nome: {}
Média DM : {:.2f}
Média DF : {:.2f}
Média Mana: {:.2f}
Média Latência : {:.2f}'''.format(self.name,mediaDanoMagico, mediaDanoFisico, mediaMana,mediaLatencia)

    def getAttack(self):
        '''
        Funcao responsavel por retornar o ataque requerido pelo PLAYER
        :return: List<Attack>
        '''
        return [self.attackI, self.attackII, self.attackIII]


class Attack:
    def __init__(self, name, mana, latencia, danoMagico, danoFisico, imageBT = "DirPNG/matrix-wallpaper.png"):
        self.name = name
        self.mana = mana
        self.latencia = latencia
        self.danoMagico = danoMagico
        self.danoFisico = danoFisico
        self.imageBt = imageBT

    def __str__(self):
        # coverter para string
        return ("Nome: " + str(self.name) + "\nDano Magico: " + str(self.danoMagico) + "\nDano Fisico: " + str(
            self.danoFisico) + "\nMana: " + str(self.mana) + "\nLantenci: " + str(self.latencia))
    def getDados(self):
        return ("Nome: " + str(self.name) + "\nDano Magico: " + str(self.danoMagico) + "\nDano Fisico: " + str(
            self.danoFisico) + "\nMana: " + str(self.mana) + "\nLantenci: " + str(self.latencia))

class Shield:
    def __init__(self, name, latencia, defesaMagica, defesaFisica,
                 imageID="DirPNG/matrix-wallpaper.png"):
        self.name = name
        self.imageID = imageID
        self.latencia = latencia
        self.defesaMagica = defesaMagica
        self.defesaFisica = defesaFisica

    def __str__(self):
        return (
                "Nome: " + self.name + "\nLatencia: " + self.latencia + "\nDefesa Magica: " + self.defesaMagica + "\nDefesa Fisica: " + self.defesaFisica)
    def getDados(self):
        return '''Nome: {}
Defesa Magica: {}
Defesa Fisica: {}
Latencia: {}
        '''.format(self.name,self.defesaMagica,self.defesaFisica,self.latencia)

class Item:
    def __init__(self, name, valor, quatidade, desc="", image="DirPNG/matrix-wallpaper.png",
                 alterLife = 0, alterMana = 0,alterDefesaMagica = 0, alterDefesaFisica = 0, alterLatenciaAttk = 0,
                 alterLatenciaDeff = 0, alterDanoMagico = 0, alterDanoFisico = 0):
        self.name = name
        self.valor = valor
        self.quatidade = quatidade
        self.desc = desc
        self.image = image
        self.alterLife = alterLife
        self.alterMana =  alterMana
        self.alterDefesaMagica = alterDefesaMagica
        self.alterDefesaFisica = alterDefesaFisica
        self.alterLatenciaAttk = alterLatenciaAttk
        self.alterLatenciaDeff = alterLatenciaDeff
        self.alterDanoMagico = alterDanoMagico
        self.alterDanoFisico = alterDanoFisico
    def usarItem(self):
        self.quatidade -= 1
    def ended(self):
        return self.quatidade > 0
    def aplicarItem(self, player, attack, latATTK, latDEFF):
        self.usarItem()
        #ALTERAR O PLAYER
        player.hp += self.alterLife
        player.mana += self.alterMana
        # ALTERAR O PLAYER.SHIELD
        player.shield.defesaFisica += self.alterDefesaFisica
        player.shield.defesaMagica += self.alterDefesaMagica
        #LATÊNCIA
        latATTK += self.alterLatenciaAttk
        latDEFF += self.alterLatenciaDeff
        #ATTACK
        attack.danoMagico += self.alterDanoMagico
        attack.danoFisico += self.alterDanoFisico
        return [latATTK,latDEFF, self.alterMana]
    def getDados(self):
        info = {"Life":self.alterLife ,
                "Mana":self.alterMana,
                "Defesa Magica":self.alterDefesaMagica,
                "Defesa Física":self.alterDefesaFisica,
                "LatenciaAttk":self.alterLatenciaAttk,
                "LatenciaDeff":self.alterLatenciaDeff,
                "Dano Magico":self.alterDanoMagico,
                "Dano Físico":self.alterDanoFisico}
        dados = f'''{self.name.upper()}\n\n'''
        for infoDic in info:
            if info[infoDic] > 0:
                dados += f"{infoDic} : + {info[infoDic]}\n"
            elif info[infoDic] < 0:
                dados += f"{infoDic} : - {abs(info[infoDic])}\n"
        dados += f'''\n{self.valor}U$\n\n{self.desc}'''
        return dados