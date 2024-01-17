#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, answer, TURNS):

  if guess > answer:
    print("Too High")
    if guess > 100:
      print("please guess the number between 1 to 100")
      return True
    print()
    return TURNS - 1
  elif guess < answer:
    print("Too Low")
    if guess < 0:
      print("please guess number between 1 to 100")
      return True
    print()
    return TURNS - 1
  else:
    print("you guessed correctly. You Won.")


def choose_difficulty():
  level = input("choose difficulty type easy or hard: ")
  print()
  if level == "easy":
    return EASY_TURNS
  else:
    return HARD_TURNS

def game():
  print(logo)  
  print("welcome to number guessing game!")
  print("i am thinking of a number between 1 to 100.")
  answer = randint(1,100)
  TURNS = choose_difficulty()
  guess = 0
  
  while guess != answer:
    print(f"You have {TURNS} attempts remaining to guess the number.")
  
    #Let the user guess a number.
    guess = int(input("Make a guess: "))
    
    #Track the number of turns and reduce by 1 if they get it wrong.
    TURNS = check_answer(guess, answer, TURNS)
    if TURNS == 0:
      print(f"You've run out of guesses, you lose. the answer is {answer}")
      return
    elif guess != answer:
      print("Guess again.")
  


game()


# Output:

  _  _            _                ___                _              ___                
 | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
 | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
 |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
                                                            |___/                       

welcome to number guessing game!
i am thinking of a number between 1 to 100.
choose difficulty type easy or hard: easy

You have 10 attempts remaining to guess the number.
Make a guess: 89
Too High

Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 50
Too High

Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 30
Too High

Guess again.
You have 7 attempts remaining to guess the number.
Make a guess: 20
you guessed correctly. You Won.
