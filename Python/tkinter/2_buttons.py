from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button")
    myLabel.pack()

myButton = Button(root, text="Click me!", state=None, padx=50, pady=50, command=myClick, fg="blue", bg="green")
myButton.pack()

root.mainloop()