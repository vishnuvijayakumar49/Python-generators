def abc():
	a = deff()
	for i in a:
		yield i
	yield 'abc'

def deff():
	a = ijk()
	for i in a:
		yield i
	yield 'deff'

	 
def ljk():
	for i in (1,2,3):
		yield 
	yield 'ijk'


a=abc()
a.next()
