# Apple tree is to the left of the house
# Orange tree is to the right of the house
# A negative value of d means the fruit fell d units to the tree's left, and a positive value of d, means it falls to the tree's right

if __name__ == '__main__':

	s_house = 7
	t_house = 10
	a_apple_tree = 4
	b_orange_tree = 12
	apples = [2, 3, -4]
	oranges = [3,-2, -4]
	apple_in_house = 0
	orange_in_house = 0

	apple_d_min = s_house - a_apple_tree
	apple_d_max = t_house - a_apple_tree
	orange_d_min = s_house - b_orange_tree
	orange_d_max = t_house - b_orange_tree
	
	for apple in apples:
		if apple >= apple_d_min and apple <= apple_d_max:
			apple_in_house += 1

	for orange in oranges:
		if orange <= orange_d_max and orange >= orange_d_min:
			orange_in_house += 1

	print(apple_in_house, orange_in_house)		







