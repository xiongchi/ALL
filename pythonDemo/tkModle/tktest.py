# encoding=utf-8
import tkinter
from tkinter import ttk
import os

class mywin():
    def __init__(self, title, width, height, x, y):
        self.mytk = tkinter.Tk()
        self.mytk.title(title)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        strl = "%dx%d+%d+%d"%(self.width,self.height,self.x,self.y)
        self.mytk.geometry(strl)

    def input(self):
        self.entry = tkinter.Entry(self.mytk)
        self.entry.pack()
        self.button = tkinter.Button(self.mytk, text = "搜索", command = self._button_event)
        self.button.pack()

    def _button_event(self):

        inputstr = self.entry.get()

        if inputstr == "notepad":
            os.system("notepad")
        else:
            print "you are wrong"

    def tk_test(self):
        text = tkinter.Text(self.mytk)
        text.pack()

    def tree_test(self):
        tree = ttk.Treeview(self.mytk)
        tree["columns"] = ("姓名", "年龄", "身高")

        tree.column("姓名", width = 100)
        tree.column("年龄", width = 100)
        tree.column("身高", width = 100)
        tree.heading("姓名", text="姓名-name")
        tree.heading("年龄", text="年龄")
        tree.heading("身高", text="身高")

        tree.pack()


    def show(self):
        self.mytk.mainloop()

if __name__ == '__main__':
    m1 = mywin("hello", 200, 200, 200, 200)
    m1.input()
    m1.tree_test()
    m1.tk_test()

    m1.show()




