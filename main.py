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
