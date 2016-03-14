# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_num_pali(testnumber):
	workingwith = str(testnumber)
	if workingwith == workingwith[::-1]:
		return True
	else:
		return False

crit = True
num1 = 100
num2 = 100
list_of_palis = []
while num2 < 1000:
	num1 = 100
	while num1 < 1000:
		testnum = num1 * num2
		if is_num_pali(testnum):
			list_of_palis.append(testnum)
		num1 = num1 + 1

	num2 = num2 + 1


print("done")
print max(list_of_palis)
