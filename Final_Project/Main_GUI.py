from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.geometry("800x450")
root.title('Online Food Order System')
root.iconbitmap(r'buy_online_5Wq_icon.ico')
#*****************upper block*****************************
upper_Root = Frame(root, bg="light blue", height=100)
title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial',28,'bold','underline'))

upper_Root.pack(side=TOP, fill=BOTH, expand=1)
title.pack(pady=30)

#*****************upper block*****************************
center_Root = Frame(root, bg="gray92", height=300)
top_center = Frame(center_Root, bg="gray92", height=140)
pic = Image.open("shopping-bag.png")
resized = pic.resize((150, 100), Image.ANTIALIAS)
mypic = ImageTk.PhotoImage(resized)
image_top_center = Label(top_center, image = mypic)
center_center = Frame(center_Root, bg="yellow", height=80)
bottom_center = Frame(center_Root, bg="blue", height=80)

center_Root.pack(side=TOP, fill=BOTH, expand=1)
top_center.pack(side=TOP, fill=BOTH, expand=1)
image_top_center.pack(pady=20)
center_center.pack(side=TOP, fill=BOTH, expand=1)
bottom_center.pack(side=TOP, fill=BOTH, expand=1)


#*****************upper block*****************************
bottom_Root = Frame(root, bg="light blue", height=50)
copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof 2020", bg="light blue", font=('arial',12,'bold'))

bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
copyRight.pack()

mainloop()

