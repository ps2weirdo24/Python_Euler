# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def test_prime(x):
	square = int(x ** 0.5) + 1
	if x < 2:
		return False
	elif x == 2:
		return True
	else:
		for item in range(2, square):
			if x % item == 0:
				return False
			elif x % item != 0:
				pass
		return True

def sum_prime(start_num):
	beg_list = range(start_num)
	total = 0
	for item in beg_list:
		if test_prime(item):
			total = total + item
		else:
			pass
	return total

print sum_prime(2000000)