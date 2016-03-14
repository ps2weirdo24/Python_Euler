# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and 
# the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.

num1 = 0
num2 = 0

for item in range(101):
	num1 = num1 + item**2

num2 = sum(range(101)) ** 2
print num1
print num2
print num2 - num1