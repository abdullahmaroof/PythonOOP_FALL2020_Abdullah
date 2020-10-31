from tkinter import *

root = Tk()

f = Frame(root, bg="blue")
f.pack(side= TOP, bg="red", padx=20, pady=10, fill= f)
lab1 = Label(text="Abdullah")
lab1.pack()


BUT1 = Button(text="Click")
BUT1.pack()

root.mainloop()
