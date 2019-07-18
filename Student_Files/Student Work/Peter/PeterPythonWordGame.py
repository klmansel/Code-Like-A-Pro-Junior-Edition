import time

# Welcome the user
name = input("what is your name ")
print("Welcome to my word game " + name + "!")

time.sleep(1)

print("Start Guessing...")

time.sleep(0.5)

#Set the secret word
word = "onomatopoeia"

# Create a variable with an empty Value
guesses = ''

# Determine the number of turns
turns = 12

#Create a Game Loop
while turns > 0:
    #Make a counter that starts with Zero
    failed = 0

    #Fore every character in the word
    for char in word:
      if char in guesses:
        print(char)
      else:
          print("_")
          # and increase the failed counter by 1
          failed += 1

    if failed == 0:
           print("You won")

           break

    print

      #Ask the user to guess a letter
    guess = input("Guess a letter ")
  #Set the player's guess to guesses
    guesses += guess
    #if the guess into not found in the secret word
    if guess not in word:
  #turns counter decreases by one
      turns -= 1
      print("Sorry, that letter isn't in the word")
      #print("You have " + turns + " more guesses")
      if turns == 0:
       print("Sorry sucker you lost and have DIED!!!")