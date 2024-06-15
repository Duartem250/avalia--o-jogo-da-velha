jogo = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
jogadas = 0
while True:
    print("O jogador X irá iniciar")
    linhax = int(input("Informe a linha da jogada:"))
    colunax = int(input("Informe a coluna da jogada:"))
    if jogo[linhax][colunax] == "":
        jogo[linhax][colunax] = "X"
        jogadas += 1
        if (jogo[0][0] == "X" and jogo[0][1] == "X" and jogo[0][2] == "X"):
            print("O jogador X venceu!!")
            break
        elif (jogo[1][0] == "X" and jogo[1][1] == "X" and jogo[1][2] == "X"):
            print("O jogador X venceu!!")
            break
        elif (jogo[2][0] == "X" and jogo[2][1] == "X" and jogo[2][2] == "X"):
            print("O jogador X venceu!!")
            break
        elif (jogo[0][0] == "X" and jogo[1][0] == "X" and jogo[2][0] == "X"):
            print("O jogador X venceu!!")
            break
        elif (jogo[0][1] == "X" and jogo[1][1] == "X" and jogo[2][1] == "X"):
            print("O jogador X venceu!!")
            break
        elif (jogo[0][2] == "X" and jogo[1][2] == "X" and jogo[2][2] == "X"):
            print("O jogador X venceu!!")
            break
        elif (jogo[0][0] == "X" and jogo[1][1] == "X" and jogo[2][2] == "X"):
            print("O jogador X venceu!!")
            break
        elif (jogo[0][2] == "X" and jogo[1][1] == "X" and jogo[2][0] == "X"):
            print("O jogador X venceu!!")
            break
        elif jogadas == 9:
            print("Não houve vencedor!")
            break
    else:
        print("Essa posição já está ocupada. Tente novamente, caso realize a mesma jogada anterior você irá perder a vez!")
        linhax = int(input("Informe a linha da jogada:"))
        colunax = int(input("Informe a coluna da jogada:"))
        if jogo[linhax][colunax] == "":
            jogo[linhax][colunax] = "X"
            jogadas += 1
            if (jogo[0][0] == "X" and jogo[0][1] == "X" and jogo[0][2] == "X"):
                print("O jogador X venceu!!")
                break
            elif (jogo[1][0] == "X" and jogo[1][1] == "X" and jogo[1][2] == "X"):
                print("O jogador X venceu!!")
                break
            elif (jogo[2][0] == "X" and jogo[2][1] == "X" and jogo[2][2] == "X"):
                print("O jogador X venceu!!")
                break
            elif (jogo[0][0] == "X" and jogo[1][0] == "X" and jogo[2][0] == "X"):
                print("O jogador X venceu!!")
                break
            elif (jogo[0][1] == "X" and jogo[1][1] == "X" and jogo[2][1] == "X"):
                print("O jogador X venceu!!")
                break
            elif (jogo[0][2] == "X" and jogo[1][2] == "X" and jogo[2][2] == "X"):
                print("O jogador X venceu!!")
                break
            elif (jogo[0][0] == "X" and jogo[1][1] == "X" and jogo[2][2] == "X"):
                print("O jogador X venceu!!")
                break
            elif (jogo[0][2] == "X" and jogo[1][1] == "X" and jogo[2][0] == "X"):
                print("O jogador X venceu!!")
                break
            elif jogadas == 9:
                print("Não houve vencedor!")
                break
    for l in range(3):
        for c in range(3):
            print(f'[{jogo[l][c]: ^5}]', end='')
        print()
    print("O jogador O irá iniciar")
    linhao = int(input("Informe a linha da jogada:"))
    colunao = int(input("Informe a coluna da jogada:"))
    if jogo[linhao][colunao] == "":
        jogo[linhao][colunao] = "O"
        jogadas += 1
        if (jogo[0][0] == "O" and jogo[0][1] == "O" and jogo[0][2] == "O"):
            print("O jogador O venceu!!")
            break
        elif (jogo[1][0] == "O" and jogo[1][1] == "O" and jogo[1][2] == "O"):
            print("O jogador O venceu!!")
            break
        elif (jogo[2][0] == "O" and jogo[2][1] == "O" and jogo[2][2] == "O"):
            print("O jogador O venceu!!")
            break
        elif (jogo[0][0] == "O" and jogo[1][0] == "O" and jogo[2][0] == "O"):
            print("O jogador O venceu!!")
            break
        elif (jogo[0][1] == "O" and jogo[1][1] == "O" and jogo[2][1] == "O"):
            print("O jogador O venceu!!")
            break
        elif (jogo[0][2] == "O" and jogo[1][2] == "O" and jogo[2][2] == "O"):
            print("O jogador O venceu!!")
            break
        elif (jogo[0][0] == "O" and jogo[1][1] == "O" and jogo[2][2] == "O"):
            print("O jogador O venceu!!")
            break
        elif (jogo[0][2] == "O" and jogo[1][1] == "O" and jogo[2][0] == "O"):
            print("O jogador O venceu!!")
            break
        elif jogadas == 9:
            print("Não houve vencedor!")
            break
    else:
        print("Essa posição já está ocupada. Tente novamente, caso realize a mesma jogada anterior você irá perder a vez!")
        inhao = int(input("Informe a linha da jogada:"))
        colunao = int(input("Informe a coluna da jogada:"))
        if jogo[linhao][colunao] == "":
            jogo[linhao][colunao] = "O"
            jogadas += 1
            if (jogo[0][0] == "O" and jogo[0][1] == "O" and jogo[0][2] == "O"):
                print("O jogador O venceu!!")
                break
            elif (jogo[1][0] == "O" and jogo[1][1] == "O" and jogo[1][2] == "O"):
                print("O jogador O venceu!!")
                break
            elif (jogo[2][0] == "O" and jogo[2][1] == "O" and jogo[2][2] == "O"):
                print("O jogador O venceu!!")
                break
            elif (jogo[0][0] == "O" and jogo[1][0] == "O" and jogo[2][0] == "O"):
                print("O jogador O venceu!!")
                break
            elif (jogo[0][1] == "O" and jogo[1][1] == "O" and jogo[2][1] == "O"):
                print("O jogador O venceu!!")
                break
            elif (jogo[0][2] == "O" and jogo[1][2] == "O" and jogo[2][2] == "O"):
                print("O jogador O venceu!!")
                break
            elif (jogo[0][0] == "O" and jogo[1][1] == "O" and jogo[2][2] == "O"):
                print("O jogador O venceu!!")
                break
            elif (jogo[0][2] == "O" and jogo[1][1] == "O" and jogo[2][0] == "O"):
                print("O jogador O venceu!!")
                break
            elif jogadas == 9:
                print("Não houve vencedor!")
                break
    for l in range(3):
        for c in range(3):
            print(f'[{jogo[l][c]: ^5}]', end='')
        print()
for l in range(3):
        for c in range(3):
            print(f'[{jogo[l][c]: ^5}]', end='')
        print()
    
    






    
