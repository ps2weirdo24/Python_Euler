# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

def find_answer(x,y):
	num1 = x * y
	answer = 1
	for item in range(1, num1):
		answer = answer * item
	return answer

print find_answer(19,19)