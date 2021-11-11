#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

choice = input('What is your choice? Head or Tail ')

number = random.randint(0, 1)

if number == 1:
  print ('You have got Head!')
else:
  print ('You got a Tail!')
