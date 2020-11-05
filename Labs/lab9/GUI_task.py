from tkinter import *

root = Tk()

#******************************TOP Root********************

upper_root = Frame(root, bg="light slate gray", height=125)
button_open = Button(upper_root, text ="Open", width= 20)
button_edit = Button(upper_root, text ="Edit", width= 20)
button_view = Button(upper_root, text = "View", width= 20)


button_open.pack(side = LEFT, padx = 10, pady = 10)
button_edit.pack(side = LEFT, padx = 10, pady = 10)
button_view.pack(side = LEFT, padx = 10, pady = 10)


upper_root.pack(side=TOP, fill=X)

#******************************center Root********************

center_root = Frame(root, bg="White", height= 700)
left_center_root= Frame(center_root, bg="light grey", width=250, height=700)
box_leftc_root = Frame(left_center_root, width= 250, bg="light grey", height=700)
button_PROJECT = Button(box_leftc_root, text ="Project", width= 20)
button_commit = Button(box_leftc_root, text ="Commit", width= 20)
button_pullrequest = Button(box_leftc_root, text = "Pull Request", width= 20)


center_root.pack(fill=BOTH, side=TOP, expand=1)
left_center_root.pack(side=LEFT, fill=BOTH)
box_leftc_root.pack(side=TOP, fill=X, expand=1)
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