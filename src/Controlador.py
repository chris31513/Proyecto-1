# -*- coding: utf-8 -*-
from Cliente import Cliente
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from ig.GUI import GUI
    else:
        from ..ig.GUI import GUI

from Tkinter import *
#----Clase que comunica al cliente con la interfaz
class Controlador(object):
    #----Método que crea una interfaz y un cliente, funciona como intermediario para la interfaz
    def set_controlador(self,master):
        GUI(master,self)
        self.cliente = Cliente()
        self.cliente.crea_socket()
    #----Método que conecta al cliente, mas tarde es usado en la interfaz
    def action(self,tupla):
        self.cliente.conecta(tupla)
    #----Método que llama al método que recibe del cliente
    def recibe(self):
        self.cliente.recibe_mensaje()
    #----Método que llama al método para manejar eventos del cliente
    def envia(self,e):
        r = e.get()
        s = "PUBLICMESSAGE " + r + "\n"
        self.cliente.maneja_evento(s)
    #----Método usado para identificar al cliente, llamado por un "Entry" en la interfaz
    def identify(self,e):
        nombre = e.get()
        s = "IDENTIFY " + nombre + "\n"
        self.cliente.maneja_evento(s)
#----Crea la primer ventana de la interfaz
def main():
    raiz = Tk()
    raiz.title("Conectar")
    controlador = Controlador()
    controlador.set_controlador(raiz)
    raiz.mainloop()

main()
