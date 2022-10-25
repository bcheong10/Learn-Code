from tkinter import *

root = Tk()

# Input Box
e = Entry(root, width=20, borderwidth=5, bg="white", fg="black")
# Inserts default text in text box
e.insert(0, "Enter your name: ")
e.pack()

def myClick():
    txt = f"Hello, {e.get()}"
    myLabel = Label(root, text=txt) # e.get() function retrieved whatever that was typed in Entry box
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", state=None, padx=50, pady=50, command=myClick, fg="black", bg="white")
myButton.pack()

root.mainloop()