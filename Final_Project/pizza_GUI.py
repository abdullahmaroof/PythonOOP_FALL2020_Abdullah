from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("800x630")
root.title('Online Food Order System')
root.iconbitmap(r'buy_online_5Wq_icon.ico')
#*****************upper block*****************************
upper_Root = Frame(root, bg="light blue", height=100)
title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial',28,'bold','underline'))

upper_Root.pack(side=TOP, fill=BOTH, expand=1)
title.pack(pady=30)


#*********************Center Block*******************
center_Root = Frame(root, bg="gray92", height=500)

#*********top-center*****
top_center = Frame(center_Root, bg="gray92", height=100)
pic = Image.open("pizza.PNG")
resized = pic.resize((150, 100), Image.ANTIALIAS)
mypic = ImageTk.PhotoImage(resized)
image_top_center = Label(top_center, image = mypic)

#*********center-center pack*****
center_center = Frame(root, bg="white", height=400)
subtitle_frame = Frame(center_center, bg="white", height=50)
subtitle_label = Label(subtitle_frame, text="Pizza Menu", font=('arial',16,'bold','underline'), bg="white")
#chicken fajita pizza
chfajita_frame = Frame(center_center, bg="red", height=50)
peeripeeri_frame = Frame(center_center, bg="green", height=50)
mexico_frame = Frame(center_center, bg="blue", height=50)
cheese_frame = Frame(center_center, bg="orange", height=50)
BBQ_frame = Frame(center_center, bg="purple", height=50)


center_Root.pack(side=TOP, fill=BOTH, expand=1)

#*********top-center pack*****
top_center.pack(side=TOP, fill=BOTH, expand=1)
image_top_center.pack(pady=20)


#********center-center pack*******
center_center.pack(side=TOP, fill=BOTH, expand=1, pady=10, padx=20)
subtitle_frame.pack(side=TOP, fill=BOTH, expand=1)
subtitle_label.pack(pady=10)
chfajita_frame.pack(side=TOP, fill=BOTH, expand=1)
peeripeeri_frame.pack(side=TOP, fill=BOTH, expand=1)
mexico_frame.pack(side=TOP, fill=BOTH, expand=1)
cheese_frame.pack(side=TOP, fill=BOTH, expand=1)
BBQ_frame.pack(side=TOP, fill=BOTH, expand=1)


#*****************bottom block*****************************
bottom_Root = Frame(root, bg="light blue", height=50)
copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof 2020", bg="light blue", font=('arial',12,'bold'))

bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
copyRight.pack()

mainloop()