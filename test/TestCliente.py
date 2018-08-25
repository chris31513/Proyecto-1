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

class Server:
    

    def crea_socket(self):
        s_socket = socket.socket()
        s_socket.bind(('localhost',8000))
        s_socket.listen(1)
        socket.setdefaulttimeout(10.0)
        return s_socket

    def conecta(self):
        conexion, ip = self.crea_socket().accept()
        return conexion
    
    def recibido(self):
        recibi = self.crea_socket().recv(1024)
        self.conecta().send("Hola")
        return recibi
        

    def desconecta(self):
        self.crea_socket().close()

class TestCliente(unittest.TestCase):
    def test_send(self):
        servidor = Server()
        servidor.crea_socket()
        cliente = Cliente()
        servidor.conecta()
        cliente.envia_mensaje()
        self.assertEquals(servidor.recibido(),cliente.recibido())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCliente)
unittest.TextTestRunner(verbosity=2).run(suite)
