global endGame
import random
#### INPUT #######################################################################

def wordCheck(word):
  wordLoop = True
  while wordLoop == True:
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
      
    elif (length > 10 or length < 3):
      print("Please input a word with 3 to 10 letters.")
      
    else:
      wordLoop = False
      
  return word
      
#Checks input 
def guessCheck(guess):
  guessLoop = True
  while guessLoop == True:
    guess = input("Guess a letter: ")
    if (len(guess) > 1) or (False==guess.isalpha()):
      print("Please only input one letter.")
    else:
      guess = guess.upper()
      guessLoop = False
  return guess

#### GUESS CHECKER #######################################################################

#Checks the string for the guess letter, changes output string
def dashMaker(word,letter,previous="---------------"):
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
            endGame = True
            
            
#### MAIN ####
print("Welcome to Hangman!")
print("By Advanced Computer Science period 9")
print("To play with a friend begin by entering 'input' followed by the word when prompted")
print("To play singleplayer enter 'random' and begin playing!")
print ("________      ")
print ("|      |      ")
print ("|             ")
print ("|             ")
print ("|             ")
print ("|             ")

    #### INPUT ####
  

randLoop = True
while randLoop == True:
  begin = input("Would you like your word to be input or random?")
  begin = begin.upper()
  word = " "

  if (begin == "RANDOM"):
    #Gets the number of words in Word.txt
    infile = open("randomList.txt", "r")
    c = 0
    line = infile.readline()
    while line:
      c += 1
      line = infile.readline()
    infile.close() 
  
    #Gets a random word from Word.txt 
    wordn = random.randint(1, c)
    infile1 = open("randomList.txt", "r")
    for x in range(wordn):
      word = infile1.readline()
    word = word.replace("\n", "")
    infile1.close()
    word = word.upper()
    randLoop = False
    
  elif (begin == "INPUT"):
    word = wordCheck(word)
    randLoop = False
    


#### GUESS CHECKER ####
guess = " "
c = 0
endGame = False
prev = dashMaker(word, guess)
print(prev)
while (endGame == False):
    guess = " "
    guess = guessCheck(guess)
    x = dashMaker(word, guess ,prev)
    
    if (prev == x):
      c = c + 1
      print (x)
      prev = x
      
    elif (x == word):
      endGame = True
      print ("You win!")
    else:
      print (x)
      prev = x
      
#### GRAPHICS ####
    hangmanGraphics(c)
    if c == 10:
      endGame = True
      
print("The word was: "+ word)
