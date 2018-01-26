print ("________      ")
print ("|      |      ")
print ("|             ")
print ("|             ")
print ("|             ")
print ("|             ")


def wordCheck(word):
  word = input("Enter your word: ")
  word = word.upper()
  
  length = len(word)
  if (len(word)> 10 or len(word) < 3):
    print("Please input a word with 3 to 10 letters.")
    wordCheck(word)
  else:
    return(word)
    
def guessCheck(guess):
  guess = input("Guess a letter: ")
  if (len(guess) > 1):
    print("Please only input one letter.")
    guess = input("Guess a letter: ")
    guessCheck(guess)
  else:
    return guess
  
begin = input("Would you like your word to be input or random? ")
begin = begin.upper()
word = " "


if (begin == "RANDOM"):
  #Gets the number of words in Word.txt
  infile = open("Word.txt", "r")
  c = 0
  line = infile.readline()
  while line:
    c += 1
    line = infile.readline()
  infile.close() 

  #Gets a random word from Word.txt 
  import random
  wordn = random.randint(1, c)
  infile1 = open("Word.txt", "r")
  for x in range(wordn):
    word = infile1.readline()
  word = word.replace("\n", "")
  infile1.close()
  word = word.upper()
  

  
elif (begin == "INPUT"):
  wordCheck(word)


guess = ""
guessCheck(guess)
print("Guess: " + guess)





def hangmanGraphics(guesses):
        if (guesses == 0):
            print ("________      ")
            print ("|      |      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif (guesses == 1):
            print ("_______       ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif (guesses == 2):
            print ("________      ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|     /       ")
            print ("|             ")
            print ("|             ")
        elif (guesses == 3):
            print ("________      ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|     /|      ")
            print ("|             ")
            print ("|             ")
        elif (guesses == 4):
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|             ")
            print ("|             ")
        elif (guesses == 5):
            print ("________      ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|     /|\     ")
            print ("|     /       ")
            print ("|             ")
        elif (guesses == 6):
            print ("________      ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("|             ")
        elif (guesses == 7):
            print ("________      ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|     /|\     ")
            print ("|     / \_    ")
            print ("|             ")
        elif (guesses == 8):
            print ("________      ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|     /|\     ")
            print ("|    _/ \_    ")
            print ("|             ")
        elif (guesses == 9):
            print ("________      ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|     /|\_    ")
            print ("|    _/ \_    ")
            print ("|             ")
        else:
            print ("________      ")
            print ("|      |      ")
            print ("|      O      ")
            print ("|    _/|\_    ")
            print ("|    _/ \_    ")
            print ("|             ")
            print ("Game Over")
            

  




