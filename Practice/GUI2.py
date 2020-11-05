from tkinter import *


def doNothing():
    print("Click is Working Here")

#**************************************** Code for Menu Bar ****************************************#

root = Tk()
mainMenu = Menu(root)

root.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "New Project", command = doNothing)
fileMenu.add_command(label = "Open Project", command = doNothing)
fileMenu.add_command(label = "Save Project", command = doNothing)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = doNothing)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Copy", command = doNothing)
editMenu.add_command(label = "Cut", command = doNothing)
editMenu.add_command(label = "Paste", command = doNothing)
editMenu.add_separator()
editMenu.add_command(label = "Undo", command = doNothing)
editMenu.add_command(label = "Redo", command = doNothing)

#**************************************** Code for Tool Bar ****************************************#

toolbar = Frame(root, bg = "grey")

buttonCopy = Button(toolbar, text = "Copy", command = doNothing)
buttonCut = Button(toolbar, text = "Cut", command = doNothing)
buttonPaste = Button(toolbar, text = "Paste", command = doNothing)
buttonUndo = Button(toolbar, text = "Undo", command = doNothing)
buttonRedo = Button(toolbar, text = "Redo", command = doNothing)
buttonBold = Button(toolbar, text = "Bold", command = doNothing)
buttonItalic = Button(toolbar, text = "Italic", command = doNothing)
buttonUnderline = Button(toolbar, text = "Underline", command = doNothing)
buttonPrint = Button(toolbar, text = "Print", command = doNothing)

buttonCopy.pack(side = LEFT, padx = 2, pady = 2)
buttonCut.pack(side = LEFT, padx = 2, pady = 2)
buttonPaste.pack(side = LEFT, padx = 2, pady = 2)
buttonUndo.pack(side = LEFT, padx = 2, pady = 2)
buttonRedo.pack(side = LEFT, padx = 2, pady = 2)
buttonBold.pack(side = LEFT, padx = 2, pady = 2)
buttonItalic.pack(side = LEFT, padx = 2, pady = 2)
buttonUnderline.pack(side = LEFT, padx = 2, pady = 2)
buttonPrint.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)

#**************************************** Code for Status Bar ****************************************#

status = Label(root, text = "Preparing to do nothing...", bd = 1, relief=SUNKEN, anchor = W)
status.pack(side=BOTTOM, fill = X)

root.mainloop()