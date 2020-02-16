#this program demonstrates file operatios

from sys import argv
from os.path import exists

# first argument is always the program file name.
prog, file_name = argv

print(prog)
print(file_name)

#check if the file exists 
print(exists(file_name))

#default open is read only
text = open(file_name)

#read the content
all_lines = text.read()

print(all_lines)

text.close()

text = open(file_name)

#read lines as collection of lines
lines = text.readlines()

print(lines)

text.close()

#open with write mode
text = open(file_name, 'w')

#clear the file
text.truncate()

line1 = "hello\n"
line2 = "there\n"

text.write(line1)
text.write(line2)

text.close()
