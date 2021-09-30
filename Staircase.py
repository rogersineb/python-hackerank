import math
import os
import random
import re
import sys

if __name__ == '__main__':

	tam_staircase = int(sys.argv[1])
	stair = "#"

	for line in range(tam_staircase):
		if(line < tam_staircase):
			temp = stair * (line+1)
			print(temp.rjust(tam_staircase))
		else:
			print("#"*line)



