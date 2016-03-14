# The sequence of triangle numbers is generated by adding the natural numbers.
# What is the value of the first triangle number to have over five hundred divisors?
# 
# 

def gen_triangle(x):
	answer = x * ((x+1.0) / 2)
	return int(answer)

def num_div(x):
	if x <= 1:
		return 1
	else:
		square = int(x ** 0.5) + 1
		num_of_div = 0
		for item in range(1, square + 1):
			if ((x / float(item)) % 1 == 0):
				num_of_div = num_of_div + 1
		return num_of_div * 2


print gen_triangle(7)
print num_div(9)

crit = True
seed = 1
tri = 0
divnum = 0
while crit:
	tri = gen_triangle(seed)
	divnum = num_div(tri)
	print seed, tri, divnum
	if divnum >= 500:
		crit = False
	else:
		seed = seed + 1


