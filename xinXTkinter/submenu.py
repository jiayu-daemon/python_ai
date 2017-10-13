"""
************有子菜单的情况*************
1.如果有子菜单，则情况稍微复杂点，这个时候，我们需
要使用 add_cascade， cascade 可以理解为“级联”，即它
的作用只是为了引出后面的菜单。
2.add_cascade 的一个很重要的属性就是 menu 属性，它指
明了要把那个菜单级联到该菜单项上，当然，还必不可少
的就是 label 属性，用于指定该菜单项的名称。
3.我们先新建一个 Menu 的实例，然后使用 add_command 来
添加菜单项，这样等该菜单建立完毕， 我们要把它作为另
一个菜单项的子菜单，就需要使用 add_cascade 方法。
"""

from tkinter import *
root = Tk()
menubar = Menu(root)

fmenu = Menu(menubar)
for item in['新建','打开','保存','另存为']:
	fmenu.add_command(label = item)

emenu = Menu(menubar)
for item in['复制','粘贴','剪切']:
	emenu.add_command(label = item)

vmenu = Menu(menubar)
for item in['默认视图','新式视图']:
	vmenu.add_command(label = item)

amenu = Menu(menubar)
for item in['版权信息','其他说明']:
	amenu.add_command(label = item)

menubar.add_cascade(label = "文件", menu = fmenu)
menubar.add_cascade(label = "编辑", menu = emenu)
menubar.add_cascade(label = "视图",menu = vmenu)
menubar.add_cascade(label = "关于",menu = amenu)

root['menu'] = menubar
root.mainloop()