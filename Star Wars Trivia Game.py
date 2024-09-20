#function to play the game 
def new_quiz_game():
  
#Beginning values for what letter choice the user guessed, how many right guesses they had, and what question they are on
  guesses = []
  right_guesses = 0
  question_number = 1

  for q in questions:
    print("-----------------------------------------------")
    print(q)
    for c in answer_choices[question_number - 1]:
      print(c)
    guess_choice = input("Choose either A, B, C, or D: ")
    guess_choice = guess_choice.upper()
    guesses.append(guess_choice)

    right_guesses += check_answer_choice(questions.get(q), guess_choice)
    question_number += 1
    
  show_score(right_guesses, guesses)
  
#Function that checks if the answer is correct and updating the score accordingly 
def check_answer_choice(answer, guess_choice):
  if answer == guess_choice:
    print("You are correctamundo!")
    return 1
  else:
    print("Womp womp, you are wrong!")
    return 0
    
#Function that displays the results by showing the correct answers, the player's guesses, and the final score in a percentage     
def show_score(right_guesses, guess_choice):
  print("-----------------------------------------------")
  print("Results")
  print("-----------------------------------------------")
  
  print("Answers: ", end="")
  for i in questions:
    print(questions.get(i), end=" ")
  print()

  print("Guesses: ", end="")
  for i in guess_choice:
    print(i, end=" ")
  print()

  final_score = int((right_guesses/len(questions))  * 100)
  print("Your final score is: " + str(final_score) + "%")
                    
#Function that allows the player to play again 
def play_again():
  player_answer = input("Do you want to play again? Yes or no?: ")
  player_answer = player_answer.upper()

  if player_answer == "YES": 
    return True 
  else: 
    return False 
    
#Dictionary of questions for the game and the correct answer choice
questions = {
  "Where did Obi-wan take Luke after his birth?": "D",
  "Who was Anakin Skywalkere's Padawan?": "C",
  "What year did the first Star Wars movie come out?": "D",
  "What is the name of Boba Fett's ship?": "D",
  "How are always how many Sith Lords?": "B",
  "What is the name of Anakin's stepbrother?": "B",
  "How many forms of communication is C-3PO flunet in?": "C",
  "What is the path to the dark side?": "A", 
  "Which hand did Luke lose in his fight with Darth Vader?": "A",
  "What name did Obi-Wan go by on Tatoonie?": "D",
  "Who voiced Darth Vader in the original trilogy?": "B"
}

#List of the answer choices for each question 
answer_choices = [["A. Hoth", "B. Naboo", "C. Alderaan", "D. Tatoonie"],
                 ["A. Jaden Korr", "B. Knox", "C. Ahsoka Tano", "D. Barriss Offee"], 
                 ["A. 1980", "B. 1979", "C. 1978", "D. 1977"], 
                 ["A. Yt-1300", "B. Executor", "C. Delta-7", "D. Slave I"], 
                 ["A. 1", "B. 2", "C. 3", "D. 4"],
                 ["A. John Lars", "B. Owen Lars", "C. John Laar", "D. Owen Laar" ], 
                 ["A. 9000", "B. 420", "C. 6,000,000", "D. 69"],
                 ["A. Fear", "B. Anger", "C. Despair", "D. Hate"], 
                 ["A. Right", "B. Left", "C. Both", "D. Trick question he didn't"],
                 ["A. John", "B. Tom", "C. Lucas", "D. Ben"], 
                 ["A. Seth MacFarlane", "B. James Earl Jones", "C. Dee Bradley Baker","D. Kevin Michael Richardson"]]

new_quiz_game()

#Starts a new game but if players declines then it prints a message 
while play_again(): 
  new_quiz_game()

print("Leaving already? Take this L on you way out, byeeeeee!")
