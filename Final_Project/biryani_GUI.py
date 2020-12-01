from tkinter import *
from PIL import ImageTk, Image

def call_biryanimenu():
    root = Toplevel()

    root.geometry("800x650")
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
    pic = Image.open("biryani.PNG")
    resized = pic.resize((150, 100), Image.ANTIALIAS)
    mypic = ImageTk.PhotoImage(resized)
    image_top_center = Label(top_center, image = mypic)

    #*********center-center pack*****
    center_center = Frame(root, bg="white", height=420)
    subtitle_frame = Frame(center_center, bg="white", height=50)
    subtitle_label = Label(subtitle_frame, text="Biryani Menu", font=('arial',16,'bold','underline'), bg="white")
    #headings
    heading_frame = Frame(center_center, bg="white", height=20)
    name_frame = Frame(heading_frame, bg="white", height=20)
    name_label = Label(name_frame, text="Flavour", font=('arial',12,'bold'), bg="white")
    price_frame = Frame(heading_frame, bg="white", height=20)
    price_label = Label(price_frame, text="Prices", font=('arial',12,'bold'), bg="white")
    bcold_frame = Frame(heading_frame, bg="white", height=20)
    bcold_label = Label(bcold_frame, text="With Drink", font=('arial',12,'bold'), bg="white")
    bcolds_frame = Frame(heading_frame, bg="white", height=20)
    bcolds_label = Label(bcolds_frame, text="With Salt", font=('arial',12,'bold'), bg="white")


    #zinger biryani
    zb_frame = Frame(center_center, bg="white", height=50)
    zbname_frame = Frame(zb_frame, bg="white", height=30)
    zbname_label = Label(zbname_frame, text="Zinger Biryani", font=('arial',12,'bold'), bg="white")
    zbprice_frame = Frame(zb_frame, bg="white", height=30)
    zbprice_btn = Button(zbprice_frame,  text="300 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    zbcold_frame = Frame(zb_frame, bg="white", height=30)
    zbcold_btn = Button(zbcold_frame,  text="350 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    zbcolds_frame = Frame(zb_frame, bg="white", height=30)
    zbcolds_btn = Button(zbcolds_frame,  text="400 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

    #beef biryani
    bbir_frame = Frame(center_center, bg="white", height=50)
    bbirname_frame = Frame(bbir_frame, bg="white", height=30)
    bbirname_label = Label(bbirname_frame, text="Beef   Biryani", font=('arial',12,'bold'), bg="white")
    bbirprice_frame = Frame(bbir_frame, bg="white", height=30)
    bbirprice_btn = Button(bbirprice_frame,  text="500 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    bbircold_frame = Frame(bbir_frame, bg="white", height=30)
    bbircold_btn = Button(bbircold_frame,  text="550 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    bbircolds_frame = Frame(bbir_frame, bg="white", height=30)
    bbircolds_btn = Button(bbircolds_frame,  text="600 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

    #Chicken biryani
    cbir_frame = Frame(center_center, bg="white", height=50)
    cbirname_frame = Frame(cbir_frame, bg="white", height=30)
    cbirname_label = Label(cbirname_frame, text="Chicken Biry.", font=('arial',12,'bold'), bg="white")
    cbirprice_frame = Frame(cbir_frame, bg="white", height=30)
    cbirprice_btn = Button(cbirprice_frame,  text="250 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    cbircold_frame = Frame(cbir_frame, bg="white", height=30)
    cbircold_btn = Button(cbircold_frame,  text="300 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    cbircolds_frame = Frame(cbir_frame, bg="white", height=30)
    cbircolds_btn = Button(cbircolds_frame,  text="350 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

    #Chinise Rics
    cricebir_frame = Frame(center_center, bg="white", height=50)
    cricebirname_frame = Frame(cricebir_frame, bg="white", height=30)
    cricebirname_label = Label(cricebirname_frame, text="Chinise Rice", font=('arial',12,'bold'), bg="white")
    cricebirprice_frame = Frame(cricebir_frame, bg="white", height=30)
    cricebirprice_btn = Button(cricebirprice_frame,  text="200 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    cricebircold_frame = Frame(cricebir_frame, bg="white", height=30)
    cricebircold_btn = Button(cricebircold_frame,  text="250 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    cricebircolds_frame = Frame(cricebir_frame, bg="white", height=30)
    cricebircolds_btn = Button(cricebircolds_frame,  text="300 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

    #BBQ biryani
    bbbir_frame = Frame(center_center, bg="white", height=50)
    bbbirname_frame = Frame(bbbir_frame, bg="white", height=30)
    bbbirname_label = Label(bbbirname_frame, text="BBQ Biryani", font=('arial',12,'bold'), bg="white")
    bbbirprice_frame = Frame(bbbir_frame, bg="white", height=30)
    bbbirprice_btn = Button(bbbirprice_frame,  text="600 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    bbbircold_frame = Frame(bbbir_frame, bg="white", height=30)
    bbbircold_btn = Button(bbbircold_frame,  text="650 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    bbbircolds_frame = Frame(bbbir_frame, bg="white", height=30)
    bbbircolds_btn = Button(bbbircolds_frame,  text="700 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")



    center_Root.pack(side=TOP, fill=BOTH, expand=1)

    #*********top-center pack*****
    top_center.pack(side=TOP, fill=BOTH, expand=1)
    image_top_center.pack(pady=20)


    #********center-center pack*******
    center_center.pack(side=TOP, fill=BOTH, expand=1, pady=10, padx=20)
    subtitle_frame.pack(side=TOP, fill=BOTH, expand=1)
    subtitle_label.pack(pady=10)
    #heading pack
    heading_frame.pack(side=TOP, fill=BOTH, expand=1, padx= 10)
    name_frame.pack(side=LEFT, fill=BOTH, expand=1)
    name_label.pack()
    price_frame.pack(side=LEFT, fill=BOTH, expand=1)
    price_label.pack()
    bcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bcold_label.pack()
    bcolds_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bcolds_label.pack()

    #zinger pack
    zb_frame.pack(side=TOP, fill=BOTH, expand=1)
    zbname_frame.pack(side=LEFT, fill=BOTH, expand=1)
    zbname_label.pack(pady=10)
    zbprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
    zbprice_btn.pack(pady=10)
    zbcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
    zbcold_btn.pack(pady=10)
    zbcolds_frame.pack(side=LEFT, fill=BOTH, expand=1)
    zbcolds_btn.pack(pady=10)

    #beef pack
    bbir_frame.pack(side=TOP, fill=BOTH, expand=1)
    bbirname_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bbirname_label.pack(pady=10)
    bbirprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bbirprice_btn.pack(pady=10)
    bbircold_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bbircold_btn.pack(pady=10)
    bbircolds_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bbircolds_btn.pack(pady=10)


    #chicken pack
    cbir_frame.pack(side=TOP, fill=BOTH, expand=1)
    cbirname_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cbirname_label.pack(pady=10)
    cbirprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cbirprice_btn.pack(pady=10)
    cbircold_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cbircold_btn.pack(pady=10)
    cbircolds_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cbircolds_btn.pack(pady=10)


    #chinise rice pack
    cricebir_frame.pack(side=TOP, fill=BOTH, expand=1)
    cricebirname_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cricebirname_label.pack(pady=10)
    cricebirprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cricebirprice_btn.pack(pady=10)
    cricebircold_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cricebircold_btn.pack(pady=10)
    cricebircolds_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cricebircolds_btn.pack(pady=10)


    #BBQ pack
    bbbir_frame.pack(side=TOP, fill=BOTH, expand=1)
    bbbirname_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bbbirname_label.pack(pady=10)
    bbbirprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bbbirprice_btn.pack(pady=10)
    bbbircold_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bbbircold_btn.pack(pady=10)
    bbbircolds_frame.pack(side=LEFT, fill=BOTH, expand=1)
    bbbircolds_btn.pack(pady=10)


    #*****************bottom block*****************************
    bottom_Root = Frame(root, bg="light blue", height=50)
    copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof 2020", bg="light blue", font=('arial',12,'bold'))

    bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
    copyRight.pack()

    mainloop()