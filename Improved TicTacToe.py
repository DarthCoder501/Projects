#sets the starting scores for each player#

player1score = 0
player2score = 0 
playnumber = 1
tienumber = 0

def tictactoe():
  boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  mathgrid = [4,9,2,3,5,7,8,1,6]
  
#creates the grid and labels the boxes for tictactoe#
  
  def createboxes():
    print()
    print('', boxes[0], "|", boxes[1], "|", boxes[2])
    print("___|___|___")
    print('', boxes[3],  "|", boxes[4],  "|", boxes[5])
    print("___|___|___")
    print('', boxes[6],  "|", boxes[7],  "|", boxes[8])
    print()

#ensures that whatever the user inputs is a number that is on the board/within the range and lets the user try again if it's not#

  def obtainnumber(): 
    while True: 
      number = input()
      try: 
        number = int(number)
        if number in range(1,10): 
          return number
        else: 
          print("That number is not on the grid, please try again.")
      except ValueError: 
        print("That is not a number, please try again.")
        continue 

#A function to list the total games played, how many times each player has won, and how many times they tied#

  def gamescore():
    print("Total games played:", playnumber, "\n player 1 has won:", player1score, "games", "\n player 2 has won", player2score, "games", "\n You have tied:", tienumber, "times")

#the coder checks to see if one of the two players won by adding up the numbers in the column/row to see if they add up to fifteen#
  
  def checkforwin(player): 
    global player1score
    global player2score
    global tienumber
    
    count = 0
    
    for x in range(9): 
      for y in range(9):
        for z in range(9):
          if x != y and y != z and  z!= x: 
            if boxes[x] == player and boxes[y] == player and boxes[z] == player:
              if mathgrid[x] + mathgrid[y] + mathgrid[z] == 15:
                if player == "X":
                  player1score += 1
                elif player == "O":
                  player2score += 1
                print("Player", player, " wins!")
                gamescore()
                return True 

#checks to see if the game ended in a tie by counting the checking to see if the total number of boxes used up is equal to 9 and one of the players has used up more boxes than the other#
    
    for a in range(9): 
      if boxes[a] == "X" or boxes[a] == "O":
        count += 1
      if count == 9:
        print("Tie!")
        tienumber += 1
        gamescore()
        return True

#replaces the number on the grid with either a X or O and if the box has already been used up it will print a statement to state so.#  
  
  def Turn(player): 
    positioning = obtainnumber() - 1
    if boxes[positioning] == "X" or boxes[positioning] == "O":
      print("That box has been used, please try again!")
      Turn(player)
    else: 
      boxes[positioning] = player 
      
#checks to see if any player has won yet if not then it allows the next player to go" 

  finish = False
  
  while not finish:
    createboxes()
    finish = checkforwin("O")
    if finish == True:
      break 
    print("Choose a box Player 1")
    Turn("X")

    createboxes()
    finish = checkforwin("X")
    if finish == True:
      break 
    print("Choose a box Player 2")
    Turn("O")

#prints the score and allows the users to play another game of tictactoe if the input is equal to yes#  
  
  if input("Do you want to play again? (yes/no): ") == "yes":
    global playnumber
    playnumber += 1
    print()
    tictactoe()

tictactoe()
