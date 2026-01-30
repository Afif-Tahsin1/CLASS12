valid = False
from colorama import Fore
while not valid:
    try: 
        n = int(input("Please enter a number:"))
        while n%2 == 0:
            print("Bye")
        valid = True
    except ValueError:
        print(Fore.RED + "Invalid")
        valid = False
