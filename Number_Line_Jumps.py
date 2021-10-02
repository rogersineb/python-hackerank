# For one act, you are given two kangaroos on a number line ready to jump in the positive direction
# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump
# it's possible to get both kangarro at the same location at the same time?

if __name__ == '__main__':

	x1 = 4523
	v1 = 8092
	x2 = 9419
	v2 = 8076

	alcancou = False
 if ((x1 >= 0 and x2 > x1 and x2 <= 10000) and \
 	(v1 >= 1 and v2 >= 1 and v1 <= 10000 and v2 <= 10000)):
			if(v2 >= v1):
				print("NO")
			elif ((x2 + v2) - (x1 + v1)) % (v2 - v1) == 0: 
				print( "YES" )
			else:
				print("NO")

