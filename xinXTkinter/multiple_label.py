from tkinter import *

root = Tk()
root.wm_title("Tkinter")
w1 = Label(root,text = "Learn tkinter",background = "green")
w2 = Label(root,text = "Learn Python", background = "red")
w3 = Label(root,text = "Be relax", background = "yellow")
w1.pack()
w2.pack()
w3.pack()
root.mainloop()