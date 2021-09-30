import math
import os
import random
import re
import sys


'''
 # minute == 0: hour " o' clock"
 # minute > 0 and minute < 15: minute "minute past " hour
 # minute == 15: "quarter past " hour
 # minute > 15 and minute < 30: minute " minutes past " hour 
 # minute ==30: "half past " hour
 # minute == 45: "quarter to " hour
 # minute > 30: minute " minutes to " hour

 1 >= h <= 12
 0 >= m < 60

'''

if __name__ == '__main__':

	h = 1
	m = 1

	numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',11:'eleven', \
			   12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', \
			   20:'twenty', 21:'twenty one', 22:'twenty two', 23:'twenty three', 24:'twenty four', 25:'twenty five', 26:'twenty six', \
			   27:'twenty seven', 28:'twenty eight', 29:'twenty nine'}

	if(m == 0):
		print( numbers[h] + " o' clock")
	elif(m == 15):
 		print( "quarter past " + numbers[h])
	elif(m == 30):
		print( "half past " + numbers[h])
	elif(m == 45):
		print( "quarter to " + numbers[h+1])
	elif(m > 0 and m < 15):
		if(m == 1):
			print( numbers[m] + " minute past " + numbers[h])
		else:
			print( numbers[m] + " minutes past " + numbers[h])
	elif(m > 15 and m < 30):
		print( numbers[m] + " minutes past " + numbers[h])
	else:
		minutes_to = 60 - m
		if(h == 12):
			h = 0
		print( numbers[minutes_to] + " minutes to " + numbers[h+1])
	

