from fileClass import Player,InteligencePlayer,System
print("MODO é DO JOGO \n0 - Player x Player\n1 - Player x BOT")
ModelGame = int(input())

while ModelGame != 0 and ModelGame != 1:
    print("o numero escolhido invalido")
    ModelGame = int(input())

if ModelGame == 0:
    print("Player 1 escolha o seu Campeão")
    System.printPlayers()
    print("------------------\nO seu Campeão: ")
    indexPlayer1 = int(input())

    while indexPlayer1 < 0 or indexPlayer1 >= len(System.listPlayer()):
        print("CAMPEÃO INVÁLIDO\n\n")
        indexPlayer1 = int(input())
    #Campeão escolhido
    Player1 = System.choosePlayer(indexPlayer1)

    print("Player 2 escolha o seu Campeão")
    System.printPlayers()
    print("------------------\nO seu Campeão: ")
    indexPlayer2 = int(input())

    while indexPlayer2 < 0 or indexPlayer2 >= len(System.listPlayer()):
        print("CAMPEÃO INVÁLIDO\n\n")
        indexPlayer2 = int(input())
    # Campeão escolhido
    Player2 = System.choosePlayer(indexPlayer2)

    print(Player1)
    print(Player2)

    while True:
        if Player1.hp <= 0:
            print(Player2.name+" É O VERDADEIRO VENCEDOR!!")
            break
        print("\nVocê é o " + Player1.name + ", hora de atacar!")
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

                value = int(input("O indice escolhido não é válido, tente novamente :\n"))
                continue

            attackP1 = attacksUser1[value]
            if attackP1.mana > Player1.mana:
                value = int(input("Você não tem mana suficiente para realizar esse ataque\n Tente outro ataque :\n"))
                continue
            else:
                Player1.knock(Player2, attacksUser1[value])
                break
        print("--------------------------------------------------------------")

        if Player2.hp <= 0:
            print(Player1.name + " É O VERDADEIRO VENCEDOR!!")
            break
        print("\nVoce e o " + Player2.name + ", hora de atacar!")
        # Imprimir os ataques do Player 2
        Player.printAttacks(Player2)

        attacksUser2 = Player2.sword.getAttack()

        # Solicitar que o usuario insira o valor como escolha do ataque
        value = int(input("Escolha o seu Ataque de acordo com o indice\n"))
        while True:
            # Validacao de dados
            if value != 0 and value != 1 and value != 2:
                # Verificar se o player manteve no modo defensivo
                if value == 3:
                    Player2.restoreMana(0)
                    break

                value = int(input("O indice escolhido nao e valido, tente novamente :\n"))
                continue

            attackP2 = attacksUser2[value]
            if attackP2.mana > Player2.mana:
                value = int(input("Voce nao tem mana suficiente para realizar esse ataque\n Tente outro ataque :\n"))
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

    print("Player 1 escolha o Campeao que deseja infrentar")
    System.printPlayers()
    print("------------------\nCampeao BOT: ")
    indexBOT = int(input())

    while indexBOT < 0 or indexBOT >= len(System.listPlayer()):
        print("o numero escolhido invalido")
        indexBOT = int(input())

    BOT = System.choosePlayer(indexBOT)
    intelBOT = InteligencePlayer(BOT, 200)

    print(Player1)
    print(BOT)

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