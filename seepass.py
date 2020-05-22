from colorama import Fore,Style
from pyfiglet import Figlet

print(Fore.CYAN,Style.BRIGHT)
custom_fig = Figlet(font='xsbook')
print(custom_fig.renderText('See Pass'))
print(Fore.YELLOW)

def seeing():
    print("File Name without .txt: ",end="")
    n=input()
    print()
    name=n+".txt"
    try:
       with open(name)as see:
  
          out=see.readlines()
          for k in out:
           print(Fore.GREEN,Style.BRIGHT,k)
           print(Style.RESET_ALL)
      
    except Exception as e:
	    print("No Such File ",name)
	    print()
	    print("Try Again (y/n): ",end="")
	    tr=input()
	    print()
	    if(tr=="n"):
	    	print(Fore.RED,Style.BRIGHT,"Thanks For Using")	
	    	print(Style.RESET_ALL)
	    else:
	    	 seeing()
  
seeing()