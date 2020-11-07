from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x370")
root.title("Online Shopping System")
root.iconbitmap(r'buy_online_5Wq_icon.ico')


#*****************Upper part***************

Upper_root = Frame(root,bg="cornflower blue", height=50)
Title_upper_root = Label(Upper_root, text="Online Shopping System", bg="cornflower blue", pady=10, font=('arial',28,'bold'))


Upper_root.pack(side= TOP, fill= X)
Title_upper_root.pack()




#*****************Center part*******************
Center_root = Frame(root,bg="gray92", height=320)
part1_Center_root = Frame(Center_root, bg="gray92", height=170)
part2_Center_root = Frame(Center_root, bg="gray92", height=150)
fbutton1_Cnter_root = Frame(part2_Center_root, bg="blue", width=400, height=150)
fbutton2_Cnter_root = Frame(part2_Center_root, bg="red", width=400, height=150)
pic = Image.open("shopping-bag.png")
resized = pic.resize((150, 100), Image.ANTIALIAS)
mypic = ImageTk.PhotoImage(resized)
image_upper_root = Label(part1_Center_root, image = mypic)
Center_root.pack(side= TOP, fill= X)
part1_Center_root.pack(side=TOP, fill=X)
image_upper_root.pack(pady=10)
part2_Center_root.pack(side= BOTTOM, expand=1, fill=BOTH)
fbutton1_Cnter_root.pack(side=LEFT, fill=BOTH)
fbutton2_Cnter_root.pack(side=LEFT, fill=BOTH)

#*****************end part*******************
Bottom_root = Frame(root,bg="cornflower blue", height=30)
Bottom_root.pack(side= BOTTOM, fill= X)

mainloop()
