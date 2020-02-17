#this program demonstrates how to use for loop 

List = ["aad", "bada", "cadda", "dda","ead"]

#range function
print(f"Range of 5 = {range(5)}")

#len of list is
print(f"length of our list is {len(List)}")

#for loop with index and the len of list
for i in range(len(List)):
	print(f"Index {i}, Item {List[i]}")

#if dont want index then 
for item in List:
	print(f"Item {item}")

#we can combine above two types 
for i, item in enumerate(List):
	print(f"Index {i}, Item {item}")