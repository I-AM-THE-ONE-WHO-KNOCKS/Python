#string manipulation

from sys import argv

name, csv_string = argv

#string variable
s = "Test string"

#print the first 4 chars
print(s[0:4:1])

#print the remainder of the string
print(s[5:])

#spilt the string into an array of strings
s = s.split(" ")
print(s)

#combine the strigs back
s = " ".join(s)
print(s)

#csv format
print(csv_string)
csv_string = csv_string.split(",")
print(csv_string)

#make the entire string uppercase
s = s.upper()
print(s)

#make is lower case
s = s.lower()
print(s)