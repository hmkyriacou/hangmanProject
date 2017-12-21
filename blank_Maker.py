def dashMaker(word):
  blanks = ""
  for blankMaker in range(len(word)):
    blanks += "-"
  return blanks
  
  
#    ****MAIN***
x = "HELLO"
print(dashMaker(x))

