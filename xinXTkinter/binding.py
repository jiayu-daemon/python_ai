from tkinter import *
def xinlabel(event):
	global xinlabel
	s = Label(xin, text = "I Love Python")
	s.pack()

def oklabel(event):
	global oklabel
	s = Label(xin, text = "I am OK")
	s.pack()

xin = Tk()
b1 = Button(xin, text = "Python")
b1.bind("<Button-1>", xinlabel)
b1['width'] = 20
b1['height'] = 4
b1.pack()

b2 = Button(xin, text = "OK")
b2.bind("<Button-1>",oklabel)
b2['width'] = 20
b2['background'] = 'red'
b2.pack()

xin.mainloop()

