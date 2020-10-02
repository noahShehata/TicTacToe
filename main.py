tiktactoeBoard = [["_","_","_"],["_","_","_"],["_","_","_"]]
player = "X"
keepGoing = True
currentPlayer = True


def game():
  gameBoard = tiktactoeBoard
  sideNumber = 1
  for i,j in enumerate(gameBoard):
    print (*j, end = "     ")
    print (sideNumber, sideNumber + 1, sideNumber + 2)
    sideNumber = sideNumber + 3
  userInput = int(input("Select 1-9 to place your X or O"))

  if userInput == 1:
    gameBoard[0][0] = player
  elif userInput == 2:
    gameBoard[0][1] = player
  elif userInput == 3:
    gameBoard[0][2] = player
  elif userInput == 4:
    gameBoard[1][0] = player
  elif userInput == 5:
    gameBoard[1][1] = player
  elif userInput == 6:
    gameBoard[1][2] = player
  elif userInput == 7:
    gameBoard[2][0] = player
  elif userInput == 8:
    gameBoard[2][1] = player
  elif userInput == 9:
    gameBoard[2][2] = player
  return gameBoard

def switchPlayer(gameBoard):
  global currentPlayer
  global player
  if (currentPlayer):
    player = "O"
    currentPlayer = not currentPlayer
  else:
    player = "X"
    currentPlayer = not currentPlayer
  return gameBoard

def checkWins(gameBoard):
  row0 = gameBoard[0][0] + gameBoard[0][1] + gameBoard[0][2]
  row1 = gameBoard[1][0] + gameBoard[1][1] + gameBoard[1][2]
  row2 = gameBoard[2][0] + gameBoard[2][1] + gameBoard[2][2]

  column0 = gameBoard[0][0] + gameBoard[1][0] + gameBoard[2][0]
  column1 = gameBoard[0][1] + gameBoard[1][1] + gameBoard[2][1]
  column2 = gameBoard[0][2] + gameBoard[2][1] + gameBoard[2][2]


  diagnol0 = gameBoard[0][0] + gameBoard[1][1] + gameBoard[2][2]
  diagnol1 = gameBoard[0][2] + gameBoard[1][1] + gameBoard[2][0]

  if (row0 == (player* 3)):
    return False
  elif(row1 == (player* 3)):
    return False
  elif(row2 == (player*3)):
    return False
  elif (column0 == (player* 3)):
    return False
  elif(column1 == (player* 3)):
    return False
  elif(column2 == (player*3)):
    return False
  elif(diagnol0 == (player*3)):
    return False
  elif(diagnol1 == (player*3)):
    return False
  else:
    return True

while(keepGoing):
  keepGoing = switchPlayer(checkWins(game()))
  if keepGoing == False:
    for i,j in enumerate(tiktactoeBoard):
      print (*j)

    print("Good Game " + player + "!")