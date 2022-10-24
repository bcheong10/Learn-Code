from tkinter import *

# Root Widget
root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text = "Hello World")
myLabel2 = Label(root, text = "My name is Ben")

# Specifies location of label using grid system
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Shoves into the screen
# myLabel.pack()

root.mainloop()