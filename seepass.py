from colorama import Fore,Style
from pyfiglet import Figlet

print(Fore.CYAN,Style.BRIGHT)
custom_fig = Figlet(font='xsbook')
print(custom_fig.renderText('See Pass'))
print(Fore.YELLOW)
print("File Name without .txt: ",end="")

n=input()
print()
name=n+".txt"
try:
    with open(name)as see:
  
      print(see.readlines())
      
except Exception as e:
	print("No Such File....")
  
