from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code')
root.iconbitmap(r"resources\icon.ico")

my_img = ImageTk.PhotoImage(Image.open(r"resources\photo.jpg"))
myLabel = Label(image=my_img)
myLabel.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()





root.mainloop()