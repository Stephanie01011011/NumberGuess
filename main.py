
#welcome
#thinking of a number
#difficulty level
#let player know attempts count
#player guess
#Too high or too low, correct, or no more guesses left
import random
from replit import clear

def get_number():
  num_choice = random.randint(1, 100)
  return num_choice

def check_guess(guess, number_choice):
  if guess == number_choice:
    print(f"You got it! The random number was {number_choice}")
    return "winner"
  elif guess < number_choice:
    print("Too low.")
  elif guess > number_choice:
    print("Too high")

def set_difficulty():
  #Get difficulty level and set attempts
  difficulty = input("Would you like to try 'easy' version or 'hard':\n")
  if difficulty == 'easy':
    return 10
  else:
    return 5

def game():
  #set attempts
  attempts = 0
  number_choice = get_number()
  print(number_choice)
  #welcome
  print("I'm thinking of a number between 1-100.")
  #set attempt amount with difficulty selection
  attempts = set_difficulty()

  while attempts > 0:
    
    print(f"You have {attempts} guesses.")
    
    guess = int(input("Make your guess: \n"))
      
    check = check_guess(guess, number_choice)

    #check if the player won yet
    if check == 'winner':
      attempts = 0
    #if the player hasn't won, take away an attempt
    attempts -= 1
  #if player has no attempts and they didn't guess correctly, they lose
  if attempts < 1 and check != 'winner':
    print("You have lost. You have no more guesses left")


while input("Do you want to play the number guessing game: \n") == 'yes':
  clear()
  game()

print("Thanks for playing!")
