try:
    number = int(input("Enter a number: "))
    print(f"The number entered is {number}")
except ValueError as e:
    print(f"Exception: {e}")