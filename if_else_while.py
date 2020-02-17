# this program shows the conditions an while loop

a = 3
b = 5

#if else case
if(a==3):
	print("a == 3")
elif(b == 5):
	print("b==5")
else:
	print("default")

#while loop
i = 0;
while(i != 10):
	i +=1

	if i == 3:
		print(f"only print on third iteration ({i})")
		#continue
		continue
	#print something ever other iteration 
	print(f"print ({i})")

	if i == 7:
		break;

print(f"Exit when i = {i}")