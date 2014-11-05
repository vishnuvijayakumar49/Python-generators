def num_from(i):
	while 1:
		yield i
		i = i + 1

def exclude_multiples(n, ints):
	for i in ints:
		if (i % n):
			yield i


def firstn(g,n):
	for i in range(n):
		yield g.next()

print list(firstn(exclude_multiples(2,intsfrom(1)),5))

