#Since 1927, "The Cyclone" roller coaster has delighted visitors at Coney Island (Brooklyn, NY). 🎢
#They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) 
#It's a program that ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

height = int(input('What is your height (cm) ?'))
credits = int(input('How many credits do you have ?'))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif credits >= 10 and height < 137:
  print("You are not tall enough to ride")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("You have not met either requirement")
