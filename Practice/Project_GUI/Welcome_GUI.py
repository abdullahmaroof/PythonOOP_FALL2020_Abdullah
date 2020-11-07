from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x600")
root.title("Online Shopping System")
root.iconbitmap(r'buy_online_5Wq_icon.ico')


#*****************Upper part***************

Upper_root = Frame(root,bg="cornflower blue", height=100)
Title_upper_root = Label(Upper_root, text="Online Shopping System", bg="cornflower blue", pady=10)


Upper_root.pack(side= TOP, fill= X)
Title_upper_root.pack()




#*****************Center part*******************
Center_root = Frame(root,bg="gray70", height=400)
part1_Center_root = Frame(Center_root, bg="gray70", height=170)
part2_Center_root = Frame(Center_root, bg="blue", height=230)
pic = Image.open("shopping-bag.png")
resized = pic.resize((150, 100), Image.ANTIALIAS)
mypic = ImageTk.PhotoImage(resized)
image_upper_root = Label(part1_Center_root, image = mypic)
Center_root.pack(side= TOP, fill= X)
part1_Center_root.pack(side=TOP, fill=X)
image_upper_root.pack(pady=10)
part2_Center_root.pack(side= BOTTOM, expand=1, fill=BOTH)

#*****************bottom part*******************
Bottom_root = Frame(root,bg="cornflower blue", height=70)
Bottom_root.pack(side= TOP, fill= X)

#*****************end part*******************
Bottom_root = Frame(root,bg="light grey", height=30)
Bottom_root.pack(side= BOTTOM, fill= X)

mainloop()
