# ***MAIN***
#asks the user if they want to chose their own word or get a random one
choice = input("Enter \"CHOICE\" if you want to pick the word or enter \"RANDOM\" if you want the program to pick it for you: ")
choice = choice.upper()
check = True

#Gets the word from Word.txt or user
if (choice == "CHOICE"):
  #asks the user for a word and finds how long it is
  word = input("Enter your word: ")
  word = word.lower()
  digits = len(word)
  if (digits > 10 or digits < 3):
    print("Please enter a word that has fewer than 10 letters and greater than 3.")
    check = False
  else:
    check = True
elif (choice == "RANDOM"):
  #Gets the number of words in Word.txt
  infile = open("Word.txt", "r")
  c = 0
  line = infile.readline()
  while line:
    c += 1
    line = infile.readline()
  infile.close() 

  #Gets a random word from Word.txt and finds how long the word is
  import random
  wordn = random.randint(1, c)
  infile1 = open("Word.txt", "r")
  for x in range(wordn):
    word = infile1.readline()
  word = word.replace("\n", "")
  infile1.close()
  digits = len(word)

#Checks if the program should run with the given word (applies to user input only)
if (check == False):
  print("")
elif (check == True):
  #prints the first picture and how many spaces are in the word
  wordspaces = ""
  print("_______________\nl             l\nl\nl\nl\nl\nl\nl______________\n")
  for x in range(digits):
    wordspaces = wordspaces + "_ "
  print("\t" + wordspaces + "\n")
  print("The word is " + str(digits) + " characters long.")

'''
  #Asks the user if they want to use a letter or solve the puzzel and runs the program
  choice2 = input("Would you like to guess a letter \"LETTER\" or solve the puzzel \"PUZZEL\"?")
  choice2 = choice2.upper
  if (choice2 == "LETTER"):
  elif (choice2 == "PUZZEL"):
    #asks the user for their guess and sees if it is correct (if not automatic loss)
    wordguess = input("Enter your guess: ")
    if (wordguess == word):
      print("Congrats! You saved hang man!")
    else:
      print("So close! Sorry you lose.")
      

'''
