import math
import os
import random
import re
import sys

if __name__ == '__main__':
	
	#candles = [3, 2, 1, 3]
	#candles = [3, 3, 3, 3]
	candles = [3, 4, 3, 4]

	tallest = candles[0]
	qnt_tallest_candle = 1

	for index in range(len(candles) - 1):
	
		if(tallest < candles[index + 1]):
			tallest = candles[index + 1]
			qnt_tallest_candle = 1
	
		elif(tallest == candles[index + 1]):
			qnt_tallest_candle += 1
	
	print("tallest: %d. qnt: %d" %(tallest, qnt_tallest_candle))		