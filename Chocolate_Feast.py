if __name__ == '__main__':
	
	n = 6
	c = 2
	m = 2

	w = n // c
	ch = w
	ch_eated = ch

	while (ch > 0):
		print("w: %d. ch: %d. ch_eated: %d" %(w, ch, ch_eated))
		while (w >= m):
			ch = w // m
			print("ch: %d" %ch)
			w = ch + (w % m)
			print("w: %d" %w)
			ch_eated += ch
			print("ch_eated: %d" %ch_eated) 
		ch = 0
	print("Chocolate Eated: %d" %ch_eated) 

