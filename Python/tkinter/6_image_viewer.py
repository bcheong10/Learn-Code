from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code')
root.iconbitmap(r"resources\icon.ico")

my_img1 = ImageTk.PhotoImage(Image.open(r"resources\photo1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open(r"resources\photo2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open(r"resources\photo3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open(r"resources\photo4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open(r"resources\photo5.jpg"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

myLabel = Label(image=my_img1)
myLabel.grid(row=0, column=0, columnspan=3)

def previous(image_number):
    global myLabel
    global button_next
    global button_previous

    if image_number > 0:

        myLabel.grid_forget() # Removes the current label
        myLabel = Label(image=img_list[image_number - 1])
        myLabel.grid(row=0, column=0, columnspan=3)

        button_next = Button(root, text="Next", padx=15, pady=5, command=lambda: next(image_number - 1))
        button_previous = Button(root, text="Previous", padx=15, pady=5, command=lambda: previous(image_number - 1))
        status = Label(root, text =f"Image {image_number} of {len(img_list)}")
        

    if image_number == 1:
        button_previous = Button(root, text="Previous", padx=15, pady=5, state=DISABLED)

    button_previous.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    button_quit.grid(row=1, column=1)
    status.grid(row=2, column=0, columnspan=3)


def next(image_number):
    global myLabel
    global button_next
    global button_previous

    myLabel.grid_forget() # Removes the current label
    myLabel = Label(image=img_list[image_number + 1])

    button_next = Button(root, text="Next", padx=15, pady=5, command=lambda: next(image_number + 1))
    button_previous = Button(root, text="Previous", padx=15, pady=5, command=lambda: previous(image_number + 1))
    myLabel.grid(row=0, column=0, columnspan=3)
    status = Label(root, text =f"Image {image_number + 2} of {len(img_list)}")

    if image_number == 3:
        button_next = Button(root, text="Next", padx=15, pady=5, state=DISABLED)

    button_previous.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    button_quit.grid(row=1, column=1)
    status.grid(row=2, column=0, columnspan=3)
 

# List of buttons
button_previous = Button(root, text="Previous", state=DISABLED, padx=15, pady=5, command=lambda: previous(0))
button_next = Button(root, text="Next", padx=15, pady=5, command=lambda: next(0))
button_quit = Button(root, text="Exit Program", padx=20, pady=5, command=root.quit)

# Button position
button_previous.grid(row=1, column=0)
button_next.grid(row=1, column=2)
button_quit.grid(row=1, column=1)

# Status bar
status = Label(root, text =f"Image 1 of {len(img_list)}")
status.grid(row=2, column=0, columnspan=3)




root.mainloop()