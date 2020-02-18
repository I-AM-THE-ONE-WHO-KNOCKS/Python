#this program demonstrate how to create a class in python

class Coordinate():
	#built in __init__ method is called to create an instance of this class
	#self points to this perticular instance

	def __init__(self, x, y):
		self.x = x
		self.y = y

	#we can define our methods as
	def distance(self, other):
		x_diff_sq = (self.x - other.x) ** 2
		y_diff_sq = (self.y - other.y) ** 2
		return (x_diff_sq + y_diff_sq) ** 0.5

	# __str__ is an inbuilt function used when print is callles on the class
	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	#other things which can also be overloaded are
	#__add__, __sub__, __eq__, __lt__, __len__, ...

#create instances of the class
c1 = Coordinate(3, 4)
org = Coordinate(0, 0)

#print out the coordinates
print(f"coordinate of c1: x = {c1.x}, y = {c1.y}")
print(f"coordinate of origin: x = {org.x}, y = {org.y}")

#print the distances using explicit and implicit parameters
print(f"Distance with explicit parameters {Coordinate.distance(c1, org)}")
print(f"Distance with implicit parameters {c1.distance(org)}")

#print c1
print(c1)