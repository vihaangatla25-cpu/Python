try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma : "))
    result = num1 / num2
    print("Result is", result)
#using multiple except block for different type of error 

except ZeroDivisionError:
    print("Divion by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers seperated by comma like 1, 2")

except:
    print("Wrong input")

except:
    print("No exceptions")

finally:
    print("This will execute no matter what")