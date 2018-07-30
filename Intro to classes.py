### class in python
##class Student:
##    # class variables
##    studentName = ""
##    studentAddress = ""
##
##    # constructor in python
##    # self keyword is compulsory in class-functions
##    def __init__(self): 
##        print("Hello you are in class")
##        # use self keyword to reference the class functions and variables.
##        self.takeUserInput()
##        print(self.studentName, self.studentAddress)
##
##    # function inside a class.
##    def takeUserInput(self):
##        self.studentName = input("Enter the student's name. ")
##        self.studentAddress = input("Enter student's address.")
##        
##
##obj = Student()
##
##





### class in python
##class Student:
##    # class variables
##    studentName = ""
##    studentAddress = ""
##    
##    def __init__(self, studentName, studentAddress): 
##        print("Hello you are in class")
##        self.studentName = studentName
##        self.studentAddress = studentAddress
##        print(self.studentName, self.studentAddress)
##        
##studentName = input("Enter your name: ")
##studentAddress = input("Enter your address ")
##obj = Student(studentName, studentAddress)

class Numbers:
    firstNumber = 0
    secondNumber = 0

    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        result = self.multiply()
        print(result)

    def multiply(self):
        result = self.firstNumber * self.secondNumber
        return result
##        print("Multiplication result is: ", result)


firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
obj = Numbers(firstNumber, secondNumber)
