from tkinter import *
root = Tk()
root.title("我是root窗口")
l = Label(root, text = "我属于root")
l.pack()

f = Toplevel(root,width = 30, height = 20)
f.title("Toplevel")
lf = Label(f, text = "我是toplevel")
lf.pack()
root.mainloop()
