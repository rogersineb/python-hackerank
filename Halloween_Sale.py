import math
import os
import random
import re
import sys

if __name__ == '__main__':

	price = 20
	discount = 3
	minimun = 6
	sale = 21
	qnt_games = 0

	while(sale >= price):
		
		print("Sale: %d. Qnt: %d. Price: %d" %(sale,qnt_games, price))
		sale -= price
		qnt_games += 1
		
		if( (price - discount) >= minimun):
			price -= discount
		else:
			price = minimun

	print("Sale: %d. Qnt: %d. Price: %d" %(sale,qnt_games, price))

