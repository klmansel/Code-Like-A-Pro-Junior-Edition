#Type python GuessTheWord.py
#importing the time module
import time

#welcoming the user
name = input("Name OR Death? ")

print("Hola, " + name, "Time for your trial!")

print(" ")

#wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

#here we set the secret
word = "eclipse"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 8

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print(char);   

        else:
    
        # if not found, print a dash
            print("_"),     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print("To Heaven Good👼") 

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print("Your death is soon")    
 
    # how many turns are left
        print("You have", + turns, 'more souls')
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print("YOU are in HELL now👿")  