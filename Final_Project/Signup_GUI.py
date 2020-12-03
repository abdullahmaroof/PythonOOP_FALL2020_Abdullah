from tkinter import *
from PIL import ImageTk, Image
from Final_Project.login_GUI import signin
from Final_Project.voice_system import voice_signup
from tkinter import ttk, messagebox
from sqlite3 import *
con = connect("userdata.db")

def call_signup():
    class gui_signup:
        def __init__(self, root):
            self.root = root
            root.geometry("800x690")
            root.title('Online Food Order System')
            root.iconbitmap(r'buy_online_5Wq_icon.ico')
            #*****************upper block*****************************
            upper_Root = Frame(root, bg="light blue", height=100)
            title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial',28,'bold','underline'))

            upper_Root.pack(side=TOP, fill=BOTH, expand=1)
            title.pack(pady=30)

            #*****************center block*****************************
            center_Root = Frame(root, bg="gray92", height=490)
            top_center = Frame(center_Root, bg="gray92", height=140)
            self.pic = Image.open("shopping-bag.png")
            self.resized = self.pic.resize((150, 100), Image.ANTIALIAS)
            self.mypic = ImageTk.PhotoImage(self.resized)
            image_top_center = Label(top_center, image = self.mypic)
            center_center = Frame(center_Root, bg="gray92", height=80)
            sub_title = Label(center_center, text="SIGN UP", bg="gray92", font=('arial',20,'underline','bold'))
            bottom_center = Frame(center_Root, bg="gray92", height=280)
            top_botcenter = Frame(bottom_center, bg="gray92", height=200)
            left_top_bot = Frame(top_botcenter, height=240, bg="gray92")
            firstname_label = Label(left_top_bot, text="First Name:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
            lastname_label = Label(left_top_bot, text="Second Name:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
            email_label = Label(left_top_bot, text="Email id:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
            age_label = Label(left_top_bot, text="Your Age:  ", font=('arial', 12, 'bold'), anchor=E, bg="gray92")
            pass_label = Label(left_top_bot, text="Password:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
            con_pass_label = Label(left_top_bot, text="Confirm Password:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
            right_top_bot = Frame(top_botcenter, height=250, bg="gray92")
            p1_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
            p2_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
            p3_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
            p4_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
            p5_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
            p6_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
            self.firstname_box = Entry(p1_right_top_bot, width=25)
            self.lastname_box = Entry(p2_right_top_bot, width=25)
            self.email_box = Entry(p3_right_top_bot, width=25)
            self.age_box = ttk.Combobox(p4_right_top_bot, width=10, state="readonly", justify=CENTER)
            self.age_box['values']=("Select Age","40","39","38","37","36","35","34","33","32","31","30","29","28","27","26","25","24","23","22","21","20","19","18","17","16")
            self.pass_box = Entry(p5_right_top_bot, width=25)
            self.con_pass_box = Entry(p6_right_top_bot, width=25)
            bottom_botcenter = Frame(bottom_center, bg="gray92", height=80)
            login_but = Button(bottom_botcenter, text="LOGIN", command= lambda : self.enter_value(), width=20, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")


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
            age_label.pack(pady=10, fill=BOTH, expand=1)
            pass_label.pack(pady=10, fill=BOTH, expand=1)
            con_pass_label.pack(pady=10, fill=BOTH, expand=1)
            right_top_bot.pack(side=LEFT, fill=BOTH, expand=1)
            p1_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
            p2_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
            p3_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
            p4_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
            p5_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
            p6_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
            self.firstname_box.pack(side=LEFT, pady=10)
            self.lastname_box.pack(side=LEFT, pady=10)
            self.email_box.pack(side=LEFT, pady=10)
            self.age_box.pack(side=LEFT, pady=10)
            self.age_box.current(0)
            self.pass_box.pack(side=LEFT, pady=10)
            self.con_pass_box.pack(side=LEFT, pady=10)
            bottom_botcenter.pack(side=TOP, fill=BOTH, expand=1)
            login_but.pack(pady=20)


            #*****************bottom block*****************************
            bottom_Root = Frame(root, bg="light blue", height=50)
            copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof 2020", bg="light blue", font=('arial',12,'bold'))

            bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
            copyRight.pack(pady=10)
        def enter_value(self):
            if self.firstname_box.get() == "" or self.lastname_box.get() == "" or self.email_box.get() == "" or self.age_box.get() == "Select Age" or self.pass_box.get() == "" or self.con_pass_box.get() == "":
                messagebox.showerror("ERROR","Please fill all fields", parent=self.root)
            elif self.pass_box.get() != self.con_pass_box.get():
                messagebox.showerror("Password","Please enter same password in confirm password", parent=self.root)
            else:
                try:
                    data = [self.firstname_box.get(),self.lastname_box.get(),self.email_box.get(),self.age_box.get(),self.con_pass_box.get()]
                    con = connect("userdata.db")
                    cursor = con.cursor()
                    cursor.execute("""INSERT INTO user_data (first_name,last_name,email_id,age,password) VALUES (?,?,?,?,?,)""",data)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Successfull", "Thank you!!! for signup", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)
                messagebox.showinfo("Successfull","Thank you!!! for signup", parent=self.root)
            #print(self.firstname_box.get(),self.lastname_box.get())
            #print(self.email_box.get())
            #print(self.age_box.get())
            #print(self.pass_box.get())
            #print(self.con_pass_box.get())

    root = Toplevel()
    obj = gui_signup(root)
    voice_signup.wishme()
    mainloop()