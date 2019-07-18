import time

# Welcome the player
name = input("What is your name ")
print("Welcome to my word game! " + name + "!")
# Wait for 1 second
time.sleep(1)

print("Want to play a guessing game?")
time.sleep(1)

print("Start Guessing...")
time.sleep(0.5)


# Set the secret word
word = "funny"

# Create a variable with an empty Value 
guesses = '10'

# Determine the number of turns
turns = 10

# Create a Game while loop
while turns > 0:
  # Make a counter that starts with zero 
  failed = 0

  #for every character in secret word
  for char in word:
    if char in guesses:
      print(char)
  else:
    print("_")
    # and increase the failed counter by 1
    failed += 1
  # if failed is equal to zero

  #tell the player they wom
  if failed == 0:
    print ("youwon!")

    # exit the script
    break

print

# Ask the user to guess a letter
guess = input("guess a letter: ")
# Set the player's guess to guesses
guesses += guess

# if the guess is not not found in the secret word
if guess not in word:
   # turms counter decreases by 1
   turns -= 1
  print("Wrong")
  #print number of turns 
  print("You have " + turns + "More guesses!")
  if turns == 0:
    print("You've lost")




