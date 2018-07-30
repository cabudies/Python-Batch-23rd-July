## #Create a function without parameter
##def functionName():
##    print("Hello World")
##
##functionName()
##
##
## #Create a function with parameters
##def functionName(name):
##    print("Hello! " + name)
##
##functionName("Gurjas")
##
## #Create a function that returns an value
##def sum(firstNumber, secondNumber):
##    thirdNumber = firstNumber + secondNumber
##    return thirdNumber
##
##result = sum(10, 20)
##print(result)
##
##input - User name
##first Number, Second Number
##
##Hello Gurjas, the sum of 10, 20 is: 30


def sumTwoNumbers(name, firstNumber, secondNumber):
    thirdNumber = firstNumber + secondNumber
    print("Hello! ", name, ". Sum of two numbers i.e. ", firstNumber, ", ",
          secondNumber, " is: ", thirdNumber)

name = input("Enter your name: ")
try:
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    sumTwoNumbers(name, firstNumber, secondNumber)
    
except ValueError:
    print("Sorry, enter only integer value for numbers.")

























