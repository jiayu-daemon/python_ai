"""
1.其实我们已经接触过 tkinter 的一种布局，就是 pack 布
局，它非常简单，我们不用做过多的设置，直接使用一个
pack 函数就可以了。
2.grid 布局： grid 可以理解为网格，或者表格，它可以把
界面设置为几行几列的网格，我们在网格里插入我们想要
的元素。这种布局的好处是不管我们如何拖动窗口，相对
位置是不会变化的，而且这种布局也超简单。
3.place 布局：它直接使用死板的位置坐标来布局，这样做
的最大的问题在于当我们向窗口添加一个新部件的时候，
又得重新测一遍数据，且我们不能随便地变大或者缩小窗
口，否则，可能会导致混乱。
"""

from tkinter import *

xin = Tk()
Label(xin, text = "账号:").grid(row = 0, sticky = W)
Entry(xin).grid(row = 0, column = 1, sticky = E)

Label(xin,text = "密码:").grid(row = 1, sticky = W)
Entry(xin).grid(row = 1, column = 1, sticky = E)

Button(xin,text = "登录").grid(row = 2, column = 1, sticky = E)
xin.mainloop()
