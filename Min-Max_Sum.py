import math
import os
import random
import re
import sys
if __name__ == "__main__":

	arr = [769082435, 210437958, 673982045, 375809214, 380564127]
	#arr = [1, 2, 3, 4, 5]
	#arr = [5, 5, 5, 5, 5]
	sum_max = None
	sum_min = None

	for num_a in range(len(arr)):
		
		sum_val = 0
		print("************************************\nIGNORE: %d" %arr[num_a])
		
		for num_b in range(len(arr)):
		
			if(num_b != num_a):
		
				print("sum: %d + %d" %(sum_val, arr[num_b]))
				sum_val += arr[num_b]
		
		if(sum_max == None and sum_min == None):
			sum_max, sum_min = sum_val, sum_val

		if(sum_val > sum_max):
			sum_max = sum_val
		elif(sum_val < sum_min):
			sum_min = sum_val
		
		print("Total Sum: %d" %sum_val)
		print("************************************\n")
	
	print("%d %d" %(sum_min, sum_max))