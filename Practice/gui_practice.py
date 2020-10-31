from tkinter import *

root = Tk()

root.geometry("733x433")

#root.minsize(200,150)

#root.maxsize(1500,1000)

lab1 = Label(text="Welcome to pycharm")
logo = PhotoImage(file="C:\\Users\\DELL\\Pictures\\pycharm.PNG")
lab_image = Label(image=logo)
lab2 = Label(text="PYCHARM")
lab3 = Label(text="Version: 2020.2.0.9")
lab4 = Label(text="Create a new Project")

lab1.pack()
lab_image.pack()
lab2.pack()
lab3.pack()
lab4.pack()

root.mainloop()