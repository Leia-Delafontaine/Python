#The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱
#This is a program that can respond to any Yes or No questions with a different answer each time it executes.

import random

question = input('Question: ')

random_number = random.randint(1,8 )

if random_number == 1:
  print('Yes - definitely.')
elif random_number == 2:
  print('It is decidedly so.')
elif random_number == 3:
  print('Without a doubt.')
elif random_number == 4:
  print('Reply hazy, try again.')
elif random_number == 5:
  print('Ask again later.')
elif random_number == 6:
  print('Better not tell you now.')
elif random_number == 7:
  print('My sources say no.')
elif random_number == 8:
  print('Very doubtful.')
