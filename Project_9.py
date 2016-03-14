# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 


# b * (a+c-b) / (a-c) == 1000
# a = (1000 - b - c) ** 2
 

def test_square(num):
	root = (float(num) ** 0.5)
	if (root % 1 == 0):
		return True
	else:
		return False

listofsquares = []
answer = []

"""

for item in range(1000000):
	if test_square(item):
		listofsquares.append(item)
		#listofsquares.append([int(item ** 0.5), item])
	else:
		pass
"""
for a in range(1000, 0, -1):
	for b in range(1000, 0, -1):
		if test_square(a**2 + b**2) and (a<b):
			listofsquares.append([a, b, ((a**2 + b**2) ** 0.5)])
			if (a + b + ((a**2 + b**2) ** 0.5)) == 1000:
				answer.append([a, b, ((a**2 + b**2) ** 0.5)])
			else:
				pass
		else:
			pass

print listofsquares
print len(listofsquares)
print answer
