
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


#    ****MAIN***

input1 = "HELLO"

prev = dashMaker(input1, "H",prev)
print(dashMaker(input1, "L",prev))
#print(dashMaker(input1,"L",letterChanger(input1, "L")))
