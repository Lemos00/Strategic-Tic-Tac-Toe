from functionalities import *


# A square or game consists of the list [line1, line2, line3, (if it is already completed),
# who completed it]
# game 1:

tic1 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column11 = [tic1[0][0], tic1[1][0], tic1[2][0]]
column12 = [tic1[0][1], tic1[1][1], tic1[2][1]]
column13 = [tic1[0][2], tic1[2][2], tic1[2][2]]
diagonal11 = [tic1[0][0], tic1[1][1], tic1[2][2]]
diagonal12 = [tic1[2][0], tic1[1][1], tic1[0][2]]


# game 2:
tic2 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column21 = [tic2[0][0], tic2[1][0], tic2[2][0]]
column22 = [tic2[0][1], tic2[1][1], tic2[2][1]]
column23 = [tic2[0][2], tic2[2][2], tic2[2][2]]
diagonal21 = [tic2[0][0], tic2[1][1], tic2[2][2]]
diagonal22 = [tic2[2][0], tic2[1][1], tic2[0][2]]


# game 3:
tic3 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column31 = [tic3[0][0], tic3[1][0], tic3[2][0]]
column32 = [tic3[0][1], tic3[1][1], tic3[2][1]]
column33 = [tic3[0][2], tic3[2][2], tic3[2][2]]
diagonal31 = [tic3[0][0], tic3[1][1], tic3[2][2]]
diagonal32 = [tic3[2][0], tic3[1][1], tic3[0][2]]

# game 4:
tic4 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column41 = [tic4[0][0], tic4[1][0], tic4[2][0]]
column42 = [tic4[0][1], tic4[1][1], tic4[2][1]]
column43 = [tic4[0][2], tic4[2][2], tic4[2][2]]
diagonal41 = [tic4[0][0], tic4[1][1], tic4[2][2]]
diagonal42 = [tic4[2][0], tic4[1][1], tic4[0][2]]

# game 5:
tic5 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column51 = [tic5[0][0], tic5[1][0], tic5[2][0]]
column52 = [tic5[0][1], tic5[1][1], tic5[2][1]]
column53 = [tic5[0][2], tic5[2][2], tic5[2][2]]
diagonal51 = [tic5[0][0], tic5[1][1], tic5[2][2]]
diagonal52 = [tic5[2][0], tic5[1][1], tic5[0][2]]

# game 6:
tic6 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column61 = [tic6[0][0], tic6[1][0], tic6[2][0]]
column62 = [tic6[0][1], tic6[1][1], tic6[2][1]]
column63 = [tic6[0][2], tic6[2][2], tic6[2][2]]
diagonal61 = [tic6[0][0], tic6[1][1], tic6[2][2]]
diagonal62 = [tic6[2][0], tic6[1][1], tic6[0][2]]

# game 7:
tic7 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column71 = [tic7[0][0], tic7[1][0], tic7[2][0]]
column72 = [tic7[0][1], tic7[1][1], tic7[2][1]]
column73 = [tic7[0][2], tic7[2][2], tic7[2][2]]
diagonal71 = [tic7[0][0], tic7[1][1], tic7[2][2]]
diagonal72 = [tic7[2][0], tic7[1][1], tic7[0][2]]

# game 8:
tic8 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column81 = [tic8[0][0], tic8[1][0], tic8[2][0]]
column82 = [tic8[0][1], tic8[1][1], tic8[2][1]]
column83 = [tic8[0][2], tic8[2][2], tic8[2][2]]
diagonal81 = [tic8[0][0], tic8[1][1], tic8[2][2]]
diagonal82 = [tic8[2][0], tic8[1][1], tic8[0][2]]

# game 9:
tic9 = [[" "," "," "], [" "," "," "], [" "," "," "], "False", ""]
column91 = [tic9[0][0], tic9[1][0], tic9[2][0]]
column92 = [tic9[0][1], tic9[1][1], tic9[2][1]]
column93 = [tic9[0][2], tic9[2][2], tic9[2][2]]
diagonal91 = [tic9[0][0], tic9[1][1], tic9[2][2]]
diagonal92 = [tic9[2][0], tic9[1][1], tic9[0][2]]

# Player names:
player1 = str(input("Player 1: "))
player2 = str(input("Player 2: "))

# valid plays for each block of tic tac toe:
validPlays1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validPlays2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validPlays3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validPlays4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validPlays5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validPlays6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validPlays7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validPlays8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
validPlays9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

listofPlays = [validPlays1, validPlays2, validPlays3 , validPlays4, validPlays5, validPlays6, validPlays7 ,validPlays8,
               validPlays9]

title("Lets play NES.TICTAC")

# Initial variables for initial game formatting:
win = False
playNumber = 1
turnBoard = 0
player = 0
newBoard = True

# Loop that will only stop when the game is won.
while not win:
    printGame(tic1, tic2, tic3, tic4, tic5, tic6, tic7, tic8, tic9, turnBoard)


    if playNumber % 2 != 0:
        print(f"\033[1;36mTurn: {player1}\033[m")
        player = 1
    elif playNumber % 2 == 0:
        print(f"\033[1;31mTurn: {player2}\033[m")
        player = 2

    # the board in which the turn is being played on:
    # Start of the game. Choosing the first board in which the game will start on:
    if newBoard == True:
        firstChoice = 0
        while firstChoice not in range(1, 10):
            if playNumber == 1:
                firstChoice = str(input(f"\033[1;32m{player1}, select the board you would like to start at\n"
                                        f"Board number [1 to 9]: \033[m"))
            else:
                if player == 1:
                    firstChoice = str(input(f"\033[1;32m{player1}, select the board you would like to play at\n"
                                            f"Board number [1 to 9]: \033[m"))
                else:
                    firstChoice = str(input(f"\033[1;32m{player2}, select the board you would like to play at\n"
                                            f"Board number [1 to 9]: \033[m"))
            try:
                firstChoice = int(firstChoice)
            except:
                print("\033[31mInvalid character, please try again\033[m")
            else:
                if firstChoice not in range(1, 10):
                    print("\033[31mInvalid number, please try again\033[m")
        turnBoard = int(firstChoice)
        newBoard = False

    play = 0

    # making a play:
    while play not in range(1, 10):
        play = str(input(f"Make your play in Board {turnBoard}: "))

        try:
            play = int(play)
        except:
            print("\033[31mInvalid character, please try again\033[m")
        else: # if the play is valid:
            if play not in range(1, 10):
                print("\033[31mInvalid number, please try again\033[m")
            else:
                continue

    # checking for valid play:
    valid = False

    while not valid:
        if play not in listofPlays[turnBoard - 1]:
            print("\033[31mThis spot is taken, please try again\033[m")
            play = str(input(f"Make your play in Board {turnBoard}: "))

            try:
                play = int(play)
            except:
                print("\033[31mInvalid character, please try again\033[m")
            else:
                if play not in range(1, 10):
                    print("\033[31mInvalid number, please try again\033[m")
                else:
                    continue
        else:
            listofPlays[turnBoard - 1].remove(play)
            break


    # Updating the board of the game:
    if turnBoard == 1:
        updateBoard(tic1[0], tic1[1], tic1[2], play, player)
        column11 = updateColumn(tic1[0], tic1[1], tic1[2], 0)
        column12 = updateColumn(tic1[0], tic1[1], tic1[2], 1)
        column13 = updateColumn(tic1[0], tic1[1], tic1[2], 2)
        diagonal11 = [tic1[0][0], tic1[1][1], tic1[2][2]]
        diagonal12 = [tic1[2][0], tic1[1][1], tic1[0][2]]



    if turnBoard == 2:
        updateBoard(tic2[0], tic2[1], tic2[2], play, player)
        column21 = updateColumn(tic2[0], tic2[1], tic2[2], 0)
        column22 = updateColumn(tic2[0], tic2[1], tic2[2], 1)
        column23 = updateColumn(tic2[0], tic2[1], tic2[2], 2)
        diagonal21 = [tic2[0][0], tic2[1][1], tic2[2][2]]
        diagonal22 = [tic2[2][0], tic2[1][1], tic2[0][2]]

    if turnBoard == 3:
        updateBoard(tic3[0], tic3[1], tic3[2], play, player)
        column31 = updateColumn(tic3[0], tic3[1], tic3[2], 0)
        column32 = updateColumn(tic3[0], tic3[1], tic3[2], 1)
        column33 = updateColumn(tic3[0], tic3[1], tic3[2], 2)
        diagonal31 = [tic3[0][0], tic3[1][1], tic3[2][2]]
        diagonal32 = [tic3[2][0], tic3[1][1], tic3[0][2]]


    if turnBoard == 4:
        updateBoard(tic4[0], tic4[1], tic4[2], play, player)
        column41 = updateColumn(tic4[0], tic4[1], tic4[2], 0)
        column42 = updateColumn(tic4[0], tic4[1], tic4[2], 1)
        column43 = updateColumn(tic4[0], tic4[1], tic4[2], 2)
        diagonal41 = [tic4[0][0], tic4[1][1], tic4[2][2]]
        diagonal42 = [tic4[2][0], tic4[1][1], tic4[0][2]]


    if turnBoard == 5:
        updateBoard(tic5[0], tic5[1], tic5[2], play, player)
        column51 = updateColumn(tic5[0], tic5[1], tic5[2], 0)
        column52 = updateColumn(tic5[0], tic5[1], tic5[2], 1)
        column53 = updateColumn(tic5[0], tic5[1], tic5[2], 2)
        diagonal51 = [tic5[0][0], tic5[1][1], tic5[2][2]]
        diagonal52 = [tic5[2][0], tic5[1][1], tic5[0][2]]

    if turnBoard == 6:
        updateBoard(tic6[0], tic6[1], tic6[2], play, player)
        column61 = updateColumn(tic6[0], tic6[1], tic6[2], 0)
        column62 = updateColumn(tic6[0], tic6[1], tic6[2], 1)
        column63 = updateColumn(tic6[0], tic6[1], tic6[2], 2)
        diagonal61 = [tic6[0][0], tic6[1][1], tic6[2][2]]
        diagonal62 = [tic6[2][0], tic6[1][1], tic6[0][2]]

    if turnBoard == 7:
        updateBoard(tic7[0], tic7[1], tic7[2], play, player)
        column71 = updateColumn(tic7[0], tic7[1], tic7[2], 0)
        column72 = updateColumn(tic7[0], tic7[1], tic7[2], 1)
        column73 = updateColumn(tic7[0], tic7[1], tic7[2], 2)
        diagonal71 = [tic7[0][0], tic7[1][1], tic7[2][2]]
        diagonal72 = [tic7[2][0], tic7[1][1], tic7[0][2]]

    if turnBoard == 8:
        updateBoard(tic8[0], tic8[1], tic8[2], play, player)
        column81 = updateColumn(tic8[0], tic8[1], tic8[2], 0)
        column82 = updateColumn(tic8[0], tic8[1], tic8[2], 1)
        column83 = updateColumn(tic8[0], tic8[1], tic8[2], 2)
        diagonal81 = [tic8[0][0], tic8[1][1], tic8[2][2]]
        diagonal82 = [tic8[2][0], tic8[1][1], tic8[0][2]]

    if turnBoard == 9:
        updateBoard(tic9[0], tic9[1], tic9[2], play, player)
        column91 = updateColumn(tic9[0], tic9[1], tic9[2], 0)
        column92 = updateColumn(tic9[0], tic9[1], tic9[2], 1)
        column93 = updateColumn(tic9[0], tic9[1], tic9[2], 2)
        diagonal91 = [tic9[0][0], tic9[1][1], tic9[2][2]]
        diagonal92 = [tic9[2][0], tic9[1][1], tic9[0][2]]


    # checking if there is a win. If there is, there are no valid plays at that game anymore:
    check = checkWin(tic1[0], tic1[1], tic1[2], column11, column12, column13, diagonal11, diagonal12)
    tic1[3] = check[0]
    tic1[4] = check[1]
    if tic1[3] == "True":
        validPlays1 = []
        if player == int(tic1[4]):
            tic1[0] = completeBoard(player)
            tic1[1] = completeBoard(player)
            tic1[2] = completeBoard(player)

    check = checkWin(tic2[0], tic2[1], tic2[2], column21, column22, column23, diagonal21, diagonal22)
    tic2[3] = check[0]
    tic2[4] = check[1]
    if tic2[3] == "True":
        validPlays2 = []
        if player == int(tic2[4]):
            tic2[0] = completeBoard(player)
            tic2[1] = completeBoard(player)
            tic2[2] = completeBoard(player)

    check = checkWin(tic3[0], tic3[1], tic3[2], column31, column32, column33, diagonal31, diagonal32)
    tic3[3] = check[0]
    tic3[4] = check[1]
    if tic3[3] == "True":
        validPlays3 = []
        if player == int(tic3[4]):
            tic3[0] = completeBoard(player)
            tic3[1] = completeBoard(player)
            tic3[2] = completeBoard(player)

    check = checkWin(tic4[0], tic4[1], tic4[2], column41, column42, column43, diagonal41, diagonal42)
    tic4[3] = check[0]
    tic4[4] = check[1]
    if tic4[3] == "True":
        validPlays4 = []
        if player == int(tic4[4]):
            tic4[0] = completeBoard(player)
            tic4[1] = completeBoard(player)
            tic4[2] = completeBoard(player)

    check = checkWin(tic5[0], tic5[1], tic5[2], column51, column52, column53, diagonal51, diagonal52)
    tic5[3] = check[0]
    tic5[4] = check[1]
    if tic5[3] == "True":
        validPlays5 = []
        if player == int(tic5[4]):
            tic5[0] = completeBoard(player)
            tic5[1] = completeBoard(player)
            tic5[2] = completeBoard(player)

    check = checkWin(tic6[0], tic6[1], tic6[2], column61, column62, column63, diagonal61, diagonal62)
    tic6[3] = check[0]
    tic6[4] = check[1]
    if tic6[3] == "True":
        validPlays6 = []
        if player == int(tic6[4]):
            tic6[0] = completeBoard(player)
            tic6[1] = completeBoard(player)
            tic6[2] = completeBoard(player)

    check = checkWin(tic7[0], tic7[1], tic7[2], column71, column72, column73, diagonal71, diagonal72)
    tic7[3] = check[0]
    tic7[4] = check[1]
    if tic7[3] == "True":
        validPlays7 = []
        if player == int(tic7[4]):
            tic7[0] = completeBoard(player)
            tic7[1] = completeBoard(player)
            tic7[2] = completeBoard(player)

    check = checkWin(tic8[0], tic8[1], tic8[2], column81, column82, column83, diagonal81, diagonal82)
    tic8[3] = check[0]
    tic8[4] = check[1]
    if tic8[3] == "True":
        validPlays8 = []
        if player == int(tic8[4]):
            tic8[0] = completeBoard(player)
            tic8[1] = completeBoard(player)
            tic8[2] = completeBoard(player)

    check = checkWin(tic9[0], tic9[1], tic9[2], column91, column92, column93, diagonal91, diagonal92)
    tic9[3] = check[0]
    tic9[4] = check[1]
    if tic9[3] == "True":
        validPlays9 = []
        if player == int(tic9[4]):
            tic9[0] = completeBoard(player)
            tic9[1] = completeBoard(player)
            tic9[2] = completeBoard(player)

    # game check will receive "False" if the game is not finished or the number of the winning player:

    gameCheck = MajorWin(tic1, tic2, tic3)
    if gameCheck != False:
        break

    gameCheck = MajorWin(tic4, tic5, tic6)
    if gameCheck != False:
        break

    gameCheck = MajorWin(tic7, tic8, tic9)
    if gameCheck != False:
        break

    gameCheck = MajorWin(tic1, tic4, tic7)
    if gameCheck != False:
        break

    gameCheck = MajorWin(tic2, tic5, tic8)
    if gameCheck != False:
        break

    gameCheck = MajorWin(tic3, tic6, tic9)
    if gameCheck != False:
        break

    gameCheck = MajorWin(tic1, tic5, tic9)
    if gameCheck != False:
        break

    gameCheck = MajorWin(tic7, tic5, tic3)
    if gameCheck != False:
        break


    # At the end of a turn:
    turnBoard = play

    # Update the list of plays:
    listofPlays = [validPlays1, validPlays2, validPlays3, validPlays4, validPlays5, validPlays6, validPlays7,
                   validPlays8,validPlays9]

    #Check to see if the next play will be played in a completed board. If so, player selects another board to play on:
    newBoard = checkCompletion(listofPlays, turnBoard)
    noWinner = velha(listofPlays) # will check to see if the game had no winners (all slots occupied)

    #This will only happen if all possible plays were made and no one can possibly win the game:
    if noWinner == True:
        print("THE GAME HAD NO WINNER, THANK YOU FOR PLAYING :)")
        exit(0)

    playNumber += 1

if player == 1:
    winningPrint(tic1, tic2, tic3, tic4, tic5, tic6, tic7, tic8, tic9, player)
    title(f"\033[36mCONGRATULATIONS {player1}!!!!!\033[m")
    print("YOU WON THIS MATCH OF STRATEGIC TIC TAC TOE!")

else:
    winningPrint(tic1, tic2, tic3, tic4, tic5, tic6, tic7, tic8, tic9, player)
    title(f"\033[31mCONGRATULATIONS {player2}!!!!!\033[m")
    print("YOU WON THIS MATCH OF STRATEGIC TIC TAC TOE!")
