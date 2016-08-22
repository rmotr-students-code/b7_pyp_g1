r = lambda x, y, z: x + y + z
print(r(1,2,3))

""""
def add(numbers):
	result = 0
	for number in numbers:
		result += number
	return result
map(lambda x: len(x), numbers)

numbers = [1, 2, 3]

def add_immutable(numbers):
	return reduce(lambda x, y: x + y, numbers, 0)
	# x   y
	# ? + 0 = 0
	# 1 + 0 = 1
	# 2 + 1 = 3
	# 3 + 3 = 6
	# ret: -- ^

p1 = ['bye', 'world']
p2 = ['hello', 'world']
"""