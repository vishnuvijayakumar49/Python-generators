def pi_series():
	sum = 0;i = 1.0; j = 1
	while(1):
		sum = sum + j/i	
		yield 4*sum
		i = i + 2; j = j * -1
