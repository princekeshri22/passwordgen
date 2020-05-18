print("Enter the file name to see the passwords: ",end="")

n=input()
print()
name=n+".txt"

with open(name)as see:
	
	print(see.readlines())

