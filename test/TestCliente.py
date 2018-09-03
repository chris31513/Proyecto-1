if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from src.Cliente import Cliente
    else:
        from ..src.Cliente import Cliente
import unittest
import socket
import threading
import time
import sys
import pickle

class Server(object):
    def __init__(self):
        self.clientes = []
        self.host = host
        self.port = port
        self.sock = socket.socket()
        hilo1 = threading.Thread(target = self.recibe_mensajes())
        hilo1.daemon = True
    def prepara_coneccion(self):
        self.sock.bind("localhost", 8000)
        self.sock.listen(100000)
    def conecta(self):
        while True:
            conn, ip = self.sock.accept()
            self.clientes.append(conn)
    def mensaje_a_todos(self,msg):
        for cliente in self.clientes:
            try:
                cliente.send(msg)
            except:
                clientes.remove(cliente)
    def recibe_mensajes(self):
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        mensaje = c.recv(1024)
                        if mensaje:
                            self.mensaje_a_todos(mensaje)
                    except:
                        pass
    def desconecta(self):
        self.sock.close()
        sys.exit()
class Cliente2:
    def crea_socket(self):
        self.sock = socket.socket()
    def conecta(self):
        self.sock.connect("localhost", 8000)
    def recibe_mensaje(self):
        while True:
            mensaje = self.sock.recv(1024)
            if mensaje:
                return mensaje
    def desconecta(self):
        self.sock.close()
        sys.exit()
class TestCliente(unittest.TestCase):
    def test_conecta(self):
        servidor = Server()
        servidor.prepara_coneccion()
        hilo1 = threading.Thread(target = servidor.conecta())
        hilo1.daemon = True
        hilo1.start()
        hilo2 = threading.Thread(target = cliente.conecta())
        hilo2.deamon = 
        
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCliente)
unittest.TextTestRunner(verbosity=2).run(suite)
