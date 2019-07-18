import time

# Welcome the player
name = input ("What is your name?")

print("Welcome to my word game " + name + "!")

# wait for one second
time.sleep(1)

print("Start Guessing...")
time.sleep(0.5)

#set the secret word
word = "swimmer"

# Create a variable with an empty Value 
guesses = ''

# Determine the number of turns
turns = 10

# Create a game while loop 
while turns > 0:
    # make a counter that starts with a Zero 
    failed = 0

    # for every character in the secret word
    for char in word: 
      if char in guesses:
        print(char);
      else:
          print("_"),
          # and increase the failed counter by 1
          failed += 1
      # if failed is equal to Zero
  
      # tell the player they won
    if failed == 0:
      print("you won!")

      # exit the script
      break

    print

      # Ask the player to guess a letter
    guess = input("Guess a letter: ")

     # Set the player's guess to guesses
    guesses += guess

      # if the guess is not found in the secret word
    if guess not in word: 
        # turns counter decreases by 1
      turns -= 1
      print(" Nope, that's incorrect")
        # print number of turns
    # print(" You have " + turns + "more guesses!")
    if turns == 0:
      print("You Lost!")