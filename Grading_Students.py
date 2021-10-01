# A grade begin in 0 and rise up to 100
# Any grade less than 40 is a falling grade

# Rules:
# if the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5
# if the value of grade is less than 38, rounding occurs as the result will still be a falling grade



if __name__ == '__main__':

	grades =[4, 73, 67, 38, 33, 84, 29, 57]
	for id_grade in range(len(grades)):
		if grades[id_grade] >= 38:
			next_multiple = grades[id_grade] + 1
			while next_multiple % 5 != 0 and next_multiple < 100:
				next_multiple += 1
			if grades[id_grade] < 100 and next_multiple - grades[id_grade] < 3:
				grades[id_grade] = next_multiple
	print(grades)
	

