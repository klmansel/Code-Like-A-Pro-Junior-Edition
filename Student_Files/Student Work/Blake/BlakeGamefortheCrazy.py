import time

# welcome the User 
name = input("What is your name?")

print("Welcome to your end if you fail " + name + "!")

#wait 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# Set the secret word
word = "death"

# Create a variable with an empty value
guesses = ''

#turn
turns = 10

# Game loop 
while turns > 0:
    #make a counter  
    failed = 0
    #for every character in the word 
    for char in word:
      if char in guesses:
        print(char)
      else:
        print("_")
        #increase the counter by 1
        failed +=1
    #if failed is equal to zero tell he player they won
    if failed ==0:
      print("You Survived for now.")
      #exit
      break
    print
    #guess
    guess = input("guess a letter: ")
    # set guess to guesses
    guesses += guess
    #if it is incorrect
    if guess not in  word:
      #decreases by 1
      turns -= 1
      print("Nope, that is wrong")
      #say number of turns
      if turns == 0:
        print("You DIE.")