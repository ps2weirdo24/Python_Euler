#
#
from timeit import timeit

s = """\

def findtotal(index):
	my_total = 0
	for item in range(int(index)):
		if (item % 3 == 0) and (item % 5 == 0):
			my_total = my_total + item
		elif (item % 3 == 0):
			my_total = my_total + item
		elif (item % 5 == 0):
			my_total = my_total + item
	return my_total

print findtotal(10000)

"""

print timeit(stmt=s, number=100)

