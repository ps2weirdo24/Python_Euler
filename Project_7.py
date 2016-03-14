# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def test_prime(x):
	if x <= 2:
		return True
	else:
		for item in range(2,x):
			if x % item == 0:
				return False
			elif item == x-1:
				return True
			else:
				pass

print test_prime(13)
print test_prime(15)
listofprimes = []
counter = 2

while len(listofprimes) < 10001:
	if test_prime(counter):
		listofprimes.append(counter)
	else:
		pass
	counter = counter + 1

print max(listofprimes)
