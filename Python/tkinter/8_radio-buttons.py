from tkinter import *
from PIL import ImageTk, Image

root = Tk()

food = ["Pizza", "Hamburger", "Hotdog"]

pizza = Image.open(r"resources\pizza.png")
burger = Image.open(r"resources\hamburger.png")
hotdog = Image.open(r"resources\hotdog.png")

pizza = pizza.resize((50,50))
burger = burger.resize((50,50))
hotdog = hotdog.resize((50,50))

pizza = ImageTk.PhotoImage(pizza)
burger = ImageTk.PhotoImage(burger)
hotdog = ImageTk.PhotoImage(hotdog)

foodImage = [pizza, burger, hotdog]

def order():
    if x.get() == 0:
        txt = Label()
        txt.grid_forget()
        txt = Label(root, text="Pizza is selected", padx=20).grid(row=3, column=0)
    elif x.get() == 1:
        txt = Label()
        txt.grid_forget()
        txt = Label(root, text="Hamburger is selected", padx=20).grid(row=3, column=0)
    else:
        txt = Label()
        txt.grid_forget()
        txt = Label(root, text="Hotdog is selected", padx=20).grid(row=3, column=0)

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(root,
                              text = food[index],
                              variable = x, # Groups the radiobuttons together if they share the same variable
                              value=index, # Assigns each button a different value
                              padx = 25,
                              font = ("Arial", 15),
                              image = foodImage[index], # Adds images to radiobutton
                              compound = 'left', # Adds image and text together
                              indicatoron = 0, # Removes circle indicators, changes input feedback to push buttons
                              width = 200,
                              command = order
                              )

    radiobutton.grid(row=index, column=0)

print("Hello")
root.mainloop()
