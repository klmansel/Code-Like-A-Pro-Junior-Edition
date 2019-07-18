import time

#Welcome the player
name = input("What is the name I should put on your gravestone?")

print("Welcome to my word (cough life or death cough )game " + name + "!")

#wait for one second
time.sleep(1)

print("Start guessing...hehe...")
time.sleep(0.5)

#set the secret word
word = "Deadly"

#create a varible with an empty value
guesses = ''

#num of turns
turns = 12

#game loop
while turns > 0:
    #make a counter that starts with zero
    failed = 0

    #for every character in the secret word
    for char in word:
      if char in guesses:
        print(char)
      else:
        print("_")
        #fail +1
        failed += 1
    #if failed is equal to zero 

    #tell the player they won
    if failed == 0:

      print("You lived!")

      #exit script
      break

    print

    #ask user to guess letter
    guess = input("Guess a letter or die!")

    #set guess to guesses
    guesses += guess
    if guess not in word:
      turns -= 1
      print("One step closer to your doom!")
      print("You have " + turns + "more guesses till your doom!")
      if turns == 0:
        print("You died!")