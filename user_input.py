#how to handle user input in python

print("provide a number")
num = input()
print(f"number = {num}")

#have the inpute on the same line as the question
print("give a number again: ", end = ' ')
num = input()
print(f"number = {num}")

#get rid of print altogether
num = input("enter a number")
print(f"number = {num}")

#check the type of the input
print(type(num))
