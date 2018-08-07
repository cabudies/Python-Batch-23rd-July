import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Calculator")

textValue = "0"
firstNumber = 0
secondNumber = 0

def takeInput(number):
    global textValue
    if textValue == "0":
        textValue = str(number)
    else:
        textValue = textValue + str(number)
    print(textValue)
    mainLabel.config(text = textValue)

def operator(operator):
    global firstNumber
    global secondNumber
    global textValue
    if (operator == "+"):
        print(operator)
        if (firstNumber == 0):
            firstNumber = int(textValue)
        elif (secondNumber == 0):
            secondNumber = int(textValue)
        else:
            firstNumber = firstNumber + secondNumber
            secondNumber = int(textValue)
        textValue = "0"
        mainLabel.config(text = textValue)

def displayResult():
    global firstNumber, secondNumber, textValue
    print("result")
    secondNumber = int(textValue)
    thirdNumber = int(firstNumber) + int(secondNumber)
    print(thirdNumber)
    textValue = str(thirdNumber)
    mainLabel.config(text = textValue)

mainLabel = tk.Label(root, text = textValue, width="30")
mainLabel.grid(row = 0, columnspan = 4)

buttonOne = tk.Button(root, text = "1", command = lambda : takeInput(1))
buttonOne.grid(row = 1, column = 0)

buttonTwo = tk.Button(root, text = "2", command = lambda : takeInput(2))
buttonTwo.grid(row = 1, column = 1)

buttonThree = tk.Button(root, text = "3", command = lambda : takeInput(3))
buttonThree.grid(row = 1, column = 2)

buttonPlus = tk.Button(root, text = "+", command = lambda : operator("+"))
buttonPlus.grid(row = 1, column = 3)

buttonEqual = tk.Button(root, text="=", command = lambda: displayResult())
buttonEqual.grid(row = 2, columnspan=2, padx=10)

mainLabel.mainloop()
