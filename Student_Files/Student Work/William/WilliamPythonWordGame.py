import time

#welcome the UserWarning
name = input ("what is your name? ")

print("welcome to my word game " + name + "!")

#wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

#set the secret word
word = "superstar"

#Create variable with an empty Value
guesses = ''

# Determine the number of turns
turns = 15

#Create a while loop
while turns > 0:
    #make a counter that starts  with zero
    failed = 0

    #for every character in secret word
    for char in word: 
      if char in guesses: 
        print(char) 
      else :
        print("_")
        #and increase the failed counter by 1
        failed += 1
    # if failed is equal to zero

   #tell the player they won
    if failed == 0: 
      print ("You Won !")

    #exit the script
      break

    print

    #ask the user to guess a letter 
    guess = input("Guess a letter: ")

    #Set the player's guess to guesses
    guesses += guess
       
   # if the guess is not found in the secret word
    if guess not in word:
      #turns counter decreases by 1
      turns -= 1
      print("Nope, that's wrong")
      #print number of turns
      print (turns)
      if turns == 0: 
        print ("You lose!")
