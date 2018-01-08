def wordCheck(word):
  word = input("Enter your word: ")
  word = word.upper()
  z = 1
  
  length = len(word)
  while (x <= length):
    let = word.find(x)
    if (ord(let) < 65 or ord(let) > 90):
      z = 0
      
  if (z == 0):
    print("Please only enter letters")
    wordCheck(word)
  elif (length > 10 or length < 3):
    print("Please input a word with 3 to 10 letters.")
    wordCheck(word)
  else:
    return word
    
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
