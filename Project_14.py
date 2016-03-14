# even n = n/2
# odd n = 3n + 1

def is_even(x):
	if (x / 2.0) % 1 == 0:
		return True
	else:
		return False


def len_chain(x):
	total = 1
	num = x
	while num != 1:
		if is_even(num):
			num = num / 2
		else:
			num = (num * 3) + 1
		total = total + 1
	return total

chain_total = [0,0]
for item in range(2, 1000000):
	thisone = len_chain(item)
	print item, thisone, chain_total
	if thisone > chain_total[1]:
		chain_total = [item, thisone]
	else:
		pass

print chain_total