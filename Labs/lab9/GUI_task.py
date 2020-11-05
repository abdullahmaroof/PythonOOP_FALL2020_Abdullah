from tkinter import *

root = Tk()

def open():
    print("Open new file")

def edit():
    print("Edit this python file")

def view():
    print("View more options")

def project():
    print("See your created project")

def commit():
    print("Commit your project")


def pullreq():
    print("See your pull request here")

#******************************TOP Root********************

upper_root = Frame(root, bg="light slate gray", height=125)
button_open = Button(upper_root, text ="Open", width= 20, command= open)
button_edit = Button(upper_root, text ="Edit", width= 20, command= edit)
button_view = Button(upper_root, text = "View", width= 20, command= view)

upper_root.pack(side=TOP, fill=X)
button_open.pack(side = LEFT, padx = 10, pady = 10)
button_edit.pack(side = LEFT, padx = 10, pady = 10)
button_view.pack(side = LEFT, padx = 10, pady = 10)




#******************************center Root********************

center_root = Frame(root, bg="White", height= 700)
left_center_root= Frame(center_root, bg="light grey", width=250, height=700)
box_leftc_root1 = Frame(left_center_root, width= 250, bg="light grey")
box_leftc_root2 = Frame(left_center_root, width= 250, bg="light grey")
box_leftc_root3 = Frame(left_center_root, width= 250, bg="light grey")
button_PROJECT = Button(box_leftc_root1, text ="Project", width= 20, command= project)
button_commit = Button(box_leftc_root2, text ="Commit", width= 20, command= commit)
button_pullrequest = Button(box_leftc_root3, text = "Pull Request", width= 20, command= pullreq)


center_root.pack(fill=BOTH, side=TOP, expand=1)
left_center_root.pack(side=LEFT, fill=BOTH)
box_leftc_root1.pack(side=TOP, fill=X, expand=1)
box_leftc_root2.pack(side=TOP, fill=X, expand=1)
box_leftc_root3.pack(side=TOP, fill=X, expand=1)
button_PROJECT.pack(side = TOP, padx = 5, pady = 5, expand=1)
button_commit.pack(side = TOP, padx = 5, pady = 5, expand=1)
button_pullrequest.pack(side = TOP, padx = 5, pady = 5, expand=1)

#******************************BOTTOM Root********************

lower_root = Frame(root, bg="light slate gray", height=125)
button_run = Button(lower_root, text ="Run", width= 20)
button_todo = Button(lower_root, text ="TODO", width= 20)
button_problem = Button(lower_root, text = "Problems", width= 20)
lower_root.pack(side=BOTTOM, fill=X)
button_run.pack(side = LEFT, padx = 30, pady = 40)
button_todo.pack(side = LEFT, padx = 30, pady = 40)
button_problem.pack(side = LEFT, padx = 30, pady = 40)

mainloop()