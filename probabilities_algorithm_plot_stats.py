#This is a probabilities algorithm. 
#Let's see how to use it.
#Rules:
#You set your total amount you want to play and a starting amount you want to begin with.
#Program returns how many tries you have, as well as your winnining percentage.
#You have to play on at least equitable events. For our example, choose events from 1.85 and above. Every time you loose, multiply your starting amount with 2.20 
#Finally, you could perform a demonstration with your numbers to find out if it works.

#imports
import time
from random import randint
import math
import matplotlib.pyplot as plt

#starting question, if you want you like to play or not
while True:
	question = input("Do you like probabilities games(Y/N)?")
	if (question == 'y' or question == 'Y' or question == 'YES' or question == 'yes' or question == 'N' or question == 'n' or question == 'NO' or question == 'no'):
		break

#if yes, algorithm starts
if (question == 'y' or question == 'Y' or question == 'YES' or question == 'yes'):
	
	#print starting messages:
	print ("")
	print ("Then, welcome to our game.")
	print ("-------------------------------------------------------------------")
	print ("Rules:")
	print ("Set total budget and starting amount.")
	print ("Algorithm will give your tries and percentage")
	print ("You have to play on equitable events (eg 1.85).")
	print ("When you lose, just multiply your bet by 2.20.")
	print ("-------------------------------------------------------------------")
	
	#user inputs
	print ("")
	total = input ("Your budget?")
	start = input ("Your starting amount?")
	print ("")
	
	#convert input to float
	start = float(start)
	total = float(total)

	#initialize variables
	odd = 1.85
	multiplier = 2.20
	add_every_win = odd*start - start
	no_of_games = 0
	
	#Find number of tries, depending on the variables above
	tries = 0
	current_total = start 
	temp_total = start
	while (total > current_total):
		temp_total = temp_total * multiplier
		current_total = current_total + temp_total
		tries += 1
		
	#calculate winning percentage and round 2 decimal number
	percentage = 100 - (1/(2**tries))*100
	percentage = round(percentage, 2)
	
	#print total budget
	if (total > 1):
		print ("Total budget is",total,"euros.")
	else:
		print ("Total budget is",total,"euro.")
	
	#print starting bet
	if (start <= 1):
		print ("Starting amount is",start,"euro.")
	else:
		print ("Starting amount is",start,"euro.")
	
	#print initial screen messages
	print ("Algorithm finds that you have",tries,"tries.")
	print ("So, your winning percentage is", percentage,"%.")
	key = input("Press enter to start with game 1...")
	
	#initialize two lists, in order to use them to design a graph
	game_list = [no_of_games]
	budget_list = [total]
	#main game, while we still have tries
	while (tries > 0):
		print("")
		no_of_games += 1
		print ("Game",no_of_games,"starts.")
		print ("Loading...")
		
		#insert no_of_games to game_list
		game_list.append(no_of_games)
		
		time.sleep(2)
		#get a random result, 1 means winning, 0 means losing
		result = randint(0,1)
		
		#win part
		if (result == 1): 
			print ("Win! :) ")
			total = total + add_every_win
			total = round (total,2)
			
			#insert budget to budget_list in case of winning
			budget_list.append(total)
			
			print (total)
			#Find number of tries again, depending on the variables above
			#If we win a game, we have to calculate again our tries, as our total has increased and we may "win" another try
			tries = 0
			current_total = start 
			temp_total = start
			while (total > current_total):
				temp_total = temp_total * multiplier
				current_total = current_total + temp_total
				tries += 1
			
			plt.plot(game_list,budget_list)
			plt.show()
			print ("You have",tries,"tries.")
			key = input("Press any key to continue with next game...")
			print ("")
		
		#lose part
		else:            
			print ("Lose :( ")
			#insert budget to budget_list in case of losing
			budget_list.append(total)
			tries -= 1
			if (tries > 1):
				print ("You have",tries,"tries.")
			else:
				print ("You have",tries,"try")
			if (tries > 0):
				key = input("Press enter to continue with next game...")
				print ("")
	
	#no other tries, print goodbay message and ask user for input
	print ("")
	print("Unfortunately, you don't have other try. Game over.")
	key = input("Press enter to exit game and see your stats...")
	plt.plot(game_list,budget_list)
	plt.show()

#user chose no, so game will not start at all
else:
	print ("")
	print("Understood. This game has nothing to offer you!")
	key = input("Press enter to exit...")