# Number Guessing Game Code

## Number Guessing Game Objectives:
> - Include an ASCII art logo.
> - Allow the player to submit a guess for a number between 1 and 100.
> - Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
> - If they got the answer correct, show the actual answer to the player.
> - Track the number of turns remaining.
> - If they run out of turns, provide feedback to the player. 
> - Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

### ***My Solution***
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
### ***Angela's Solution***
```python
```