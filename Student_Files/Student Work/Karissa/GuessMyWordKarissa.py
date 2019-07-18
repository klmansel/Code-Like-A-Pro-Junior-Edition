import time

# Welcome the player
name = input("What is your name?")

print("Wlcome to my game " + name + "!" )

# wait for 1 second
time.sleep(1)

print("start Guessing...")
time.sleep(0.5)

# set the secret word
word = "cheerleader"

# create a variable with an empty Value
guesses = ""

# determine the number of turns
turns = 20

#create a game while Loop
while turns > 0:
    # make a counter that starts with Zero
    failed = 0

    # for every character in the secret word 
    for char in word:
      if char in guesses:
        print(char)
    else:
      print("_")
      # and increase the failed counter by 1 
      failed += 1
  # if failed is equal to  Zero

  # tell the player they won
    if failed == 0:
      print("you won")
  
  # exit the script
      break 

    print

   # ask the user to guess a letter
    guess = input("Guess a letter: ")

   # set the players guess to guesses
    guesses += guess

   # if that guess is not found in the secret word 
    if guess not in word:
     #turns counter decreases by 1
     turns -= 1 
     print("Nope, thats wrong")
     # print number of turns left
     print("You have" + turns, "more guesses!")
     if turns == 0:
       print (" You lose!")


