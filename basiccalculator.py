# We want to obtain two number inputs from the user
# as well as an operation of: +, -, /, *, or exit

from operator import truediv

num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
myoperator = raw_input("Enter an operator (choices are +, -, /, *): ")

haveresult = True #To show we have the correct input for a result

if myoperator == "+" :
    result = num1 + num2
elif myoperator == "-":
    result = num1 - num2
elif myoperator == "*":
    result = num1 * num2
elif myoperator == "/" and num2 == 0:
    print("Cannot divide by 0.")
    haveresult = False
elif myoperator == "/" and num2 !=0:
    result = num1 / num2
else:
    haveresult = False

#Did the user want a result or wanted to exit?
if haveresult == True:
    print(result)
else:
    print("Thank you and goodbye!")



