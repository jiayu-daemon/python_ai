from tkinter import *
def xinlabel():
	global xinlabel
	s = Label(xin, text = "I Love Python")
	s.pack()

	
xin = Tk()
b1 = Button(xin, text = "xin ge", command = xinlabel)
b1.pack()
xin.mainloop()