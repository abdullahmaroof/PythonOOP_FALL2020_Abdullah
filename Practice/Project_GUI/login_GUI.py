from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x490")
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
part2_Center_root = Frame(Center_root, bg="gray92", height=300)
PLabel_part2c_root = Frame(part2_Center_root, bg="gray92", width=200, height=40)
label_part2c_root = Label(PLabel_part2c_root, bg="gray92", text="LOG IN", font=('arial',18,'underline','bold'))
p1form_part2c_root = Frame(part2_Center_root, bg="gray92", height=80)
lp1form_part2c_root = Frame(p1form_part2c_root, width=400, bg="gray92", height=80)
llabel_p1form = Label(lp1form_part2c_root, text="User Name: ", font=('arial',10,'bold'))
rp1form_part2c_root = Frame(p1form_part2c_root, width=400, bg="gray92", height=80)
p2form_part2c_root = Frame(part2_Center_root, bg="gray92", height=80)
lp2form_part2c_root = Frame(p2form_part2c_root, width=400, bg="gray92", height=80)
rp2form_part2c_root = Frame(p2form_part2c_root, width=400, bg="gray92", height=80)
p3form_part2c_root = Frame(part2_Center_root, bg="gray92", height=50)
loginbuttonp3_part2c_root = Button(p3form_part2c_root, text="LOG IN", width=20, height=2, bg="light blue",font=('arial',10,'bold'))
pic = Image.open("shopping-bag.png")
resized = pic.resize((150, 100), Image.ANTIALIAS)
mypic = ImageTk.PhotoImage(resized)
image_upper_root = Label(part1_Center_root, image = mypic)
Center_root.pack(side= TOP, fill= X)
part1_Center_root.pack(side=TOP, fill=BOTH)
image_upper_root.pack(pady=10)
part2_Center_root.pack(side= TOP, fill=X)
PLabel_part2c_root.pack(side=TOP,fill=BOTH, padx=300, pady=10)
label_part2c_root.pack()
p1form_part2c_root.pack(side=TOP, fill=BOTH)
lp1form_part2c_root.pack(side=LEFT, fill=BOTH)
llabel_p1form.pack()
rp1form_part2c_root.pack(side=LEFT, fill=BOTH)
p2form_part2c_root.pack(side=TOP, fill=BOTH)
lp2form_part2c_root.pack(side=LEFT, fill=BOTH)
rp2form_part2c_root.pack(side=LEFT, fill=BOTH)
p3form_part2c_root.pack(side=TOP, fill=BOTH)
loginbuttonp3_part2c_root.pack(pady=5)


#*****************end part*******************
Bottom_root = Frame(root,bg="cornflower blue", height=30)
Bottom_root.pack(side= BOTTOM, fill= X)

mainloop()