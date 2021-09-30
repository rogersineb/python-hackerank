import math
import os
import random
import re
import sys

if __name__ == "__main__":
	num_positivo = 0
	num_negativo = 0
	num_0 = 0

	arr =[-4, 3, -9, 0, 4, 1]

	for item in arr:
	   if(item < 0):
	   	num_negativo += 1
	   elif(item > 0):
	   	num_positivo += 1
	   else:
	   	num_0 += 1
	
	ratio_positivo = num_positivo/len(arr)
	ratio_negativo = num_negativo/len(arr)
	ratio_neutro = num_0/len(arr)

	print("%.6f\n%.6f\n%.6f\n" %(ratio_positivo, ratio_negativo, ratio_neutro))	