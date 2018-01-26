#### INPUT #######################################################################

def wordCheck(word):
  word = input("Enter your word: ")
  word = str(word)
  word = word.upper()
  z = 1
  let = " "
  
  length = len(word)
  for y in range(length):
    let = word[y]
    if (ord(let) < 65 or ord(let) > 90):
      z = 0
      
  if (z == 0):
    print("Please only enter letters")
    wordCheck(word)
  if (length > 10 or length < 3):
    print("Please input a word with 3 to 10 letters.")
    wordCheck(word)
  else:
    return word
    
def guessCheck(guess):
  guess = input("Guess a letter: ")
  if (len(guess) > 1):
    print("Please only input one letter.")
    guess = input("Guess a letter: ")
    guessCheck(guess)
  else:
    return guess

#### GUESS CHECKER #######################################################################

def guessChecker(word,letter,previous="---------------"):
  blanks = ""

  c = 0
  for letterCounter in range(len(word)):
      if word[letterCounter] == letter and previous[letterCounter] == "-" :
          blanks += letter
      elif previous[letterCounter] == "-":
          blanks += "-"
      else:
          blanks += previous[letterCounter]

  return blanks

#### GRAPHICS ############################################################################

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
            print ("|      0      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif (guesses == 2):
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /       ")
            print ("|             ")
            print ("|             ")
        elif (guesses == 3):
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
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
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     /       ")
            print ("|             ")
        elif (guesses == 6):
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("|             ")
        elif (guesses == 7):
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     / \_    ")
            print ("|             ")
        elif (guesses == 8):
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|    _/ \_    ")
            print ("|             ")
        elif (guesses == 9):
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\_    ")
            print ("|    _/ \_    ")
            print ("|             ")
        else:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|    _/|\_    ")
            print ("|    _/ \_    ")
            print ("|             ")
            print ("Game Over")
            
            
#### MAIN ####

print ("________      ")
print ("|      |      ")
print ("|             ")
print ("|             ")
print ("|             ")
print ("|             ")

    #### INPUT ####
  
begin = input("Would you like your word to be input or random?")
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
  word = wordCheck(word)
  
guess = " "
guessCheck(guess)

    #### GUESS CHECKER ####
  
    #### GRAPHICS ####
