from random import randint, shuffle
from operator import itemgetter
import winsound
import sys


class System:
    @staticmethod
    def choosePlayer(indexPlayer=None,nameChamp=None):
        if indexPlayer != None or nameChamp!=None:
            if nameChamp == 'Ichigo Kurosaki' or indexPlayer==0 :
                at1 = Attack(name="Getsuga Tenshou", mana=400, latencia=5, danoFisico=300, danoMagico=2000,
                             imageBT="DirPNG/atk3.png")
                at2 = Attack(name="Piercer of Heaven", mana=200, latencia=2, danoFisico=100, danoMagico=1000,
                             imageBT="DirPNG/atk3.png")
                at3 = Attack(name="Getsuga Jūjishō", mana=350, latencia=2, danoFisico=250, danoMagico=1500,
                             imageBT="DirPNG/atk3.png")

                sword = Sword("Zanpakutō", at1, at2, at3,
                              imageID="DirPNG/Sword/zampakuto.png")

                shield = Shield(name="Shielding Berserker", latencia=2, defesaFisica=400, defesaMagica=1500,
                                imageID="DirPNG/Shield/berserker.png")

                player = Player(name="Ichigo Kurosaki", hp=10000, mana=600, sword=sword, shield=shield, personality=[5,4,1],
                                baseMana=450,
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
            elif nameChamp == 'Killer Bee' or indexPlayer==1:
                at1 = Attack(name="Crumbling the skin", mana=800, latencia=6, danoFisico=3000, danoMagico=600,
                             imageBT="DirPNG/atk1.png")
                at2 = Attack(name="Life Theft", mana=250, latencia=3, danoFisico=400, danoMagico=1500,
                             imageBT="DirPNG/atk3.png")
                at3 = Attack(name="Samehada and the 7 swords", mana=500, latencia=3, danoFisico=1000,
                             danoMagico=1500,
                             imageBT="DirPNG/atk2.png")

                sword = Sword("Samehada", at1, at2, at3,
                              imageID="DirPNG/Sword/samehada.png")

                shield = Shield(name="Shielding of Gemini", latencia=4, defesaFisica=500, defesaMagica=1200,
                                imageID="DirPNG/Shield/gemeos.png")

                player = Player(name="Killer Bee", hp=12500, mana=1000, sword=sword, shield=shield, personality=[6,3,4],
                                baseMana=850,
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
            elif nameChamp == 'Xena' or indexPlayer==2:
                at1 = Attack(name="Full Counter", mana=700, latencia=3, danoFisico=3000, danoMagico=500,
                             imageBT="DirPNG/atk1.png")
                at2 = Attack(name="Counter Vanish", mana=200, latencia=1, danoFisico=2000, danoMagico=0,
                             imageBT="DirPNG/atk1.png")
                at3 = Attack(name="Hellblaze", mana=400, latencia=4, danoFisico=1500, danoMagico=300,
                             imageBT="DirPNG/atk1.png")

                sword = Sword("Excalibur", at1, at2, at3,
                              imageID="DirPNG/Sword/excalibur.png")

                shield = Shield(name="Shielding Knight", latencia=3, defesaFisica=1600, defesaMagica=300,
                                imageID="DirPNG/Shield/knight.png")

                player = Player(name="Xena", hp=9900, mana=1500, sword=sword, shield=shield, personality=[6,3,3],
                                baseMana=750,
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
            elif nameChamp == 'Roronoa Zoro' or indexPlayer==3:
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
                                baseMana=250,
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
            elif nameChamp == 'Gohan' or indexPlayer==4:
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
                                baseMana=1000,
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
        else:
            return None


    @staticmethod
    def allItens():
        return [
            Item("Dragon claws",420,5,alterDanoMagico=200,alterLatenciaAttk=8, image="DirPNG/Itens/Dragonclaws.png"),

            Item("3 warriors of David",800,3,alterLatenciaDeff=-5,alterDanoFisico=700, alterDanoMagico=300,
                 image="DirPNG/Itens/3warriorsofDavid.png"),

            Item("Adam's ring",270,5,alterLatenciaAttk=7,alterLatenciaDeff=4, alterLife=150,
                 image="DirPNG/Itens/Adamsring.png"),

            Item("living shield", 250, 1,alterLife=2500, alterDefesaMagica=550,alterLatenciaAttk=-1,
            image="DirPNG/Itens/livingshield.png"),

            Item("helmet of Ulysses", 350, 1, alterDefesaFisica=1000, image="DirPNG/Itens/helmetofUlysses.png"),

            Item("Loki's dagger", 350, 1, alterLife=3000, alterMana=1000, image="DirPNG/Itens/Lokisdagger.png"),

            Item("breastplate", 600, 1, alterLife=5000,alterDefesaMagica=500, alterDefesaFisica=500,
                 image="DirPNG/Itens/breastplate.png"),

            Item("hermes dagger", 150, 1, alterLatenciaDeff=-5, image="DirPNG/Itens/hermesdagger.png"),

            Item("apollo dagger", 300, 3, alterLatenciaAttk=7, alterDefesaFisica=-50, alterLatenciaDeff=2,
                 alterDanoFisico=200, image="DirPNG/Itens/apollodagger.png"),

            Item("Spiked Shoulder Armor", 450, 1, alterDanoFisico=500,alterLatenciaAttk=6,alterMana=200,
                 alterDefesaFisica=400,
                 image="DirPNG/Itens/spikedshoulderarmor.png"),

            Item("trident of jaime", 650, 1, alterDanoMagico=1200, alterLatenciaDeff=-7, alterMana=-700,
                 image="DirPNG/Itens/tridentofjaime.png"),

            Item("fragmented sword", 650, 1, alterDanoMagico=1600,alterDefesaFisica=-500,
                 image="DirPNG/Itens/fragmentedsword.png"),

            Item("Bone knife", 150, 1, alterLatenciaAttk=9,
                 image="DirPNG/Itens/Boneknife.png"),

            Item("flail", 450, 2, alterLatenciaDeff=-2,alterDanoFisico=600,
                 image="DirPNG/Itens/flail.png"),

            Item("Sharp axe", 550, 1, alterDanoFisico=800, alterLatenciaAttk=4,
                 image="DirPNG/Itens/Sharpaxe.png"),

            Item("viking helmet", 450, 1, alterDefesaFisica=700, alterLatenciaAttk=5,
                 image="DirPNG/Itens/vikinghelmet.png"),

            Item("Black Knight Helm", 550, 1, alterDefesaFisica=1500,
                 image="DirPNG/Itens/BlackKnightHelm.png"),

            Item("helmet of the wise", 780, 1, alterDefesaFisica=300,alterDefesaMagica=700,alterDanoMagico=1000,
                 image="DirPNG/Itens/helmetofthewise.png"),

            Item("Brutal helm", 360, 1, alterDefesaFisica=700, alterLatenciaAttk=6, alterLatenciaDeff=-6,
                 image="DirPNG/Itens/Brutalhelm.png"),

            Item("Heavy helm", 400, 1, alterDefesaFisica=1200, alterDanoFisico=300,
                 image="DirPNG/Itens/Heavyhelm.png"),

            Item("Crossed axes", 350, 1, alterDanoFisico=800, alterLatenciaDeff=-7
                ,image="DirPNG/Itens/Crossedaxes.png")

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
    def __init__(self, name, hp, mana, sword, shield, personality=[4,1,3], baseMana=500,
                 activeStrategyMana = False,
                 activeStrategyLatAttk=False,
                 activeStrategyDMC=False,
                 activeStrategyLatDeff=False,
                 activeStrategyLife=False,
                 activeStrategyDF=False,
                 activeStrategyDefM=False,
                 imageShow = "DirPNG/matrix-wallpaper.png",imageID="DirPNG/matrix-wallpaper.png",
                 imageShowChoose = "DirPNG/matrix-wallpaper.png"):
        self.name = name
        self.hp = hp
        self.sword = sword
        self.shield = shield
        self.mana = mana
        self.inventory = []
        self.baseMana = baseMana

        self.imageShow = imageShow
        self.imageID = imageID
        self.imageShowChoose = imageShowChoose

        self.arqWAV = ["", ""]

        self.money = 600
        self.personality = {"importanciaDANO": personality[0],
                            "importanciaMANA": personality[1],
                            "importanciaLATENCIA": personality[2],
                            "activeStrategyMana" : activeStrategyMana,
                            "activeStrategyLatAttk": activeStrategyLatAttk,
                            "activeStrategyDMC" : activeStrategyDMC,
                            "activeStrategyLatDeff": activeStrategyLatDeff,
                            "activeStrategyLife":activeStrategyLife,
                            "activeStrategyDF":activeStrategyDF,
                            "activeStrategyDefM": activeStrategyDefM
                            }

    def setPersonalityItens(self, dic):
        '''
        Ele set os atributos do player em relação a compra dos Itens

        :param dic:
        :return: void
        '''
        for strategy in dic:
            self.personality[strategy] = dic[strategy]
    def setPersonalityAttk(self, listP):
        '''
        Ele set os atributos do player em relação a escolha de ataques

        :param listP:
        :return:
        '''
        listP = list(listP)
        self.personality["importanciaDANO"] = int(listP.__getitem__(0))
        self.personality["importanciaMANA"] = int(listP.__getitem__(1))
        self.personality["importanciaLATENCIA"] =  int(listP.__getitem__(2))


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

    def userItens(self, randomLatenciaAtaque, randomLatenciaDefesa, attack):
        newLatATTK, newLatDEF, manaItens, textLbDica = randomLatenciaAtaque, randomLatenciaDefesa, 0, "\n"
        for item in self.inventory:
            if item.ended():
                info = item.aplicarItem(self, attack, newLatATTK, newLatDEF)
                newLatATTK, newLatDEF = info[0], info[1]
                manaItens += info[2]
                textLbDica += f"\n+ {item.name.upper()}"
        return [newLatATTK, newLatDEF, manaItens, textLbDica]

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

    def addItem(self, item):
        self.inventory.append(item)
        self.money -= item.valor


class InteligencePlayer:
    def __init__(self, player, adv, baseDeMana=500, importanciaDANO=4,importanciaMANA=1, importanciaLATENCIA=3,
                 activeStrategyMana = False, activeStrategyLatAttk= False, activeStrategyDMC=False,
                 activeStrategyLatDeff=False, activeStrategyLife=False, activeStrategyDF=False,
                 activeStrategyDefM=False):
        self.player = player
        self.adv = adv
        self.importanciaDANO = importanciaDANO
        self.importanciaMANA = importanciaMANA
        self.importanciaLATENCIA = importanciaLATENCIA
        self.baseDeMana = baseDeMana

        self.rankAttack = list()

        #ATRIBUTOS DE ATIVAÇÃO
        self.activeStrategyMana = activeStrategyMana
        self.activeStrategyLatAttk = activeStrategyLatAttk
        self.activeStrategyDMC = activeStrategyDMC
        self.activeStrategyLatDeff = activeStrategyLatDeff
        self.activeStrategyLife = activeStrategyLife
        self.activeStrategyDF = activeStrategyDF
        self.activeStrategyDefM = activeStrategyDefM

        # Estratégias
        self.strategyItens = {
            # Nome da Estratégia e atributo de ativação
            "activeStrategyMana" : {
                "name": "Strategy MANA",
                # Estratégia Ativa
                "active" : lambda : self.activeStrategyMana,
                # Condição de Ativação Durante a Partida
                "condition" : lambda : self.player.mana < self.baseDeMana,
                # Atributos para o Rankamento
                "attribute" : {
                    "alterMana": {
                        "priority":10,
                        "reverse" :  False
                    }
                }
            },
            "activeStrategyLatAttk": {
                "name": "Attk Frenético",
                "active": lambda : self.activeStrategyLatAttk,
                "condition": lambda : self.player.sword.getAttack()[self.resolverAttack(self.adv)].latencia > 3,
                "attribute": {
                    "alterLatenciaAttk": {
                        "priority": 1,
                        "reverse": False
                    }
                }
            },
            "activeStrategyDMC": {
                "name": "ATTK DM",
                "active": lambda : self.activeStrategyDMC,
                "condition": lambda : True,
                "attribute": {
                    "alterDanoMagico": {
                        "priority": 3,
                        "reverse": False
                    }
                }
            },
            "activeStrategyLatDeff": {
                "name": "ATTK Críticos",
                "active": lambda : self.activeStrategyLatDeff,
                #Só a necessidade de comprar itens se a defesa for eficiente
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
            "activeStrategyLife": {
                "name": "Strategy LIFE",
                "active": lambda : self.activeStrategyLife,
                "condition": lambda: self.player.hp < 5000,
                "attribute": {
                    "alterLife": {
                        "priority": 5,
                        "reverse": False
                    }
                }
            },
            "activeStrategyDF": {
                "name": "ATTK DF",
                "active": lambda : self.activeStrategyDF,
                "condition": lambda: True,
                "attribute": {
                    "alterDanoFisico": {
                        "priority": 1,
                        "reverse": False
                    }
                }
            },
            "activeStrategyDefM": {
                "name": "Defesa Mágica",
                "active": lambda : self.activeStrategyDefM,
                "condition": lambda: self.adv.sword.getMAXdanoMagico() >= self.player.shield.defesaMagica,
                "attribute": {
                    "alterDefesaMagica": {
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
            if self.strategyItens[strategy]["active"]() and self.strategyItens[strategy]["condition"]():
                print(strategy)
                # Add pontuação para todos os atributos dessa estratégia
                for attr in self.strategyItens[strategy]["attribute"]:
                    listaPontosGeralItens = self.gerarRankItensAttr(attr, self.strategyItens[strategy]["attribute"][attr],
                                                                listaPontosGeralItens)
        listaPontosGeralItens = sorted(listaPontosGeralItens, key=itemgetter(1), reverse=True)

        return listaPontosGeralItens

    def buyItems(self):
        contTop = 0
        listItensBuy = self.resolverListCompraItens()
        a = [[item[0].name, item[1]] for item in listItensBuy] if len(listItensBuy) > 0 else None
        print(a)
        for listItem in listItensBuy:
            if listItem[0].valor <= self.player.money and contTop < 3:
                self.player.addItem(listItem[0])
            contTop+=1

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

    def getMAXdanoFisico(self):
        return max([attack.danoFisico for attack in self.getAttack()])
    def getMAXdanoMagico(self):
        return max([ attack.danoMagico for attack in self.getAttack()])

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
        '''
        Altera a quantidade do item.

        -- Função "private"

        :return: Void
        '''
        self.quatidade -= 1
    def ended(self):
        '''
        Verifica se o Item terminou

        :return: Boolean
        '''
        return self.quatidade > 0
    def aplicarItem(self, player, attack, latATTK, latDEFF):
        '''
        Ela altera algumas vaiáveis do jogo.

        :param player:
        :param attack:
        :param latATTK:
        :param latDEFF:
        :return: list [latATTK, latDEFF, self.alterMana]
        '''
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
        return [latATTK, latDEFF, self.alterMana]
    def getDados(self):
        '''
        Get dos dados do Item de forma formatada.

        :return: String
        '''
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