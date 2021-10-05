# Conditions:
	# The elements of the first array are all factors of the integer being considered
	# The integer being considered is a factor of all elements of the second array

# These number are referred as being between the two arrays. Determine how many such number exist

if __name__ == '__main__':

	qnt_factors = 0
	min_interval = 0
	max_interval = 0

#	a = [2, 4]
#	b = [16, 32, 96]

	a = [2, 6]
	b = [24, 36]

	#Find the minimium interval
	a.sort()
	min_interval = a[len(a)-1]

	#Find the maximum interval
	b.sort()
	max_interval = b[0]

	a_b = []
	divise = []
	for num_a in a:
		a_b.append(num_a)
	for num_b in b:
		a_b.append(num_b)


	while min_interval < max_interval:
		count = 0
		for item in a_b:
				if min_interval % item == 0 or item % min_interval == 0:
					#print("for item:%d mod a_b:%d. count:%d" %(min_interval, item, count))
					count += 1
		if count == len(a_b):
			divise.append(min_interval)
			qnt_factors += 1
		min_interval += 1
	print("Qnt Factors: %d." %qnt_factors)
	min_interval += 1
	#print("Factors Interval: ", divise)
	
'''
	#print("num_min:%d. num_max:%d" %(min_interval, max_interval))

	#print("a_b:", a_b)
	
	#Verify if the integer is a factor of all elements in the vectors

	for item in a_b:
		count = 0
		for ab_item in a_b:
			if item >= min_interval and item < max_interval:
				#print("for item:%d mod a_b:%d. count:%d" %(item, ab_item, count))
				if item % ab_item == 0 or ab_item % item == 0:
					count += 1
		if count == len(a_b):
			qnt_factors += 1
			divise.append(item)

	#print("Factors array: ", divise)
'''