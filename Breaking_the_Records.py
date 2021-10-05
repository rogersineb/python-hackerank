
# number of games: 1 <= n <= 1000
# Scores per game 0 <= scores[i] <= 10^8
# records_break position 0 is for breaking most points records
# records_break position 1 is for breaking least points records

if __name__ == '__main__':

	#scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
	
	scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
	
	min_score = scores[0]
	max_score = scores[0]
	
	records_breaks = [0,0]

	for score in scores:
		if score < min_score:
			min_score = score
			records_breaks[1] += 1
		elif score > max_score:
			max_score = score
			records_breaks[0] += 1

	print(records_breaks)

