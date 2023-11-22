#NAME: Jack Lester
#PD: 8

from random import randint
car = randint(1,3)

guess = input("Which door would you want to pick? 1, 2, or 3: ")

while guess != 1 and guess != 2 and guess != 3 and not guess.isnumeric():
  guess = input("Which door would you want to pick? 1, 2, or 3: ")
  
guess = int(guess)
if(guess == 1 and car == 3):
  print("The goat is behind door 2") #
elif(guess == 2 and car == 1):
  print("The goat is behind door 3") #
elif(guess == 3 and car == 2):
  print("The goat is behind door 1") #

elif(guess == 1 and car == 2):
  print("The goat is behind door 3") 
elif(guess == 2 and car == 3):
  print("The goat is behind door 1") ##
elif(guess == 3 and car == 1):
  print("The goat is behind door 2")

elif(guess == 1 and car == 1):
  print("The goat is behind door 3") #
elif(guess == 2 and car == 2):
  print("The goat is behind door 1")#
elif(guess == 3 and car == 3):
  print("The goat is behind door 2")#

decision = input("Would you like to change your pick? y/n ")
while decision not in ["y","n"]:
  decision = input("Would you like to change your pick? y/n ")
  
#your validation loop should check for y or n being
while decision == "y":
  if(guess == 1 and car == 3 or guess == 3 and car == 3 or guess == 2 and car == 3):
      guess = 3
      break
  elif(guess == 2 and car == 1 or guess == 2 and car == 2 or guess == 1 and car == 2):
      guess = 1
      break
  elif(guess == 3 and car == 2 or guess == 2 and car == 2 or guess == 3 and car == 1):
      guess = 2
      break
if guess == car:
  print("The car was behind Door #", car,".",sep='')
  print("You won!")
else:
  print("The car was behind Door #", car,".",sep='')
  print("You lost")

