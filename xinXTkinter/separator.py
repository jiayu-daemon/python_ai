"""
************分割线*******************
1.有时候，一个菜单项的各个菜单可能并不是一个类型，
有可能是两种类型，在它们中间可以插一个分割线来界定
界限。
2.插入分割线和插入正常的菜单项操作很相似，只是使用
的方法是 add_separator，该方法无需参数。
3.插入分割线效果示例（在 ruby 下面插入了一个分割线）：
"""
from tkinter import *
root = Tk()
m = Menu(root)
m2 = Menu(m)

for item in ['python','perl','php','ruby']:
	m2.add_command(label = item)

m2.add_separator()

for item in ['java','c++','c']:
	m2.add_command(label = item)

m.add_cascade(label = "lan", menu = m2)
root['menu'] = m
root.mainloop()