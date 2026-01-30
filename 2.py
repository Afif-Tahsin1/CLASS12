try:
    num1,num2 = eval(input('Please enter 2 numbers, seperate by coma: '))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except SyntaxError:
    print("coma is missing! Enters the numbers seperated by coma like 1,2")
except Exception as e:
    print(f"Wrong input! error: {e}")
else:
    print('no exception')
finally:
    print("This will execute no matter what")