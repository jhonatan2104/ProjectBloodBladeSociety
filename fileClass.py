from random import randint, shuffle
from operator import itemgetter
import winsound

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
            at1 = Attack(name="Getsuga Tenshou", mana=400, latencia=6, danoFisico=1000, danoMagico=6000,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
            at2 = Attack(name="Piercer of Heaven", mana=200, latencia=3, danoFisico=600, danoMagico=2000,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
            at3 = Attack(name="Getsuga Jūjishō", mana=350, latencia=3, danoFisico=2500, danoMagico=1500,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")

            sword = Sword("Zanpakutō", at1, at2, at3,
                          imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Sword/zampakuto.png")

            shield = Shield(name="Armor Berserker", latencia=2, defesaFisica=1000, defesaMagica=3000,
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Shield/berserker.png")

            player = Player(name="Ichigo Kurosaki", hp=10000, mana=10, sword=sword, shield=shield,
                            imageShow="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/ichico.png",
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/nIchigo.png")

            player.setWAVShow("DirWAV/ICHIGOPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Killer Bee':
            at1 = Attack(name="Crumbling the skin", mana=200, latencia=3, danoFisico=3000, danoMagico=600,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
            at2 = Attack(name="Life Theft", mana=10, latencia=5, danoFisico=1000, danoMagico=5500,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
            at3 = Attack(name="Samehada and the seven lightning swords", mana=500, latencia=3, danoFisico=3500,
                         danoMagico=4500,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")

            sword = Sword("Samehada", at1, at2, at3,
                          imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Sword/samehada.png")

            shield = Shield(name="Armor of Gemini", latencia=4, defesaFisica=2000, defesaMagica=1000,
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Shield/gemeos.png")

            player = Player(name="Killer Bee", hp=9900, mana=1500, sword=sword, shield=shield,
                            imageShow="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/bee.png",
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/nBee.png")

            player.setWAVShow("DirWAV/KILLERBEEPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Xena':
            at1 = Attack(name="Full Counter", mana=200, latencia=3, danoFisico=3000, danoMagico=500)
            at2 = Attack(name="Counter Vanish", mana=100, latencia=1, danoFisico=2500, danoMagico=100)
            at3 = Attack(name="Hellblaze", mana=400, latencia=5, danoFisico=4000, danoMagico=3000)

            sword = Sword("Excalibur", at1, at2, at3,
                          imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Sword/excalibur.png")

            shield = Shield(name="Armor Knight", latencia=3, defesaFisica=1000, defesaMagica=1000,
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Shield/knight.png")

            player = Player(name="Xena", hp=7000, mana=1000, sword=sword, shield=shield,
                            imageShow="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/xena.png",
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/nXena.png")

            player.setWAVShow("DirWAV/XENAPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Roronoa Zoro':
            at1 = Attack(name="Shishi SonSon", mana=100, latencia=1, danoFisico=1500, danoMagico=0,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
            at2 = Attack(name="Sanjuroku Pound Ho", mana=200, latencia=4, danoFisico=3500, danoMagico=500,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
            at3 = Attack(name="Yakkodori", mana=500, latencia=3, danoFisico=3000, danoMagico=4000,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")

            sword = Sword("Sandai Kitetsu", at1, at2, at3,
                          imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Sword/sandaiKitetsu.png")

            shield = Shield(name="Black Armor", latencia=4, defesaFisica=1000, defesaMagica=1000,
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Shield/negra.png")

            player = Player(name="Roronoa Zoro", hp=7000, mana=1000, sword=sword, shield=shield,
                            imageShow="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/zoro.png",
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/nZoro.png")

            player.setWAVShow("DirWAV/ZOROPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Gohan':
            at1 = Attack(name="Fulminant Strike", mana=400, latencia=3, danoFisico=1000, danoMagico=3000,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
            at2 = Attack(name="Blade Combo", mana=300, latencia=1, danoFisico=1500, danoMagico=1500,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")
            at3 = Attack(name="Rage of the Blade", mana=600, latencia=7, danoFisico=6500, danoMagico=1000,
                         imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png")

            sword = Sword("Espada Z", at1, at2, at3,
                          imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Sword/espadaZ.png")

            shield = Shield(name="Metal Tech", latencia=3, defesaFisica=700, defesaMagica=500,
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Shield/metalTech.png")

            player = Player(name="Gohan", hp=9999, mana=2000, sword=sword, shield=shield,
                            imageShow="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/gohan.png",
                            imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/Personagens/nGohan.png")

            player.setWAVShow("DirWAV/GOHANPERSONAGEM.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player

    @staticmethod
    def allItens():
        return [
            Item("SANGUE DE DRAGÃO",100,15,alterMana=-100,alterDanoFisico=500),
            Item("LÁGRIMA DE PRINCESA",300,1,alterLatenciaDeff=-3,alterDanoMagico=1000),
            Item("ANEL DE ADÃO",200,15,alterDanoFisico=500,alterDanoMagico=600),
            Item("ESCUDO VIVO", 100, 15, alterDefesaFisica=300,alterDefesaMagica=-300),
            Item("LÁGRIMA DE PRINCESA", 300, 1, alterLatenciaDeff=-3, alterDanoMagico=1000),
            Item("ANEL DE ADÃO", 200, 15, alterDanoFisico=500, alterDanoMagico=600),
            Item("SANGUE DE DRAGÃO", 100, 15, alterMana=-100, alterDanoFisico=500),
            Item("LÁGRIMA DE PRINCESA", 300, 1, alterLatenciaDeff=-3, alterDanoMagico=1000),
            Item("ANEL DE ADÃO", 200, 15, alterDanoFisico=500, alterDanoMagico=600),
        ]

    @staticmethod
    def filterItens():
        lista = System.allItens()
        shuffle(lista)
        return lista[0:6]

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
    def __init__(self, name, hp, mana, sword, shield,
                 imageShow = "C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png",
                 imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png"):
        self.name = name
        self.hp = hp
        self.sword = sword
        self.shield = shield
        self.mana = mana
        self.imageShow = imageShow
        self.imageID = imageID
        self.arqWAV = ["", ""]
        self.inventory = []

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
        print("1")


class InteligencePlayer:
    def __init__(self, player, baseDeMana):
        self.player = player
        self.importanciaDANO = 4
        self.importanciaMANA = 1
        self.importanciaLATENCIA = 3
        self.rank = list()
        self.baseDeMana = baseDeMana

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

        self.rank = sorted(rankLantancia, key=itemgetter(5))
    def ADDpontos(self, matriz, pontos):
        cont = 0
        for line in matriz:
            line[5] += cont
            cont += pontos
        return matriz

    def rankAttack(self, PlayerAdv):
        '''
        Funcao responsavel por rankear os ataques do player
        :param PlayerAdv: Player
        :return: Matriz[3][3]
        '''

        ListAttack = self.player.sword.getAttack()
        ListRank = []
        for indexAttack in range(len(ListAttack)):
            danos = System.calculeteDamageShield(PlayerAdv, ListAttack[indexAttack])
            danoReal = danos[0]+danos[1]
            ListRank.append([ListAttack[indexAttack], danoReal, indexAttack])
        return sorted(ListRank, key=itemgetter(1))

    def resolverAttack(self, PlayerAdv):
        '''
        Funcao responsavel por retorna o index do ataque mais recomendado
        :param PlayerAdv: Player
        :return: int [0:3]
        '''
        if self.player.mana == 0:
            return 3
        if self.player.mana <= self.baseDeMana:
            for linhaMatrizAttack in self.rank:
                if self.player.mana > linhaMatrizAttack[0].mana:
                    return linhaMatrizAttack[4]
            return 3
        else:
            for linhaMatrizAttack in self.rank[::-1]:
                if self.player.mana > linhaMatrizAttack[0].mana:
                    return linhaMatrizAttack[4]
            return 3


class Sword:
    def __init__(self, name, attackI, attackII, attackIII,
                 imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png"):
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
    def __init__(self, name, mana, latencia, danoMagico, danoFisico,
                 imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png"):
        self.name = name
        self.mana = mana
        self.latencia = latencia
        self.danoMagico = danoMagico
        self.danoFisico = danoFisico
        self.imageID = "C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png"

    def __str__(self):
        # coverter para string
        return ("Nome: " + str(self.name) + "\nDano Magico: " + str(self.danoMagico) + "\nDano Fisico: " + str(
            self.danoFisico) + "\nMana: " + str(self.mana) + "\nLantenci: " + str(self.latencia))
    def getDados(self):
        return ("Nome: " + str(self.name) + "\nDano Magico: " + str(self.danoMagico) + "\nDano Fisico: " + str(
            self.danoFisico) + "\nMana: " + str(self.mana) + "\nLantenci: " + str(self.latencia))

class Shield:
    def __init__(self, name, latencia, defesaMagica, defesaFisica,
                 imageID="C:/Users/User/PycharmProjects/ProjectBloodBladeSociety/DirPNG/matrix-wallpaper.png"):
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
    def __init__(self, name, valor, quatidade, desc="",
                 alterLife = 0, alterMana = 0,alterDefesaMagica = 0, alterDefesaFisica = 0, alterLatenciaAttk = 0,
                 alterLatenciaDeff = 0, alterDanoMagico = 0, alterDanoFisico = 0):
        self.name = name
        self.valor = valor
        self.quatidade = quatidade
        self.desc = desc
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
        dados = f'''{self.name}\n\n'''
        for infoDic in info:
            if info[infoDic] > 0:
                dados += f"{infoDic} : + {info[infoDic]}\n"
            elif info[infoDic] < 0:
                dados += f"{infoDic} : - {abs(info[infoDic])}\n"
        dados += f'''\n{self.valor}U$\n\n\n{self.desc}'''
        return dados