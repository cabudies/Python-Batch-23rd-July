##firstNumber = 10
##secondNumber = 20
##
##if (firstNumber > 10):
##    print("Yes. It's greater than 10.")
##elif (firstNumber == 10):
##    print("Yes. It's equal to 10.")
##else:
##    print("No. It's less than 10.")
##    print("Hello World.")

##for i in range(0, 3):
##    print("Hello World ", i)

##startIndex = int(input("Enter the start index:  "))
##endIndex = int(input("Enter the end index: "))
##incrementValue = int(input("Enter the increment value: "))
##
##if (startIndex > endIndex):
##    print("Start index is greater than end index.")
##    incrementValue = incrementValue * -1
##    
##    for i in range(startIndex, endIndex, incrementValue):
##        print("Hello World ", i)
##
##elif (endIndex > startIndex):
##    print("End index is greater than start index.")
##
##    for i in range(startIndex, endIndex, incrementValue):
##        print("Hello World ", i)
##
##else:
##    print("Sorry, your start index and end index is same. So, we cannot print anything.")

for i in range(0, 4):
    for j in range(0, i):
        print("*", end=" ")
    print("")




















