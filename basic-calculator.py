import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")

def addThisDigit(number):
    global textValue
    print(number)
    textValue = textValue + str(number)
    label.config(text = textValue)


textValue = "0"

label = tkinter.Label(mainWindow, text=textValue)
label.pack()

buttonOne = tkinter.Button(mainWindow, text="1", command = lambda : addThisDigit(1))
buttonOne.pack()

buttonTwo = tkinter.Button(mainWindow, text="2", command = lambda : addThisDigit(2))
buttonTwo.pack()

addOperator = tkinter.Button(mainWindow, text="+", command = lambda : addOperator("+"))
addOperator.pack()

def addOperator(operator):
    global textValue
    print(operator)
    firstNumber = int(label.cget("text"))
    textValue = "0"
    print(firstNumber)
    label.config(text = "0")

mainWindow.mainloop()
