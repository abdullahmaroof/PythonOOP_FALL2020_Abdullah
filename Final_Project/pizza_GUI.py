from tkinter import *
from PIL import ImageTk, Image
from Final_Project.voice_system import voice_pizza
def call_pizzamenu():
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
    pic = Image.open("pizza.PNG")
    resized = pic.resize((150, 100), Image.ANTIALIAS)
    mypic = ImageTk.PhotoImage(resized)
    image_top_center = Label(top_center, image = mypic)

    #*********center-center pack*****
    center_center = Frame(root, bg="white", height=420)
    subtitle_frame = Frame(center_center, bg="white", height=50)
    subtitle_label = Label(subtitle_frame, text="Pizza Menu", font=('arial',16,'bold','underline'), bg="white")
    #headings
    heading_frame = Frame(center_center, bg="white", height=20)
    name_frame = Frame(heading_frame, bg="white", height=20)
    name_label = Label(name_frame, text="Flavour", font=('arial',12,'bold'), bg="white")
    small_frame = Frame(heading_frame, bg="white", height=20)
    small_label = Label(small_frame, text="Small 5\"", font=('arial',12,'bold'), bg="white")
    medium_frame = Frame(heading_frame, bg="white", height=20)
    medium_label = Label(medium_frame, text="Medium 8\"", font=('arial',12,'bold'), bg="white")
    large_frame = Frame(heading_frame, bg="white", height=20)
    large_label = Label(large_frame, text="Large 13\"", font=('arial',12,'bold'), bg="white")


    #chicken fajita pizza
    chfajita_frame = Frame(center_center, bg="white", height=50)
    chfname_frame = Frame(chfajita_frame, bg="white", height=30)
    chfname_label = Label(chfname_frame, text="Chicken Fajita", font=('arial',12,'bold'), bg="white")
    chfsmall_frame = Frame(chfajita_frame, bg="white", height=30)
    chfsmall_btn = Button(chfsmall_frame,  text="300 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    chfmedium_frame = Frame(chfajita_frame, bg="white", height=30)
    chfmedium_btn = Button(chfmedium_frame,  text="500 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    chflarge_frame = Frame(chfajita_frame, bg="white", height=30)
    chflarge_btn = Button(chflarge_frame,  text="800 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

    #peeri peeri pizza
    peeripeeri_frame = Frame(center_center, bg="green", height=50)
    peeriname_frame = Frame(peeripeeri_frame, bg="white", height=30)
    peeriname_label = Label(peeriname_frame, text=" Peeri     Peeri ", font=('arial',12,'bold'), bg="white")
    peerismall_frame = Frame(peeripeeri_frame, bg="white", height=30)
    peerismall_btn = Button(peerismall_frame,  text="350 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    peerimedium_frame = Frame(peeripeeri_frame, bg="white", height=30)
    peerimedium_btn = Button(peerimedium_frame,  text="600 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    peerilarge_frame = Frame(peeripeeri_frame, bg="white", height=30)
    peerilarge_btn = Button(peerilarge_frame,  text="900 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

    #mexico pizza
    mexico_frame = Frame(center_center, bg="blue", height=50)
    mexiconame_frame = Frame(mexico_frame, bg="white", height=30)
    mexiconame_label = Label(mexiconame_frame, text="SmokeMexico", font=('arial',12,'bold'), bg="white")
    mexicosmall_frame = Frame(mexico_frame, bg="white", height=30)
    mexicosmall_btn = Button(mexicosmall_frame,  text="500 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    mexicomedium_frame = Frame(mexico_frame, bg="white", height=30)
    mexicomedium_btn = Button(mexicomedium_frame,  text="800 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    mexicolarge_frame = Frame(mexico_frame, bg="white", height=30)
    mexicolarge_btn = Button(mexicolarge_frame,  text="1100 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

    #cheese pizza
    cheese_frame = Frame(center_center, bg="orange", height=50)
    cheesename_frame = Frame(cheese_frame, bg="white", height=30)
    cheesename_label = Label(cheesename_frame, text="Cheese  Fajita", font=('arial',12,'bold'), bg="white")
    cheesesmall_frame = Frame(cheese_frame, bg="white", height=30)
    cheesesmall_btn = Button(cheesesmall_frame,  text="320 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    cheesemedium_frame = Frame(cheese_frame, bg="white", height=30)
    cheesemedium_btn = Button(cheesemedium_frame,  text="500 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    cheeselarge_frame = Frame(cheese_frame, bg="white", height=30)
    cheeselarge_btn = Button(cheeselarge_frame,  text="950 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

    #BBQ pizza
    BBQ_frame = Frame(center_center, bg="purple", height=50)
    BBQname_frame = Frame(BBQ_frame, bg="white", height=30)
    BBQname_label = Label(BBQname_frame, text="Thikka BarBQ", font=('arial',12,'bold'), bg="white")
    BBQsmall_frame = Frame(BBQ_frame, bg="white", height=30)
    BBQsmall_btn = Button(BBQsmall_frame,  text="350 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    BBQmedium_frame = Frame(BBQ_frame, bg="white", height=30)
    BBQmedium_btn = Button(BBQmedium_frame,  text="600 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    BBQlarge_frame = Frame(BBQ_frame, bg="white", height=30)
    BBQlarge_btn = Button(BBQlarge_frame,  text="1000 RS", width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")



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
    small_frame.pack(side=LEFT, fill=BOTH, expand=1)
    small_label.pack()
    medium_frame.pack(side=LEFT, fill=BOTH, expand=1)
    medium_label.pack()
    large_frame.pack(side=LEFT, fill=BOTH, expand=1)
    large_label.pack()

    #ch fajita pack
    chfajita_frame.pack(side=TOP, fill=BOTH, expand=1)
    chfname_frame.pack(side=LEFT, fill=BOTH, expand=1)
    chfname_label.pack(pady=10)
    chfsmall_frame.pack(side=LEFT, fill=BOTH, expand=1)
    chfsmall_btn.pack(pady=10)
    chfmedium_frame.pack(side=LEFT, fill=BOTH, expand=1)
    chfmedium_btn.pack(pady=10)
    chflarge_frame.pack(side=LEFT, fill=BOTH, expand=1)
    chflarge_btn.pack(pady=10)

    #peeri peeri pack
    peeripeeri_frame.pack(side=TOP, fill=BOTH, expand=1)
    peeriname_frame.pack(side=LEFT, fill=BOTH, expand=1)
    peeriname_label.pack(pady=10)
    peerismall_frame.pack(side=LEFT, fill=BOTH, expand=1)
    peerismall_btn.pack(pady=10)
    peerimedium_frame.pack(side=LEFT, fill=BOTH, expand=1)
    peerimedium_btn.pack(pady=10)
    peerilarge_frame.pack(side=LEFT, fill=BOTH, expand=1)
    peerilarge_btn.pack(pady=10)

    #mexico pack
    mexico_frame.pack(side=TOP, fill=BOTH, expand=1)
    mexiconame_frame.pack(side=LEFT, fill=BOTH, expand=1)
    mexiconame_label.pack(pady=10)
    mexicosmall_frame.pack(side=LEFT, fill=BOTH, expand=1)
    mexicosmall_btn.pack(pady=10)
    mexicomedium_frame.pack(side=LEFT, fill=BOTH, expand=1)
    mexicomedium_btn.pack(pady=10)
    mexicolarge_frame.pack(side=LEFT, fill=BOTH, expand=1)
    mexicolarge_btn.pack(pady=10)

    #cheese pack
    cheese_frame.pack(side=TOP, fill=BOTH, expand=1)
    cheesename_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cheesename_label.pack(pady=10)
    cheesesmall_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cheesesmall_btn.pack(pady=10)
    cheesemedium_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cheesemedium_btn.pack(pady=10)
    cheeselarge_frame.pack(side=LEFT, fill=BOTH, expand=1)
    cheeselarge_btn.pack(pady=10)


    #bbq pack
    BBQ_frame.pack(side=TOP, fill=BOTH, expand=1)
    BBQname_frame.pack(side=LEFT, fill=BOTH, expand=1)
    BBQname_label.pack(pady=10)
    BBQsmall_frame.pack(side=LEFT, fill=BOTH, expand=1)
    BBQsmall_btn.pack(pady=10)
    BBQmedium_frame.pack(side=LEFT, fill=BOTH, expand=1)
    BBQmedium_btn.pack(pady=10)
    BBQlarge_frame.pack(side=LEFT, fill=BOTH, expand=1)
    BBQlarge_btn.pack(pady=10)



    #*****************bottom block*****************************
    bottom_Root = Frame(root, bg="light blue", height=50)
    copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof 2020", bg="light blue", font=('arial',12,'bold'))

    bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
    copyRight.pack()
    voice_pizza.wishme()
    mainloop()