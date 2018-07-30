# Variables in python are declared without datatype

##firstNumber = 20.41 # variable-name = value
##secondNumber = 33.12

firstNumber = int(input('Enter the first number.'))
secondNumber = int(input('Enter the second number.'))

result = firstNumber + secondNumber
##
### we use print function to print any output
### to print any variable which is not of String datatype, use str() function
### to convert it only while displaying.
### print("Sum of two number is: " + str(result))
##
##print("Sum of two number i.e. %f and %f is: %f" % (firstNumber, secondNumber, result))

print("Sum of two numbers i.e. ", firstNumber, " and ", secondNumber, " is: ", result)
