from Tkinter import *


class GUI():
    def __init__(self,master,control):
        self.control = control
        b = Button(master, text= "Hola", command = lambda:self.a())
        b.pack()
    def a(self):
        self.control.action()
