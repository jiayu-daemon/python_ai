from tkinter import *
time1 = 0

def xin1():
	global l,c1,time1
	if time1 % 2 == 0:
		time1 += 1
		l['text'] = "Cancel"
	else:
		time1 += 1
		l['text'] = "Choose"

root = Tk()
c1 = Checkbutton(root, text = "my button", command = xin1)
c1.pack()
l = Label(root,text = " ")
l.pack()
root.mainloop()