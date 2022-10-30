from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code')
root.iconbitmap(r"resources\icon.ico")

frame = LabelFrame(root, text="This is a frame", padx=10, pady=10)
frame.pack(padx=10, pady=10)

button1 = Button(frame, text="This is a button")
button2 = Button(frame, text="This is another button")

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)



root.mainloop()