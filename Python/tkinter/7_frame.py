from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code')
root.iconbitmap(r"resources\icon.ico")

frame = LabelFrame(root, text="This is my frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)




root.mainloop()