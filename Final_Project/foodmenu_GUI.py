from Final_Project.Paratharoll_GUI import call_parathamenu
from Final_Project.pizza_GUI import call_pizzamenu
from Final_Project.biryani_GUI import call_biryanimenu
from tkinter import *
from PIL import ImageTk, Image
from Final_Project.burger_gui import call_burgermenu

def call_menu():
    root = Toplevel()

    root.geometry("800x750")
    root.title('Online Food Order System')
    root.iconbitmap(r'buy_online_5Wq_icon.ico')
    #*****************upper block*****************************
    upper_Root = Frame(root, bg="light blue", height=100)
    title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial',28,'bold','underline'))

    upper_Root.pack(side=TOP, fill=BOTH, expand=1)
    title.pack(pady=30)

    #*****************center block*****************************
    center_Root = Frame(root, bg="gray92", height=520)
    top_center = Frame(center_Root, bg="gray92", height=140)
    pic = Image.open("shopping-bag.png")
    resized = pic.resize((150, 100), Image.ANTIALIAS)
    mypic = ImageTk.PhotoImage(resized)
    image_top_center = Label(top_center, image = mypic)
    center_center = Frame(center_Root, bg="gray92", height=80)
    sub_title = Label(center_center, text="Order Food", bg="gray92", font=('arial',20,'underline','bold'))
    bottom_center = Frame(center_Root, bg="white", height=320)
    pizza_frame = Frame(bottom_center, bg="white", height=60)
    pframe_left = Frame(pizza_frame, bg="white", height=60)
    pizza = Image.open("pizza.PNG")
    pi_size = pizza.resize((100,70), Image.ANTIALIAS)
    pizzapic = ImageTk.PhotoImage(pi_size)
    pizza_label = Label(pframe_left, image= pizzapic)
    pframe_right = Frame(pizza_frame, bg="white", height=60)
    pizza_btn = Button(pframe_right,  text="Pizza", command= lambda : call_pizzamenu(), width=20, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    burger_frame = Frame(bottom_center, bg="white", height=60)
    bframe_left = Frame(burger_frame, bg="white", height=60)
    burger = Image.open("burger.PNG")
    bu_size = burger.resize((100,70), Image.ANTIALIAS)
    burgerpic = ImageTk.PhotoImage(bu_size)
    burger_label = Label(bframe_left, image= burgerpic)
    bframe_right = Frame(burger_frame, bg="white", height=60)
    burger_btn = Button(bframe_right,  text="Burger", command= lambda : call_burgermenu(), width=20, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    biryani_frame = Frame(bottom_center, bg="white", height=80)
    biframe_left = Frame(biryani_frame, bg="white", height=80)
    biryani = Image.open("biryani.PNG")
    bi_size = biryani.resize((100,70), Image.ANTIALIAS)
    biryanipic = ImageTk.PhotoImage(bi_size)
    biryani_label = Label(biframe_left, image= biryanipic)
    biframe_right = Frame(biryani_frame, bg="white", height=60)
    biryani_btn = Button(biframe_right,  text="Biryani", command= lambda : call_biryanimenu(), width=20, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    paratharoll_frame = Frame(bottom_center, bg="white", height=60)
    paframe_left = Frame(paratharoll_frame, bg="white", height=60)
    paratharoll = Image.open("paratharoll.PNG")
    pa_size = paratharoll.resize((100,70), Image.ANTIALIAS)
    parathapic = ImageTk.PhotoImage(pa_size)
    paratha_label = Label(paframe_left, image= parathapic, pady=10)
    paframe_right = Frame(paratharoll_frame, bg="white", height=80)
    paratha_btn = Button(paframe_right,  text="Paratha Roll", command= lambda : call_parathamenu(), width=20, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")


    center_Root.pack(side=TOP, fill=BOTH, expand=1)
    top_center.pack(side=TOP, fill=BOTH, expand=1)
    image_top_center.pack(pady=20)
    center_center.pack(side=TOP, fill=BOTH, expand=1)
    sub_title.pack(pady=10)
    bottom_center.pack(side=TOP, fill=BOTH, expand=1, padx=20, pady=10)
    pizza_frame.pack(side=TOP, fill=BOTH, expand=1)
    pframe_left.pack(side=LEFT, fill=BOTH, expand=1, pady=10)
    pizza_label.pack(side=RIGHT)
    pframe_right.pack(side=LEFT, fill=BOTH, expand=1, pady=10)
    pizza_btn.pack(side=LEFT, padx= 20)
    burger_frame.pack(side=TOP, fill=BOTH, expand=1)
    bframe_left.pack(side=LEFT, fill=BOTH, expand=1, pady=10)
    burger_label.pack(side=RIGHT)
    bframe_right.pack(side=LEFT, fill=BOTH, expand=1, pady=10)
    burger_btn.pack(side=LEFT, padx= 20)
    biryani_frame.pack(side=TOP, fill=BOTH, expand=1)
    biframe_left.pack(side=LEFT, fill=BOTH, expand=1, pady=10)
    biryani_label.pack(side=RIGHT)
    biframe_right.pack(side=LEFT, fill=BOTH, expand=1, pady=10)
    biryani_btn.pack(side=LEFT, padx= 20)
    paratharoll_frame.pack(side=TOP, fill=BOTH, expand=1)
    paframe_left.pack(side=LEFT, fill=BOTH, expand=1, pady=10)
    paratha_label.pack(side=RIGHT)
    paframe_right.pack(side=LEFT, fill=BOTH, expand=1, pady=10)
    paratha_btn.pack(side=LEFT, padx= 20)

    #*****************lower block*****************************
    bottom_Root = Frame(root, bg="light blue", height=50)
    copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof 2020", bg="light blue", font=('arial',12,'bold'))

    bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
    copyRight.pack(pady=10)

    mainloop()

x = call_menu()