from tkinter import *

root = Tk()

root.geometry("800x600")

#*****************Upper part***************

Upper_root = Frame(root,bg="cornflower blue", height=100)
Upper_root.pack(side= TOP, fill= X)


#*****************Center part*******************
Center_root = Frame(root,bg="gray70", height=400)
Center_root.pack(side= TOP, fill= X)

#*****************bottom part*******************
Bottom_root = Frame(root,bg="cornflower blue", height=70)
Bottom_root.pack(side= TOP, fill= X)

#*****************end part*******************
Bottom_root = Frame(root,bg="light grey", height=30)
Bottom_root.pack(side= BOTTOM, fill= X)

mainloop()
