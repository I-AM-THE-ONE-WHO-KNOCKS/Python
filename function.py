#this program shows how to use function in python

def add(one, two):
	result = one + two
	print("addition of", one, "and", two, "is:", result)

#if we do not know how many arguments we have we can use the following function
def print_any(*argv):
	print(argv)

#function with return value
def mul(one, two):
	return one * two

print_any("hello", "there", 10)

add(2, 3)

m = mul(5, 4)
print(m)

print(f"5 * 4 is = {mul(5, 4)}")