# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
#----Clase de la interfaz gráfica
class GUI():
    #----Método que construye la primer ventana que se muestra
    def __init__(self,master,control):
        self.host = StringVar()
        self.port = StringVar()
        self.control = control
        label = Label(master)
        e = Entry(label,textvariable = self.host)
        r = Entry(label, textvariable = self.port)
        e.bind('<Return>',(lambda _:self.e(e)))
        r.bind('<Return>',(lambda _:self.r(r)))
        b = Button(label, text = "Conectar", command = lambda: self.conecta(self.host,self.port,master),anchor = S)
        b.pack()
        e.pack()
        r.pack()
        label.pack()
    #----Método que define el host al que se conectará el cliente
    def e(self,e):
        self.host = e.get()
    #----Método que define el puerto al que se conectará el cliente
    def r(self,r):
        self.port = r.get()
    #----Método que abre una nueva ventana para el chat
    def identify(self,e, master):
        try:
            self.control.identify(e)
            master.destroy()
            r = Tk()
            label = Label(r)
            r.title("Chat")
            T = Text(label)
            T.pack()
            try:
                T.insert(END,self.control.recibe())
            except ValueError:
                pass
            e = Entry()
            e.bind('<Return>', (lambda _: self.control.envia(e)))
            e.pack()
            label.pack()
            r.mainloop()
        except:
            tkMessageBox.showinfo("Nombre ocupado", "Nombre ocupado")
    #----Método que llama a <action> del controlador y abre una nueva ventana para que el usuario se identifique
    def conecta(self,host,puerto,master):
        try:
            print(host)
            p = int(puerto)
            print(p)
            self.control.action((host,p))
            master.destroy()
            r = Tk()
            r.title("Identificarse")
            label = Label(r)
            e = Entry(r)
            e.bind('<Return>', (lambda _: self.identify(e,r)))
            e.pack()
            label.pack()
            r.mainloop()
        except:
            tkMessageBox.showinfo("Error al conectar", "Conexion rechazada por el host")
            sys.exit()
