import random as r
import time

def pwdgen():
	char=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0","<",">","{","}","[","]","&","!","+","*","=","@","$","#","%"]
	
	pwd=""
	print("For what account (ex:- Facebook):", end="")
	ac=input()
	print()
	print("Length of your password (min.8 recomended) :  ",end=""	)
	
	len=int(input())
	print("Please wait")
	i=0
	while(i<len):
		time.sleep(0.08)
		print("*")
		
		pwd=pwd+r.choice(char)
		i+=1
	str=f"Password for {ac} is: {pwd}"
	print()
	print(str)
	print()
	print("Do you want to save it(y/n): ",end="")
	op=input()
	print()
	
	if(op=="y"):
		
		print("Do you want custom file name (y/n ) : ",end="")
		
	
		fn=input()
		print()

		if(fn=="y"):
			print("Enter file name: ",end="")
			nm=input()
			
			with open(nm,"a")as txt:
				txt.write(str)
				print()
			print("Your password has been saved...")
				
		else:
			with open("passwords.txt","a")as d:
				d.write(str)
				print()
				print("Your password has been saved to passwords.txt...")
	
		
	else:
		print("Oops! O.K.")
pwdgen()
print()		
print("Do you want to generate more passwords(y/n): ")

mr=input()

if(mr=="n"):
	print()
	print("Thanks for using. Hope see you next time.")
	
else:
	pwdgen()
				
			
	
	
