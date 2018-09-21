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
import sys

class TestCliente(unittest.TestCase):
    def runnable(self):
        self.conexion, ip = self.sock.accept()
    def setUp(self):
        self.sock = socket.socket()
        self.sock.bind(("0.0.0.0",8000))
        self.sock.listen(0)
        try:
            threading.Thread(target = self.runnable).start()
        except:
            self.assertTrue(False)
    def test_conecta(self):
        cliente = Cliente()
        cliente.crea_socket()
        cliente.conecta(("localhost",8000))
        self.assertTrue(cliente.is_conectado())
        self.desconecta()
    def desconecta(self):
        self.sock.close()
    def test_recibe(self):
        cliente = Cliente()
        cliente.crea_socket()
        cliente.conecta(("localhost",8000))
        m = "Hola" 
        s = m.encode('UTF-8')
        self.conexion.send(s)
        self.assertEquals("Hola", cliente.recibe_mensaje())
        self.desconecta()
    def test_envia(self):
        cliente = Cliente()
        cliente.crea_socket()
        cliente.conecta(("localhost",8000))
        cliente.maneja_evento("IDENTIFY yo" + "\n")
        self.assertEquals("IDENTIFY yo", self.conexion.recv(1024).encode('UTF-8'))
        self.desconecta()
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCliente)
unittest.TextTestRunner(verbosity=2).run(suite)
