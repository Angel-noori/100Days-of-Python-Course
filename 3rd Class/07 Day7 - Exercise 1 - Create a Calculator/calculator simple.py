# Python program to make a simple calculator by Zidi

# take inputs3
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# choise operation
print("Operation: +, -, *, /")
select = input("Select operations: ")

# check operations and display result
# add(+) two numbers
if select == "+":
    print(num1, "+", num2, "=", num1+num2)

# subtract(-) two numbers
elif select == "-":
    print(num1, "-", num2, "=", num1-num2)

# multiplies(*) two numbers
elif select == "*":
    print(num1, "*", num2, "=", num1*num2)

# divides(/) two numbers
elif select == "/":
    print(num1, "/", num2, "=", num1/num2)

else:
    print("Invalid input")