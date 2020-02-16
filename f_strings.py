#this program shows off the f-string in python

normal_string = "Umesh"

#save and f-string to a variable
f_string = f"this is, {normal_string}"

print(f_string)

#save an f-string with a variable decided upon later
empty_f_string = "Is this a valid f-string? {}"

print(empty_f_string.format(True))

#string combine
first = "Hello"
second = " There"
print(first + second)

#store a dividing line char (-)
divider = "-"
dividing_line = "{}"
print(dividing_line.format(divider * 10))
