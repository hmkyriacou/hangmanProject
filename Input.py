begin = input("Would you like your word to be input or random? ")
begin = begin.upper()

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
  imput random
  wordn = random.randint(1, c)
  infile1 = open("Word.txt", "r")
  for x in range(wordn):
    word = infile1.readline()
  word = word.replace("\n", "")
  infile1.close()
  
elif (begin == "INPUT"):
  word = input("Enter your word: ")
