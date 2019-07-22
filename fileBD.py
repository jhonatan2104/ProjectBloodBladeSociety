"""
List de atributos do RELATÓRIO de cobate
            "damageTotal": 0
            "damageMagico": 1
            "damageFisico": 2
            "CONTAttackFalhos": 3
            "CONTAttackCriticos": 4
            "CONTAttackNormais": 5
            "CONTAttack": 6
            "FalhaDefesa": 7
            "damageMagicoSofrido": 8
            "damageFisicoSofrido": 9
            "damageMagicoDefendido": 10
            "damageFisicoDefendido": 11
            "manaRestaurada": 12
            "manaGasta": 13

Dados da partida
            ID: 0
            PLAYER: 1
            BOT: 2
            RELATÓRIO : 3
            STATUS: 4

"""


class DAO:
    def __init__(self):
        self.dirProject = "DirTXT"
        self.masterDate = "DAOUser.txt"

    def cadastrar(self, name, senha):
        if not self.isExist(name):
            arqRead = open(f"{self.dirProject}/{self.masterDate}", "r")
            # pagar o que já escrito
            txt = arqRead.readlines()
            arqRead.close()
            arqWrite = open(f"{self.dirProject}/{self.masterDate}", "w")

            newArq = f"User{name.upper()}.txt"
            # escrever no arquivo master
            if len(txt) == 0:
                txt = f"{name}:{senha}:{newArq}"
                arqWrite.writelines(txt)
                arqWrite.close()
            else:
                txt += f"\n{name}:{senha}:{newArq}"
                arqWrite.writelines(txt)
                arqWrite.close()

            arqUser = open(f"{self.dirProject}/{newArq}", "w")
            arqUser.close()
            return True
        else:
            return False

    def isExist(self, nome):
        arqRead = open(f"{self.dirProject}/{self.masterDate}", "r")
        txt = arqRead.readlines()
        arqRead.close()
        for linha in txt:
            Nome,Senha,arq = linha.split(":")
            if Nome.upper() == nome.upper():
                return True
        return False

    def getSenha(self, nome):
        arqRead = open(f"{self.dirProject}/{self.masterDate}", "r")
        txt = arqRead.readlines()
        arqRead.close()
        for linha in txt:
            Nome, Senha, arq = linha.split(":")
            if Nome.upper() == nome.upper():
                return Senha
        return None

    def getArq(self, nome):
        arqRead = open(f"{self.dirProject}/{self.masterDate}", "r")
        txt = arqRead.readlines()
        arqRead.close()
        for linha in txt:
            Nome, Senha, arq = linha.split(":")
            if Nome.upper() == nome.upper():
                return arq
        return None

    def getUser(self, nome):
        arqRead = open(f"{self.dirProject}/{self.masterDate}", "r")
        txt = arqRead.readlines()
        arqRead.close()
        for linha in txt:
            Nome, Senha, arq = linha.split(":")
            if Nome.upper() == nome.upper():
                return User(Nome, Senha, arq)
        return None

    def gerarSTR(self, lista):
        '''
            atributo.info - atributo.info - {...}
        :param dic:
        :return:
        '''
        txt = ""
        for elem in lista:
            txt += f"{elem}-"

        return txt[0:-1]

    def gerarLIST(self, str):
        listDados = list()
        listSTR = str.split("-")
        for date in listSTR:
            listDados.append(int(date))
        return listDados


class User:
    def __init__(self, nome, senha, arq):
        self.dirProject = "DirTXT"
        self.ArqSTR = arq
        self.Senha = senha
        self.Nome = nome

    def addPartida(self, player, adv, lista, win):
        arqRead = open(f"{self.dirProject}/{self.ArqSTR}", "r")
        txt = arqRead.readlines()
        arqRead.close()
        if len(txt) == 0:
            txt += f"0:{player}:{adv}:{lista}:{win}"
        else:
            id = len(txt)
            txt += f"\n{id}:{player}:{adv}:{lista}:{win}"
        arqWrite = open(f"{self.dirProject}/{self.ArqSTR}", "w")
        arqWrite.writelines(txt)
        arqWrite.close()

    def getRelatorioChanp(self, namePlayer):
        arqRead = open(f"{self.dirProject}/{self.ArqSTR}", "r")
        txt = arqRead.readlines()
        arqRead.close()
        listDados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cont = 0

        for linha in txt:
            linha = linha.split(":")
            if linha[1] == namePlayer:
                relatorio = linha[3].split("-")
                for indexAtributo in range(len(relatorio)):
                    listDados[indexAtributo] = listDados[indexAtributo] + int(relatorio[indexAtributo])
                cont += 1
        listMedia = []
        for info in listDados:
            listMedia.append(int(info/cont))
        return listMedia
