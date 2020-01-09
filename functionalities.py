def printGame(tic1, tic2, tic3, tic4, tic5, tic6, tic7, tic8, tic9, turnBoard = 0):
    ## This function will print the game after each turn:
    if turnBoard == 0:
        print(f"{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}")

    elif turnBoard == 1:
        print(f"\033[32m{tic1[0]}\033[m   {tic2[0]}   {tic3[0]}")
        print(f"\033[32m{tic1[1]}\033[m   {tic2[1]}   {tic3[1]}")
        print(f"\033[32m{tic1[2]}\033[m   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}")

    elif turnBoard == 2:
        print(f"{tic1[0]}   \033[32m{tic2[0]}\033[m   {tic3[0]}")
        print(f"{tic1[1]}   \033[32m{tic2[1]}\033[m   {tic3[1]}")
        print(f"{tic1[2]}   \033[32m{tic2[2]}\033[m   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}")

    elif turnBoard == 3:
        print(f"{tic1[0]}   {tic2[0]}   \033[32m{tic3[0]}\033[m")
        print(f"{tic1[1]}   {tic2[1]}   \033[32m{tic3[1]}\033[m")
        print(f"{tic1[2]}   {tic2[2]}   \033[32m{tic3[2]}\033[m")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}")

    elif turnBoard == 4:
        print(f"{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"\033[32m{tic4[0]}\033[m   {tic5[0]}   {tic6[0]}")
        print(f"\033[32m{tic4[1]}\033[m   {tic5[1]}   {tic6[1]}")
        print(f"\033[32m{tic4[2]}\033[m   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}")

    elif turnBoard == 5:
        print(f"{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   \033[32m{tic5[0]}\033[m   {tic6[0]}")
        print(f"{tic4[1]}   \033[32m{tic5[1]}\033[m   {tic6[1]}")
        print(f"{tic4[2]}   \033[32m{tic5[2]}\033[m   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}")

    elif turnBoard == 6:
        print(f"{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   \033[32m{tic6[0]}\033[m")
        print(f"{tic4[1]}   {tic5[1]}   \033[32m{tic6[1]}\033[m")
        print(f"{tic4[2]}   {tic5[2]}   \033[32m{tic6[2]}\033[m")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}")

    elif turnBoard == 7:
        print(f"{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"\033[32m{tic7[0]}\033[m   {tic8[0]}   {tic9[0]}")
        print(f"\033[32m{tic7[1]}\033[m   {tic8[1]}   {tic9[1]}")
        print(f"\033[32m{tic7[2]}\033[m   {tic8[2]}   {tic9[2]}")

    elif turnBoard == 8:
        print(f"{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   \033[32m{tic8[0]}\033[m   {tic9[0]}")
        print(f"{tic7[1]}   \033[32m{tic8[1]}\033[m   {tic9[1]}")
        print(f"{tic7[2]}   \033[32m{tic8[2]}\033[m   {tic9[2]}")

    elif turnBoard == 9:
        print(f"{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   \033[32m{tic9[0]}\033[m")
        print(f"{tic7[1]}   {tic8[1]}   \033[32m{tic9[1]}\033[m")
        print(f"{tic7[2]}   {tic8[2]}   \033[32m{tic9[2]}\033[m")




def checkWin(l1, l2, l3, c1, c2, c3, d1, d2):
    ## This function will check to see if the game being played was won by the player or not:
    if l1 == ["X", "X", "X"] or l2 == ["X", "X", "X"] or l3 == ["X", "X", "X"]:
        return ["True", "1"]
    elif c1 == ["X", "X", "X"]or c2 == ["X", "X", "X"]or c3 == ["X", "X", "X"]:
        return ["True", "1"]
    elif d1 == ["X", "X", "X"] or d2 == ["X", "X", "X"]:
        return ["True", "1"]


    if l1 == ["O", "O", "O"] or l2 == ["O", "O", "O"] or l3 == ["O", "O", "O"]:
        return ["True", "2"]
    elif c1 == ["O", "O", "O"] or c2 == ["O", "O", "O"] or c3 == ["O", "O", "O"]:
        return ["True", "2"]
    elif d1 == ["O", "O", "O"] or d2 == ["O", "O", "O"]:
        return ["True", "2"]
    else:
        return ["False", ""]


def MajorWin(game1, game2, game3):
    ## This function will check to see if the "big tictactoe" was won by some player or not:
    if game1[3] == "True" and game2[3] == "True" and game3[3] == "True":
        if game1[4] == game2[4] == game3[4]:
            return game1[4]
        else:
            return False
    else:
        return False



def updateBoard(l1, l2, l3, input, player):
    ## This function will update the game after each turn:
    if input == 1:
        if player == 1:
            l1[0] = "X"
        elif player == 2:
            l1 [0] = "O"

    elif input == 2:
        if player == 1:
            l1[1] = "X"
        elif player == 2:
            l1 [1] = "O"

    elif input == 3:
        if player == 1:
            l1[2] = "X"
        elif player == 2:
            l1 [2] = "O"

    elif input == 4:
        if player == 1:
            l2[0] = "X"
        elif player == 2:
            l2[0] = "O"

    elif input == 5:
        if player == 1:
            l2[1] = "X"
        elif player == 2:
            l2[1] = "O"

    elif input == 6:
        if player == 1:
            l2[2] = "X"
        elif player == 2:
            l2[2] = "O"

    elif input == 7:
        if player == 1:
            l3[0] = "X"
        elif player == 2:
            l3[0] = "O"

    elif input == 8:
        if player == 1:
            l3[1] = "X"
        elif player == 2:
            l3[1] = "O"

    elif input == 9:
        if player == 1:
            l3[2] = "X"
        elif player == 2:
            l3[2] = "O"


# remake these functions.
def updateColumn(l1, l2 , l3, cNum):
    ## Update column variables after each turn:
    return [l1[cNum], l2[cNum], l3[cNum]]


def title(title):
    ## This function is used for formatting and neat printing purposes:
    print()
    print("="*45)
    print(title.center(45))
    print("="*45)
    print()

def checkCompletion(validPlays, turnBoard):
    ## This function will check if the next board that the player would play on is already complete or not.
    # If it is, the player will select another board to play:
    turnBoard -= 1
    if len(validPlays[turnBoard]) == 0:
        return True
    else:
        return False

def completeBoard(player):
    ## After a board is won, this function will fill it with "X" or "O" depending on the player who won it:
    if player == 1:
        line = ["X","X","X"]
        return line
    elif player == 2:
        line = ["O","O","O"]
        return line

def winningPrint(tic1, tic2, tic3, tic4, tic5, tic6, tic7, tic8, tic9, player):
    ## This function will print the game board in the colour of the winning player:
    if player == 1:
        print(f"\033[36m{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}\033[m")

    else:
        print(f"\033[31m{tic1[0]}   {tic2[0]}   {tic3[0]}")
        print(f"{tic1[1]}   {tic2[1]}   {tic3[1]}")
        print(f"{tic1[2]}   {tic2[2]}   {tic3[2]}")
        print()
        print()
        print(f"{tic4[0]}   {tic5[0]}   {tic6[0]}")
        print(f"{tic4[1]}   {tic5[1]}   {tic6[1]}")
        print(f"{tic4[2]}   {tic5[2]}   {tic6[2]}")
        print()
        print()
        print(f"{tic7[0]}   {tic8[0]}   {tic9[0]}")
        print(f"{tic7[1]}   {tic8[1]}   {tic9[1]}")
        print(f"{tic7[2]}   {tic8[2]}   {tic9[2]}\033[m")


def velha(listofplays):
    length = len(listofplays)
    c = 0
    count = 0
    while c != length:
        if len(listofplays[c]) == 0:
            count += 1
        if count == 8:
            return True
        c += 1
