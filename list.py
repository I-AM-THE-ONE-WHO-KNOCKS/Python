#this program demonstrate usage of list in python 

#list variable
List = []

#add elements 
List.append("Umesh")
List.append(10)
List.append(True)

print(f"content of list {List}")

#length of list
print(f"size of list {len(List)}")

#access individual elements of list
print(List[0])
print(List[1])
print(List[2])

#clear the list
List.clear()
print(f"size of list after clear is {len(List)}")

#new list
List = [2, 4, 1, 0, 23]

#sort the list
List.sort()
print(f"content of list after sorting {List}")


#reverse
print(f"content of list after reverse {List.reverse()}")

#insert at specific postion
List.insert(1, 10)
List.insert(3, 10)
print(f"content of list after insert {List}")

#count a perticula number in list
print(f"there are {List.count(10)} 10s in the list")

#remove the first 10 from list
print(f"Removing 10 from position {List.index(10)}")
List.remove(10)
print(f"content of list after removing 10 is {List}")

#pop from the end
List.pop()
print(f"content of list after pop is {List}")


