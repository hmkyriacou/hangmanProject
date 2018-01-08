
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


#    ****MAIN***

input1 = "HELLO"
endGame = False
while endGame ==False:
    prev = dashMaker(input1, word,prev)
    print(dashMaker(input1, word,prev))
