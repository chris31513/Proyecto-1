from Tkinter import *
import tkMessageBox

class GUI():
    def __init__(self,master,control):
        self.control = control
        b = Button(master, text= "Conectar", command = lambda:self.conecta())
        b.pack()
    def conecta(self):
        try:
            self.control.action()
        except:
            tkMessageBox.showinfo("Error al conectar", "Conexion rechazada por el host")
