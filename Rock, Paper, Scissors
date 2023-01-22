#lists the starting number of wins, ties, and games played
playerscore = 0
computerscore = 0
gametotal = 1
ties = 0

import random

# A function that prints out the various information about wins, ties, and games played
def rockpaperscissors():

  def score():
    print("Total games played:", gametotal, "\n You have won:", playerscore,
          "games", "\n the computer has won", computerscore, "games",
          "\n You have tied:", ties, "times")

#while the game is going on the user has three options to choose and the computer randomly chooses from those three options#
  while True:
    global playerscore
    global computerscore
    global ties

    player_choice = input("Choose one: rock, paper, or scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
#conditional statements for all of the possibilites of a game of rock, paper, scissors and the global keyword to keep track of the score    
#If both the player and computer choose the same option then a tie message is printed and the tie score is updated 
    if player_choice == computer_choice:
      print("It's a tie, you both chose " + player_choice + ".")
      ties += 1
      score()
#If the person chooses rock and the computer chooses scissors then a you win message is printed and the +1 is added to the player's score
    elif player_choice == "rock":
      if computer_choice == "scissors":
        print("You win!")
        playerscore += 1
        score()
#If the inverse happens then a you lose message is printed and a +1 is added to the computer's score
      else:
        print("You lose, sad trumbone sounds")
        computerscore += 1
        score()
    elif player_choice == "paper":
      if computer_choice == "rock":
        print("You win!")
        playerscore += 1
        score()
      else:
        print("You lose, sad trumbone sounds")
        computerscore += 1
        score()
    elif player_choice == "scissors":
      if computer_choice == "paper":
        print("You win!")
        playerscore += 1
        score()
      else:
        print("You lose, sad trumbone sounds")
        computerscore += 1
        score()

#allows the user to play another game or end the game, and updates the score 
    another_try = input("Do you want to play again? (yes/no): ")
    if another_try != "yes":
      break
      global gametotal
      gametotal += 1
      print()
      rockpaperscissors()

rockpaperscissors()
