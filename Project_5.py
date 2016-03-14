# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

crit = False

def test_num(number):
	counter = 2
	while counter <= 20:
		if number % counter == 0:
			pass
		else:
			return False
		counter = counter + 1
	return True

counter = 1

while not crit:
	if test_num(counter):
		print counter
		crit = True
	else:
		counter = counter + 1


print "done"
