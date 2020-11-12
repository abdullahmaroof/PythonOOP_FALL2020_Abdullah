from tkinter import *

def GUI_Creator():
    root = Tk()
    root.geometry("800x600")
    #******************Upper root**********
    upper_root = Frame(root, bg="black", height=100, width=800)
    left_upper_root = Frame(upper_root, bg="black", height=100, width=400)
    right_upper_root = Frame(upper_root, bg="white", height=100, width=400)
    p1_leftuproot = Frame(left_upper_root, bg="black", height=100)
    p2_leftuproot = Frame(left_upper_root, bg="black", height=100)
    p1_rightuproot = Frame(right_upper_root, bg="white", height=100)
    p2_rightuproot = Frame(right_upper_root, bg="white", height=100)
    label1 = Label(p1_leftuproot, text="Label-1", bg="white", font=('arial', 12, 'bold'))
    but1 = Button(p1_leftuproot, text="B1", bg="white", width=6)
    label2 = Label(p2_leftuproot, text="Label-2", bg="white", font=('arial', 12, 'bold'))
    but2 = Button(p2_leftuproot, text="B2", bg="white", width=6)
    label3 = Label(p1_rightuproot, text="Label-3", bg="gray92", font=('arial', 12, 'bold'))
    but3 = Button(p1_rightuproot, text="B3", bg="white", width=6)
    label4 = Label(p2_rightuproot, text="Label-4", bg="gray92", font=('arial', 12, 'bold'))
    but4 = Button(p2_rightuproot, text="B4", bg="white", width=6)
    upper_root.pack(side=TOP, fill=BOTH)
    left_upper_root.pack(side=LEFT, fill=BOTH)
    right_upper_root.pack(side=LEFT, fill=BOTH)
    p1_leftuproot.pack(side=LEFT, fill=BOTH, padx=70, pady=20)
    p2_leftuproot.pack(side=LEFT, fill=BOTH, padx=66, pady=20)
    p1_rightuproot.pack(side=LEFT, fill=BOTH, padx=70, pady=20)
    p2_rightuproot.pack(side=LEFT, fill=BOTH, padx=70, pady=20)
    label1.grid(row=0, column=0, pady=5)
    but1.grid(row=1,column=0)
    label2.grid(row=0, column=0, pady=5)
    but2.grid(row=1, column=0)
    label3.grid(row=0, column=0, pady=5)
    but3.grid(row=1, column=0)
    label4.grid(row=0, column=0, pady=5)
    but4.grid(row=1, column=0)

    #****************************center part********************
    center_root = Frame(root, bg="yellow", height=400)
    left_ceroot = Frame(center_root, bg="red", width=200, height=400)
    center_ceroot = Frame(center_root, bg="yellow", width=400, height=400)
    right_ceroot = Frame(center_root, bg="blue", width=200, height=400)
    frame_leftceroot = Frame(left_ceroot, bg="red", width=200, height=80)
    label5 = Label(frame_leftceroot, text = "Label-5", bg = "white", font = ('arial', 12, 'bold'))
    but5 = Button(frame_leftceroot, text="B5", bg="white", width=6)
    label8 = Label(right_ceroot, text="Label-8", bg="white", font=('arial', 12, 'bold'), anchor=W)
    center_root.pack(side=TOP, fill=BOTH)
    left_ceroot.pack(side=LEFT, fill=BOTH)
    center_ceroot.pack(side=LEFT, fill=BOTH)
    right_ceroot.pack(side=LEFT, fill=BOTH)
    frame_leftceroot.pack(side=BOTTOM, fill=BOTH, padx=80)
    label5.grid(row=0, column=0, pady=5)
    but5.grid(row=1, column=0)
    label8.pack(side=TOP, padx=58, pady=180)

    #***********************Last part***************
    bottom_root = Frame(root, bg="green", height=100, width=800)
    left_broot = Frame(bottom_root, bg="red", height=100, width=400)
    right_broot = Frame(bottom_root, bg="green", height=100, width=400)
    frame_leftbroot = Frame(left_broot, bg="red", width=400, height=100)
    frame_rightbroot = Frame(right_broot, bg="green", width=400, height=100)
    label6 = Label(frame_leftbroot, text="Label-6", bg="white", font=('arial', 12, 'bold'))
    but6 = Button(frame_leftbroot, text="B6", bg="white", width=6)
    label7 = Label(frame_rightbroot, text="Label-7", bg="white", font=('arial', 12, 'bold'))
    but7 = Button(frame_rightbroot, text="B7", bg="white", width=6)
    bottom_root.pack(side=TOP, fill=BOTH)
    left_broot.pack(side=LEFT, fill=BOTH)
    right_broot.pack(side=LEFT, fill=BOTH)
    frame_leftbroot.pack(side=RIGHT, fill=BOTH, pady=20)
    label6.pack(side=TOP, pady=5, padx=200)
    but6.pack(side=TOP)
    frame_rightbroot.pack(side=RIGHT, fill=BOTH, pady=20)
    label7.pack(side=TOP, pady=5, padx=140)
    but7.pack(side=TOP)







    mainloop()

GUI = GUI_Creator()