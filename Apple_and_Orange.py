# Apple tree is to the left of the house
# Orange tree is to the right of the house
# A negative value of d means the fruit fell d units to the tree's left, and a positive value of d, means it falls to the tree's right

if __name__ == '__main__':

	s_house = 7
	t_house = 11
	a_position_apple_tree = 5
	b_position_orange_tree = 15
	d_distance_falled_apple = [-2, 2, 1]
	d_distance_falled_orange = [5, -6]
	apple_in_house = 0
	orange_in_house = 0

	for index_apple in range(len(d_distance_falled_apple)):
		d_distance_falled_apple[index_apple] += a_position_apple_tree
		if d_distance_falled_apple[index_apple] >= s_house:
			apple_in_house += 1

	for index_orange in range(len(d_distance_falled_orange)):
		d_distance_falled_orange[index_orange] += b_position_orange_tree
		if d_distance_falled_orange[index_orange] <= t_house:
			orange_in_house += 1

	print(apple_in_house, orange_in_house)		







