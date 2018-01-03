def dashMaker(word,letter):
  blanks = ""
  c = 0
  for blankMaker in range(len(word)):
      for letterCounter in range(len(word)):
          wordPs = input1.find(letter)
          if wordPs == c:
              blanks+= letter
          else:
              blanks += "-"

      c+=1

  return blanks

def letterChanger(input1, letter):
    wordPs = input1.find(letter)
    rWordPs = input1.rfind(letter)
    wordPsOut = str(wordPs) + str(rWordPs)
    while (wordPs != rWordPs):
        c = wordPs + 1
        wordPs = input1.find(letter, c)
    return wordPsOut


#    ****MAIN***
input1 = "HELOLLO"
print(letterChanger(input1, "L"))
#print(dashMaker(input1,"L",letterChanger(input1, "L")))
