import random as r
import time
from  colorama import Fore, Style

def pwdgen():
  print(Fore.CYAN,Style.BRIGHT)
  print("::::::: ::        :: :::::$   ")
  print("::   :: ::   /\   :: ::    @  ")
  print("::___:: ::  /  \  :: ::    :: ")
  print("::      :: /    \ :: ::    @  ")
  print("::      ::/      \:: :::::$  GENERATOR ")
  print("::")
  print(Fore.RED, Style.BRIGHT)
  print("Passwords are like underwear:\nyou don’t let people see it, \nyou should change it very often, \nand you shouldn’t share it with strangers.")
 
  
  
  
  char=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0","<",">","{","}","[","]","&","!","+","*","=","@","$","#","%","A","Q","W","E","R","T","Y","U","I","O","P","S","D","F","G","H","J","K","L","Z","C","X","V","B","N","M"]  
  
  pwd=""
  
  print()
  print("##########################################")
  
  print(Fore.GREEN)
  
  print("For what account (ex:- Facebook):", end="")
  ac=input()
  print()
  print("Length your password(min.8 recomended):",end=""  )
  
  len=int(input())
  print(Style.RESET_ALL)
  print(Fore.YELLOW,"Please wait")
  i=0
  while(i<len):
    time.sleep(0.08)
    print("*")
    
    pwd=pwd+r.choice(char)
    i+=1
  str=f"Password for {ac} is: {pwd}\n"
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
      nm=nm+".txt"
      
      with open(nm,"a")as txt:
        txt.write(str)
        
        print()
      print("Your password has been saved to ",nm)
        
    else:
      with open("passwords.txt","a")as d:
        d.write(str)
        
        print()
        print("Your password has been saved to passwords.txt") 
  
    
  else:
    print("Oops! O.K.")
    
def reuse():
  print("Generate more passwords(y/n): ",end="")

  mr=input()

  if(mr=="n"):
    print()
    print(Fore.WHITE,"Thanks for using. Hope see you next time.")
    
    print(Style.RESET_ALL)
  
  else:
    pwdgen()
    reuse()
    
pwdgen()
print()
reuse()
print()    
