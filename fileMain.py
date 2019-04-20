from fileClass import Player, InteligencePlayer, System

System.print('''
MODO é DO JOGO 
    0 - Player x Player
    1 - Player x BOT''', 'NEGRITO')
ModelGame = int(input("DIGITE:"))

while ModelGame != 0 and ModelGame != 1:
    System.print("O NÚMERO ESCOLHIDO É INVÁLIDO", "BLACK")
    ModelGame = int(input("DIGITE:"))

if ModelGame == 0:
    System.print("PLAYER 1 SUA HORA DE SER O MESTRE DA SOCIEDADE DA LÂMINA DE SANGUE", "BLUE")
    System.printPlayers()
    System.print('''HORA DE ESCOLHER O SEU MELHOR HOSPEDEIRO

    EU ESCOLHO HOSPEDAR MINHA MENTE EM: - digite o número do compeão -''', 'RESET')
    indexPlayer1 = int(input("DIGITE:"))

    while indexPlayer1 < 0 or indexPlayer1 >= len(System.listPlayer()):
        System.print("CAMPEÃO INVÁLIDO\n\n", "RED")
        indexPlayer1 = int(input("DIGITE:"))
    # Campeão escolhido
    Player1 = System.choosePlayer(indexPlayer1)
    Player1.PlayWAVShow()

    System.print("PLAYER 2 SUA HORA DE SER O MESTRE DA SOCIEDADE DA LÂMINA DE SANGUE", "RED")
    System.printPlayers()
    System.print('''HORA DE ESCOLHER O SEU MELHOR HOSPEDEIRO
        EU ESCOLHO HOSPEDAR MINHA MENTE EM: - digite o número do compeão -''', 'RESET')
    indexPlayer2 = int(input("DIGITE:"))

    while indexPlayer2 < 0 or indexPlayer2 >= len(System.listPlayer()):
        System.print("CAMPEÃO INVÁLIDO\n\n", "RED")
        indexPlayer2 = int(input("DIGITE:"))
    # Campeão escolhido
    Player2 = System.choosePlayer(indexPlayer2)
    Player2.PlayWAVShow()
    print("-" * 50)
    System.printPlayer(Player1, "BLUE")
    System.printPlayer(Player2, "RED")
    print("-" * 50)
    while True:
        if Player1.hp <= 0:
            System.print('''
            {} TEM A VERDADEIRA MENTE DE UM ASSASSINO! AS SUAS HABILIDADES O FAZ MESTRE DESSA SOCIEDADE! 
            '''.format(Player2.name.upper()), "YELLOW")
            break
        System.print('''
        {} REALIZE O SEU MOVIMENTO. 
        SUA ESPADA TEM SEDE DO MEDO DOS SEUS INIMIGOS!
        '''.format(Player1.name), "BLUE")
        # Imprimir os ataques do Player 1
        System.printPlayer(Player1, "BLUE")
        Player.printAttacks(Player1)

        attacksUser1 = Player1.sword.getAttack()

        # Solicitar que o usuario insira o valor como escolha do ataque
        System.print("ESCOLHA O SEU ATAQUE DE ACORDO COM O INDICE...", "BLACK")
        value = int(input("DIGITE:"))
        while True:
            # Validacao de dados
            if value != 0 and value != 1 and value != 2:
                # Verificar se o player manteve no modo defensivo
                if value == 3:
                    Player1.restoreMana(0)
                    break
                System.print("O INDIDE INVÁDLIDO, TENTE NOVAMENTE...", "RED")
                value = int(input("DIGITE:"))
                continue

            attackP1 = attacksUser1[value]
            if attackP1.mana > Player1.mana:
                System.print('''VOCÊ NÃO TEM MANA SUFICIENTE PARA REALIZER ESSE MOVIMENTO.
                - ESCOLHA OUTRO ATAQUE -
                - MANTENHA MODO DEFENSIVO -''', "BLUE")
                value = int(input("DIGITE:"))
                continue
            else:
                Player1.knock(Player2, attacksUser1[value])
                break
        print("--------------------------------------------------------------")

        if Player2.hp <= 0:
            System.print('''
                        {} TEM A VERDADEIRA MENTE DE UM ASSASSINO! AS SUAS HABILIDADES O FAZ MESTRE DESSA SOCIEDADE! 
                        '''.format(Player1.name.upper()), "YELLOW")
            break
        System.print('''
                {} REALIZE O SEU MOVIMENTO. 
                SUA ESPADA TEM SEDE DO MEDO DOS SEUS INIMIGOS!
                '''.format(Player1.name), "RED")
        # Imprimir os ataques do Player 2
        System.printPlayer(Player2, "RED")
        Player.printAttacks(Player2)

        attacksUser2 = Player2.sword.getAttack()

        # Solicitar que o usuario insira o valor como escolha do ataque
        System.print("ESCOLHA O SEU ATAQUE DE ACORDO COM O INDICE...", "BLACK")
        value = int(input("DIGITE:"))
        while True:
            # Validacao de dados
            if value != 0 and value != 1 and value != 2:
                # Verificar se o player manteve no modo defensivo
                if value == 3:
                    Player2.restoreMana(0)
                    break
                System.print("O INDIDE INVÁDLIDO, TENTE NOVAMENTE...", "RED")
                value = int(input("DIGITE:"))
                continue

            attackP2 = attacksUser2[value]
            if attackP2.mana > Player2.mana:
                System.print('''VOCÊ NÃO TEM MANA SUFICIENTE PARA REALIZER ESSE MOVIMENTO.
                                - ESCOLHA OUTRO ATAQUE -
                                - MANTENHA MODO DEFENSIVO -''', "BLUE")
                value = int(input("DIGITE:"))
                continue
            else:
                Player2.knock(Player1, attacksUser2[value])
                break
        print("--------------------------------------------------------------")
elif ModelGame == 1:
    print("Player 1 escolha o seu Campeao")
    System.printPlayers()
    print("------------------\nO seu Campeao: ")
    indexPlayer1 = int(input())

    while indexPlayer1 < 0 or indexPlayer1 >= len(System.listPlayer()):
        print("o numero escolhido invalido\n\n")
        indexPlayer1 = int(input())
    Player1 = System.choosePlayer(indexPlayer1)
    Player1.PlayWAVShow()

    print("Player 1 escolha o Campeao que deseja infrentar")
    System.printPlayers()
    print("------------------\nCampeao BOT: ")
    indexBOT = int(input())

    while indexBOT < 0 or indexBOT >= len(System.listPlayer()):
        print("o numero escolhido invalido")
        indexBOT = int(input())

    BOT = System.choosePlayer(indexBOT)
    intelBOT = InteligencePlayer(BOT, 200)

    System.printPlayer(Player1, "BLACK")
    System.printPlayer(BOT, "WHITE")

    while True:
        if Player1.hp <= 0:
            print(BOT.name + " É O VERDADEIRO VENCEDOR!!")
            break
        print("\nVoce e o " + Player1.name + ", hora de atacar!")
        # Imprimir os ataques do Player 1
        Player.printAttacks(Player1)

        attacksUser1 = Player1.sword.getAttack()

        # Solicitar que o usuario insira o valor como escolha do ataque
        value = int(input("Escolha o seu Ataque de acordo com o indice\n"))

        while True:
            # Validacao de dados
            if value != 0 and value != 1 and value != 2:
                # Verificar se o player manteve no modo defensivo
                if value == 3:
                    Player1.restoreMana(0)
                    break
                value = int(input("O indice escolhido nao e valido, tente novamente :\n"))
                continue

            attackP1 = attacksUser1[value]
            if attackP1.mana > Player1.mana:
                value = int(input("Voce nao tem mana suficiente para realizar esse ataque\n    Tente outro ataque :\n"))
                continue
            else:
                Player1.knock(BOT, attackP1)
                break
        print("--------------------------------------------------------------")

        if BOT.hp <= 0:
            print(Player1.name + " É O VERDADEIRO VENCEDOR!!")
            break

        attacksBOT = BOT.sword.getAttack()
        value = intelBOT.resolverAttack(Player1)

        print(intelBOT.rankAttack(Player1))

        if value == 3:
            BOT.restoreMana(0)
            continue

        attackBOT = attacksBOT[value]

        print("\n" + BOT.name + " ATACA VOCE COM O " + attackBOT.name + "\n")
        print(attackBOT)
        print("\nValue: " + str(value))

        BOT.knock(Player1, attackBOT)

        print("--------------------------------------------------------------")