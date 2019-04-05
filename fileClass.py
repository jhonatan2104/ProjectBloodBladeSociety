from random import randint
from operator import itemgetter
import winsound


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
    def choosePlayer(indexPlayer):
        nameChamp = System.listPlayer()[indexPlayer]
        if nameChamp == 'Ichigo Kurosaki':
            at1 = Attack(name="Getsuga Tenshou", mana=400, latencia=6, danoFisico=1000, danoMagico=6000)
            at2 = Attack(name="Piercer of Heaven", mana=200, latencia=3, danoFisico=600, danoMagico=2000)
            at3 = Attack(name="Getsuga Jūjishō", mana=350, latencia=3, danoFisico=2500, danoMagico=1500)

            sword = Sword("Zanpakutō", at1, at2, at3)

            shield = Shield(name="Armor Berserker", latencia=2, defesaFisica=1000, defesaMagica=3000)
            player = Player(name="Ichigo Kurosaki", hp=10000, mana=1000, sword=sword, shield=shield)

            player.setWAVShow("DirWAV/go.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Killer Bee':
            at1 = Attack(name="Crumbling the skin", mana=200, latencia=3, danoFisico=3000, danoMagico=600)
            at2 = Attack(name="Life Theft", mana=10, latencia=7, danoFisico=1000, danoMagico=5500)
            at3 = Attack(name="Samehada and the seven lightning swords", mana=500, latencia=5, danoFisico=3500, danoMagico=4500)

            sword = Sword("Samehada", at1, at2, at3)

            shield = Shield(name="Armor of Gemini", latencia=4, defesaFisica=2000, defesaMagica=1000)
            player = Player(name="Killer Bee", hp=10000, mana=1500, sword=sword, shield=shield)

            player.setWAVShow("DirWAV/go.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Xena':
            at1 = Attack(name="Full Counter", mana=200, latencia=3, danoFisico=3000, danoMagico=500)
            at2 = Attack(name="Counter Vanish", mana=100, latencia=1, danoFisico=2500, danoMagico=100)
            at3 = Attack(name="Hellblaze", mana=400, latencia=5, danoFisico=4000, danoMagico=3000)

            sword = Sword("Excalibur", at1, at2, at3)

            shield = Shield(name="Armor Knight",  latencia=3, defesaFisica=1000, defesaMagica=1000)

            player = Player(name="Xena", hp=7000, mana=1000, sword=sword, shield=shield)

            player.setWAVShow("DirWAV/go.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Roronoa Zoro':
            at1 = Attack(name="Shishi SonSon", mana=100, latencia=1, danoFisico=1500, danoMagico=0)
            at2 = Attack(name="Sanjuroku Pound Ho", mana=200, latencia=4, danoFisico=3500, danoMagico=500)
            at3 = Attack(name="Yakkodori", mana=500, latencia=3, danoFisico=3000, danoMagico=4000)

            sword = Sword("Sandai Kitetsu", at1, at2, at3)

            shield = Shield(name="Black Armor",  latencia=4, defesaFisica=1000, defesaMagica=1000)

            player = Player(name="Roronoa Zoro", hp=7000, mana=1000, sword=sword, shield=shield)

            player.setWAVShow("DirWAV/go.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player
        elif nameChamp == 'Gohan':
            at1 = Attack(name="Fulminant Strike", mana=400, latencia=3, danoFisico=1000, danoMagico=3000)
            at2 = Attack(name="Blade Combo", mana=300, latencia=1, danoFisico=1500, danoMagico=1500)
            at3 = Attack(name="Rage of the Blade", mana=600, latencia=7, danoFisico=6500, danoMagico=1000)

            sword = Sword("Espada Z", at1, at2, at3)

            shield = Shield(name="Metal Tech", latencia=3, defesaFisica=700, defesaMagica=500)

            player = Player(name="Gohan", hp=15000, mana=2000, sword=sword, shield=shield)

            player.setWAVShow("DirWAV/go.wav")
            player.setWAVSlang("DirWAV/go.wav")

            return player

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
            danoReal = danoRealFisico + danoRealMagico
            return danoReal
        elif danoRealMagico < 0 and danoRealFisico < 0:
            # significa que o ataque foi totalmente defendido
            return 0
        else:
            # significa que apenas uma das formas foi efetiva ao realizar o dano
            if danoRealMagico < 0:
                # Dano Fisico foi efetivo
                return danoRealFisico
            else:
                # Dano Magico foi efetivo
                return danoRealMagico

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

        danoReal = danoFisico + danoMagico

        return danoReal


class Player:
    def __init__(self, name, hp, mana, sword, shield):
        self.name = name
        self.hp = hp
        self.sword = sword
        self.shield = shield
        self.mana = mana
        self.arqWAV = ["",""]

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
    def setWAVSlang(self,nomeArquivoWAV):
        '''
        Atualizar o arquivo inicializado como ('') vazio
        :param nomeArquivoWAV:
        :return: void
        '''
        self.arqWAV[0] = nomeArquivoWAV
    def PlayWAVSlang(self):
        winsound.PlaySound(self.arqWAV[0],winsound.SND_NOSTOP)
    def setWAVShow(self, nomeArquivoWAV):
        '''
        Atualizar o arquivo inicializado como ('') vazio
        :param nomeArquivoWAV:
        :return: void
        '''
        self.arqWAV[1] = nomeArquivoWAV
    def PlayWAVShow(self):
        winsound.PlaySound(self.arqWAV[1],winsound.SND_NOSTOP)
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
        print(" Lantencia: " + str(randomLatenciaAtaque))
        if (attack.latencia <= randomLatenciaAtaque):
            # ATAQUE EFETIVO
            print("SEU ATAQUE FOI EFETIVO\n-------------RANDOM LATENCIA:" + str(randomLatenciaAtaque))
            randomLatenciaDefesa = randint(0, 9)

            if (playerAdversario.shield.latencia <= randomLatenciaDefesa):
                # DEFESA EFETIVA
                dano = System.calculeteDamageShield(playerAdversario, attack)
                playerAdversario.sufferDamage(dano)
                self.userMana(attack.mana)
                self.restoreMana(dano)
                print("Dano verdadeiro:" + str(dano) + "\n")
                print(self)
                print(playerAdversario)

            else:
                # DEFESA NAO EFETIVA
                print("DANO CRITICO")
                dano = System.calculeteDamage(attack)
                playerAdversario.sufferDamage(dano)
                self.userMana(attack.mana)
                self.restoreMana(dano)
                print("Dano verdadeiro:" + str(dano) + "\n")
                print(self)
                print(playerAdversario)
        else:
            # ATAQUE NAO EFETIVO
            print("SEU ATAQUE FALHOU\n-------------RANDOM LATENCIA: " + str(randomLatenciaAtaque))

    def restoreMana(self, dano):
        """
        :param dano: int
        :return: void
        """
        # quanto maior e o dano menos se recupera a mana
        if dano >= 400:
            self.mana += int(1000*(100/dano))
        else:
            self.mana += 300

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


class InteligencePlayer:
    def __init__(self, player, baseDeMana):
        self.player = player
        self.baseDeMana = baseDeMana

    def rankAttack(self, PlayerAdv):
        '''
        Funcao responsavel por rankear os ataques do player
        :param PlayerAdv: Player
        :return: Matriz[3][3]
        '''

        ListAttack = self.player.sword.getAttack()
        ListRank = []
        for indexAttack in range(len(ListAttack)):
            Dano = System.calculeteDamageShield(PlayerAdv, ListAttack[indexAttack])
            ListRank.append([ListAttack[indexAttack], Dano, indexAttack])
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
            ListRank = self.rankAttack(PlayerAdv)
            for linhaMatrizAttack in ListRank:
                if self.player.mana > linhaMatrizAttack[0].mana:
                    return linhaMatrizAttack[2]
            return 3
        else:
            ListRank = self.rankAttack(PlayerAdv)
            for linhaMatrizAttack in ListRank[::-1]:
                if self.player.mana > linhaMatrizAttack[0].mana:
                    return linhaMatrizAttack[2]
            return 3


class Sword:
    def __init__(self, name, attackI, attackII, attackIII):
        self.name = name
        self.attackI = attackI
        self.attackII = attackII
        self.attackIII = attackIII

    def __str__(self):
        ataques = self.getAttack()
        somaDanoMagico = 0
        somaDanoFisico = 0
        samaLatencia = 0

        for ataque in ataques:
            somaDanoMagico += ataque.danoMagico
            somaDanoFisico += ataque.danoFisico
            samaLatencia += ataque.latencia

        mediaDanoMagico = somaDanoMagico / 3
        mediaDanoFisico = somaDanoFisico / 3
        mediaLatencia = samaLatencia / 3

        return ("NOME: " + self.name + "\nLATENCIA (MEDIA): " + str(mediaLatencia) + "\nDEFESA MAGICA (MEDIA) : " + str(
            mediaDanoMagico) + "\nDEFESA FISICA (MEDIA): " + str(mediaDanoFisico))

    def getAttack(self):
        '''
        Funcao responsavel por retornar o ataque requerido pelo PLAYER
        :return: List<Attack>
        '''
        return [self.attackI, self.attackII, self.attackIII]


class Attack:
    def __init__(self, name, mana, latencia, danoMagico, danoFisico):
        self.name = name
        self.mana = mana
        self.latencia = latencia
        self.danoMagico = danoMagico
        self.danoFisico = danoFisico

    def __str__(self):
        # coverter para string
        return ("Nome: " + str(self.name) + "\nDano Magico: " + str(self.danoMagico) + "\nDano Fisico: " + str(
            self.danoFisico) + "\nMana: " + str(self.mana) + "\nLantenci: " + str(self.latencia))


class Shield:
    def __init__(self, name, latencia, defesaMagica, defesaFisica):
        self.name = name
        self.latencia = latencia
        self.defesaMagica = defesaMagica
        self.defesaFisica = defesaFisica

    def __str__(self):
        return (
                    "Nome: " + self.name + "\nLatencia: " + self.latencia + "\nDefesa Magica: " + self.defesaMagica + "\nDefesa Fisica: " + self.defesaFisica)
