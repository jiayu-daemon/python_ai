#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program shows a simple
menu. It has one action, which
will terminate the program, when
selected. 

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com
"""

from tkinter import Tk, Frame, Menu

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("Simple menu")
        
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        

    def onExit(self):
        
        self.quit()


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  