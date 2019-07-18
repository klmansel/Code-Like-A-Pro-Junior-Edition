import  time 

# welcome  the player
name = input(" what is your name? ")
print("hello, " + name, "time to play hangman!")
print(" ")
#wait for one second
time.sleep(1)
print("welcome to my word game" + name + "!")
time.sleep(0.5)
#here we set the secret 
word = "secret"
#creates an vvariable with an empty 
guesses = ' '
turns = 10
while turns > 0:

  #  Make a counter that starts with zero
  failed = 0
  for char in word:
    if char in guesses:
      print(char);
    else:
      print("_"),
      failed += 1
  if failed == 0:
    print(" you won ")
    break
  print
  guess = input ("guess a character:")
  guesses += guess 
  if guess not in word:
    turns -= 1
    print("wrong")
    print("you have ", + turns, "more guesses")
    if turns == 0:
      print(" you lose") 