"""
**************checkbutton 与 radiobutton********
1.checkbutton 原本是指“复选按钮”， radiobutton 原本
是指“单选按钮”。
2.单选按钮与复选按钮是相对来说的，即在这一组中，单
选按钮中只能有一个是被选定的，即一个人的性别是女的，
就一定不是男的，但是复选按钮对应的情况则是可以有多
个同时被选定，比如一个人即可以喜欢篮球，也可以喜欢
足球，还有可能喜欢乒乓球，等等。
3.在菜单中，也有类似的概念，即单选菜单和复选菜单。
它们分别用 add_radiobutton 和 add_checkbutton 来分别
添加。
4.这两种菜单都是如果一旦被选定，那么前面会有一个类
似于对号的标记出现， checkbutton 可以多个同时被选定，
但是 radiobutton 却只能被选定一个，即这个被选定了，
会自动取消前一个的选定。
"""

from tkinter import *
root = Tk()
m = Menu(root)

m2 = Menu(m)
for item in['python','perl','php','ruby']:
	m2.add_checkbutton(label = item)
	
m2.add_separator()

for item in ['java','c++','c']:
	m2.add_radiobutton(label = item)

m.add_cascade(label = "lan", menu = m2)

root['menu'] = m
root.mainloop()