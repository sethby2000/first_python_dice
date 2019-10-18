import random
min = 1

dice = list()

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":

    dice *= 0
    num_of_dice = int(input("How many dice to roll?"))
    
    size_of_dice = int(input("How many sides of each die?"))

    print "Rolling the dice..."
    print "The values are...."
    
    for x in range (0,num_of_dice):
    	dice.append(x)
    	dice[x] = random.randint(min,size_of_dice)
    	print dice[x]
	 
    total = 0
    total = sum(dice)
    print "The sum total of the dice is", total

    roll_again = raw_input("Roll the dice again?")	

print "BYEEEE!"