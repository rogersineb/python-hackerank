import math
import os
import random
import re
import sys


if __name__ == '__main__':
	
	matx = [
			[11, 2, 4],
			[4, 5, 6],
			[10, 8, -12]]

	sum_diagonal_a = 0
	sum_diagonal_b = 0
	for index_diagonal_a in range(len(matx)):
		for index_diagonal_b in range(len(matx)-1, -1 , -1):
			if(index_diagonal_b == index_diagonal_a):
				sum_diagonal_a += matx[index_diagonal_a][index_diagonal_b]
			if(index_diagonal_a + index_diagonal_b == len(matx)-1):		
				sum_diagonal_b += matx[index_diagonal_a][index_diagonal_b]

	print("Soma da diagonal da matrix a: %d", sum_diagonal_a)
	print("Soma da diagonal da matrix b: %d", sum_diagonal_b)
	print(abs(sum_diagonal_a - sum_diagonal_b))