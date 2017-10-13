"""
************弹出菜单*****************
1.弹出菜单又叫“上下文菜单”，也叫“右键菜单”，它
通常是鼠标单击右键产生的菜单，因此会有“右键菜单”
的说法。
2.其实很多界面库里面都是给出了弹出菜单的简单的制作
方法的，但是 tkinter 里面我们却只能使用比较原始的事
件绑定的方式去做。
3.大体思路就是：我们先新建一个菜单，然后向菜单项中
添加各种功能，最后我们监听鼠标右键消息，如果是鼠标
右键被单击，此时可以根据需要判断下鼠标位置来确定是
哪个弹出菜单被弹出，然后使用 Menu 类的 pop 方法来弹出
菜单。
4.大体思路就是如此，至于具体的细节，让我们到代码实
战中一探究竟。
************提前说明*************
1.Menu 类里面有一个 post 方法，它接收两个参数，即 x 和
y 坐标，它会在相应的位置弹出菜单。
2.还记得用 bind 方法来绑定事件吗?而且要记得鼠标右键
是用的<Button-3>。
3.此处利用了 Menu 的 post 方法，还有 bind 方法，一定要
记住鼠标右键的事件名称，这些用多了之后自然能记住。
************弹出式菜单实战*************
"""
from tkinter import *

def xin():
	global root
	Label(root,text = "I love python").pack()

root = Tk()
menubar = Menu(root)

for x in ['vb','c','java','php']:
	menubar.add_command(label = x)
menubar.add_command(label = 'python', command = xin)

def pop(event):
	menubar.post(event.x_root,event.y_root)

root.bind("<Button-3>",pop)
root.mainloop()


