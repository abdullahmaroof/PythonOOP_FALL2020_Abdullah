from tkinter import *
from PIL import ImageTk, Image
from Final_Project.voice_system import voice_bill
from random import *


def call_bill():
    root = Toplevel()


    root.geometry("800x520")
    root.title('Online Food Order System')
    root.iconbitmap(r'buy_online_5Wq_icon.ico')
    #*****************upper block*****************************
    upper_Root = Frame(root, bg="light blue", height=100)
    title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial', 28, 'bold', 'underline'))

    upper_Root.pack(side=TOP, fill=BOTH, expand=1)
    title.pack(pady=30)

    #*****************center block*****************************
    center_Root = Frame(root, bg="gray92", height=400)
    top_center = Frame(center_Root, bg="gray92", height=140)
    pic = Image.open("shopping-bag.png")
    resized = pic.resize((150, 100), Image.ANTIALIAS)
    mypic = ImageTk.PhotoImage(resized)
    image_top_center = Label(top_center, image = mypic)
    center_center = Frame(center_Root, bg="gray92", height=80)
    sub_title = Label(center_center, text="Bill", bg="gray92", font=('arial',20,'underline','bold'))
    bottom_center = Frame(center_Root, bg="white", height=150)
    top_bcenter = Frame(bottom_center, bg="white", height=30)
    rand_value = randint(1000, 4000)
    bill_no = Label(top_bcenter, text="Bill # "+str(rand_value), bg="white", font=('arial',14,'bold'))
    details_bcenter = Frame(bottom_center, bg="white", height=120)
    food_name = Label(details_bcenter, text="Food: ", bg="white", font=('arial',12), anchor=E)


    center_Root.pack(side=TOP, fill=BOTH, expand=1)
    top_center.pack(side=TOP, fill=BOTH, expand=1)
    image_top_center.pack(pady=20)
    center_center.pack(side=TOP, fill=BOTH, expand=1)
    sub_title.pack(pady=10)
    bottom_center.pack(side=TOP, fill=BOTH, expand=1, padx=40, pady=10)
    top_bcenter.pack(side=TOP, fill=BOTH, expand=1)
    bill_no.pack()
    details_bcenter.pack(side=TOP, fill=BOTH, expand=1)
    food_name.pack(side=TOP, pady=5, padx= 20)


    #*****************bottom block*****************************
    bottom_Root = Frame(root, bg="light blue", height=50)
    copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof 2020", bg="light blue", font=('arial',12,'bold'))

    bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
    copyRight.pack(pady=10)
    voice_bill.wishme()
    mainloop()

@staticmethod
def get_billrecord():
    class spizza_chfajita:
        def __init__(self):
            self.food = "Pizza"
            self.flavour = "Chicken Fajita"
            self.price = 300
            self.note = "Your order will be serve in 20 min. Thank you!!!"
    class mpizza_chfajita:
        def __init__(self):
            self.food = "Pizza"
            self.flavour = "Chicken Fajita"
            self.price = 500
            self.note = "Your order will be serve in 20 min. Thank you!!!"

obj = call_bill()