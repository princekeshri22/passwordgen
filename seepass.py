from colorama import Fore

print(Fore.YELLOW,"Enter the file name to see the passwords: ",end="")

n=input()
print()
name=n+".txt"

with open(name)as see:
	
	print(see.readlines())

