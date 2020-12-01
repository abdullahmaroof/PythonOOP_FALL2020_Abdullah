from tkinter import *
from PIL import ImageTk, Image
from Final_Project.login_GUI import signin

def call_signup():
    root = Toplevel()

    root.geometry("800x650")
    root.title('Online Food Order System')
    root.iconbitmap(r'buy_online_5Wq_icon.ico')
    #*****************upper block*****************************
    upper_Root = Frame(root, bg="light blue", height=100)
    title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial',28,'bold','underline'))

    upper_Root.pack(side=TOP, fill=BOTH, expand=1)
    title.pack(pady=30)

    #*****************center block*****************************
    center_Root = Frame(root, bg="gray92", height=450)
    top_center = Frame(center_Root, bg="gray92", height=140)
    pic = Image.open("shopping-bag.png")
    resized = pic.resize((150, 100), Image.ANTIALIAS)
    mypic = ImageTk.PhotoImage(resized)
    image_top_center = Label(top_center, image = mypic)
    center_center = Frame(center_Root, bg="gray92", height=80)
    sub_title = Label(center_center, text="SIGN UP", bg="gray92", font=('arial',20,'underline','bold'))
    bottom_center = Frame(center_Root, bg="gray92", height=280)
    top_botcenter = Frame(bottom_center, bg="gray92", height=200)
    left_top_bot = Frame(top_botcenter, height=200, bg="gray92")
    firstname_label = Label(left_top_bot, text="First Name:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
    lastname_label = Label(left_top_bot, text="Second Name:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
    email_label = Label(left_top_bot, text="Email id:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
    pass_label = Label(left_top_bot, text="Password:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
    con_pass_label = Label(left_top_bot, text="Confirm Password:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
    right_top_bot = Frame(top_botcenter, height=250, bg="gray92")
    p1_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
    p2_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
    p3_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
    p4_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
    p5_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
    firstname_box = Entry(p1_right_top_bot, width=25)
    lastname_box = Entry(p2_right_top_bot, width=25)
    email_box = Entry(p3_right_top_bot, width=25)
    pass_box = Entry(p4_right_top_bot, width=25)
    con_pass_box = Entry(p5_right_top_bot, width=25)
    bottom_botcenter = Frame(bottom_center, bg="gray92", height=80)
    login_but = Button(bottom_botcenter, text="LOGIN", command= lambda : signin(), width=20, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")


    center_Root.pack(side=TOP, fill=BOTH, expand=1)
    top_center.pack(side=TOP, fill=BOTH, expand=1)
    image_top_center.pack(pady=20)
    center_center.pack(side=TOP, fill=BOTH, expand=1)
    sub_title.pack(pady=10)
    bottom_center.pack(side=TOP, fill=BOTH, expand=1)
    top_botcenter.pack(side=TOP, fill=BOTH, expand=1)
    left_top_bot.pack(side=LEFT, fill=BOTH, expand=1)
    firstname_label.pack(pady=10, fill=BOTH, expand=1)
    lastname_label.pack(pady=10, fill=BOTH, expand=1)
    email_label.pack(pady=10, fill=BOTH, expand=1)
    pass_label.pack(pady=10, fill=BOTH, expand=1)
    con_pass_label.pack(pady=10, fill=BOTH, expand=1)
    right_top_bot.pack(side=LEFT, fill=BOTH, expand=1)
    p1_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
    p2_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
    p3_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
    p4_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
    p5_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
    firstname_box.pack(side=LEFT, pady=10)
    lastname_box.pack(side=LEFT, pady=10)
    email_box.pack(side=LEFT, pady=10)
    pass_box.pack(side=LEFT, pady=10)
    con_pass_box.pack(side=LEFT, pady=10)
    bottom_botcenter.pack(side=TOP, fill=BOTH, expand=1)
    login_but.pack(pady=20)


    #*****************bottom block*****************************
    bottom_Root = Frame(root, bg="light blue", height=50)
    copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof 2020", bg="light blue", font=('arial',12,'bold'))

    bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
    copyRight.pack(pady=10)

    mainloop()