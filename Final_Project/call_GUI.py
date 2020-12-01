from Final_Project.login_GUI import *
from tkinter import *



root = Tk()

login_btn = Button(root, text="Login", width=20, bg="green", command=signin)

login_btn.pack(padx=20, pady=20)

mainloop()
