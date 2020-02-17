#this program demonstrate the usage of dictionary

#storing the data in two lists is inconvenient. take 
#the case of students and their grades

students = ["anna", "bob", "kyle"]
grades = ["A", "B", "C", "D"]

#replace with a disctionary that uses key-value pairs
#lists are a subset of dictionary that uses integers as the key

my_dict = {}

my_dict["bob"] = "A"
my_dict["anna"] = "B"
my_dict["kyle"] = "D"

print(my_dict["bob"])
print(my_dict["kyle"])

#we can test if a value is in a dictionary
print("kyle" in my_dict)

#can remove an entry
del(my_dict["kyle"])

#make a new dictionary and fill it in one line
cars = {"Bill":"Audi", "Nancy":"BMW", "Chris":"VW"}

#we can get all the keys/value from the dictionary 
#this is no quranteed to be ordered!
print(cars.keys())
print(cars.values())