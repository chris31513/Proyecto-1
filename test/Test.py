# -*- coding: utf-8 -*-
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
import time
#----Clase de pruebas unitarias
class TestCliente(unittest.TestCase):
    #----Método que acepta clientes
    def runnable(self):
        self.conexion, ip = self.sock.accept()
    #----Método que monta un pequeño servidor
    def set_up(self):
        self.sock = socket.socket()
        self.sock.bind(("0.0.0.0",0))
        self.sock.listen(0)
        threading.Thread(target = self.runnable).start()
    #----Test del método conecta
    def test_conecta(self):
        cliente = Cliente()
        cliente.crea_socket()
        self.set_up()
        cliente.conecta(("localhost", self.sock.getsockname()[1]))
        self.assertTrue(cliente.is_conectado())
        self.desconecta()
    #----Método que mata al servidor
    def desconecta(self):
        self.sock.close()
    #----Test que desconecta al cliente
    def test_desconecta(self):
        time.sleep(0.0005)
        cliente = Cliente()
        cliente.crea_socket()
        self.set_up()
        cliente.conecta(("localhost", self.sock.getsockname()[1]))
        with self.assertRaises(SystemExit):
            cliente.maneja_evento("DISCONNECT"+"\n")
        self.desconecta()
    #----Test de enviar y manejar los eventos
    def test_envia_recibe(self):
        time.sleep(0.0005)
        cliente = Cliente()
        cliente.crea_socket()
        self.set_up()
        cliente.conecta(("localhost",self.sock.getsockname()[1]))
        cliente.maneja_evento("IDENTIFY yo" + "\n")
        self.assertEquals("IDENTIFY yo", self.conexion.recv(1024).encode('UTF-8'))
        self.conexion.send("Hola".encode('UTF-8'))
        self.assertEquals(cliente.recibe_mensaje(),"Hola")
        self.desconecta()
        

if __name__ == '__main__':
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCliente)
    except:
        pass
unittest.TextTestRunner(verbosity=2).run(suite)
