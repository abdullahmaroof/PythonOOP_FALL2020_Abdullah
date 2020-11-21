from tkinter import *

root = Tk()

#*****************upper block*****************************
upper_Root = Frame(root, bg="light blue")


upper_Root.pack(side=TOP, fill=BOTH, expand=1)

#*****************upper block*****************************
center_Root = Frame(root, bg="gray92")


center_Root.pack(side=TOP, fill=BOTH, expand=1)

#*****************upper block*****************************
bottom_Root = Frame(root, bg="light blue")


bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)

mainloop()

