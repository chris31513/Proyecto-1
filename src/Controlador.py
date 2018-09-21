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
class Controlador(object):
    def set_controlador(self,master):
        GUI(master,self)
        self.cliente = Cliente()
        self.cliente.crea_socket()
    def action(self,tupla):
        self.cliente.conecta(tupla)
    def recibe(self):
        self.cliente.recibe_mensaje()
    def envia(self,e):
        r = e.get()
        s = "PUBLICMESSAGE " + r + "\n"
        self.cliente.maneja_evento(s)
    def identify(self,e):
        nombre = e.get()
        s = "IDENTIFY " + nombre + "\n"
        self.cliente.maneja_evento(s)
def main():
    raiz = Tk()
    controlador = Controlador()
    controlador.set_controlador(raiz)
    raiz.mainloop()

main()
