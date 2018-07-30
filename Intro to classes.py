class Student:
    studentName = ""
    studentAddress = ""

    def __init__():
        print("Hello you are in class")
        self.takeUserInput()
        print(self.studentName, self.studentAddress)

    def takeUserInput(self):
        self.studentName = input("Enter the student's name. ")
        self.studentAddress = input("Enter student's address.")
        #print(userName, address)

obj = Student()


