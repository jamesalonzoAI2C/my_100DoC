# Number Guessing Game Code

## Number Guessing Game Objectives:
> - Include an ASCII art logo.
> - Allow the player to submit a guess for a number between 1 and 100.
> - Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
> - If they got the answer correct, show the actual answer to the player.
> - Track the number of turns remaining.
> - If they run out of turns, provide feedback to the player. 
> - Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

## ***My Solution***
```python
from art import logo
import random

print(logo)
number = random.randint(1,100)

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def easy_mode():
    game_on = True
    attemps = 10
    while game_on:
        print(f"You have {attemps} attempts remaining to guess the number")
        guess = int(input("Make a Guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            game_on = False
        elif guess != number:
            attemps -= 1
            if attemps == 0:
                print(f"You have {attemps} attemps remaining. The number was {number}. Game over, welcome to Hell.")
                game_on = False
            elif guess < number:
                print("Too low, guess again.")
            elif guess > number:
                print("Too high, guess again.")

def hard_mode():
    game_on = True
    attemps = 5
    while game_on:
        print(f"You have {attemps} attempts remaining to guess the number")
        guess = int(input("Make a Guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            game_on = False
        elif guess != number:
            attemps -= 1
            if attemps == 0:
                print(f"You have {attemps} attemps remaining. The number was {number}. Game over, welcome to Hell.")
                game_on = False
            elif guess < number:
                print("Too low, guess again.")
            elif guess > number:
                print("Too high, guess again.")


if difficulty == "easy":
    easy_mode()
else:
    hard_mode()
```
## ***Angela's Solution***
```python
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
```
## Differences

- I like how Angela imported 'randint' from random. It allowed for the variable answer to just be set as answer = randint(1, 100) instead of calling random.randint(1,100). I did not know that was possible. 
- Angela set GLOBAL_VARIABLES for the amount of turns. I tried setting global variables but could not figure it out.
- she set numerous functions and then called the functions with in the game. I took a longer apporach and made an entire easy game and a hard game. It was simple for me becuase i only needed to create one game and just set the number of turns differently for the other. 
- i like how she manipulated the code for the set_diffculty vairbale and the way turns was updated.
- to exit the game function, Angela simnply "RETURN" when the turns was 0. I created a flag. She's too good.