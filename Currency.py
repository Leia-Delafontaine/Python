# We just got home from a (fictionnal) trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in Colombian pesos, Peruvian soles and Brazilian reais. 
# It's a program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in EUR.

co = int(input('What do you have left in pesos ?')) 
pe = int(input('What do you have left in soles ?'))
br = int(input('What do you have left in reais ?'))

total = (co * 0.00021) + (pe * 0.24) + (br * 0.16)

print(total)
