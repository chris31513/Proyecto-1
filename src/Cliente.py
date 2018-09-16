# -*- coding: utf-8 -*-
import socket
import threading
import sys
import pickle
import os
import codecs
from Eventos import Eventos
import time
import traceback
reload(sys)
sys.setdefaultencoding('utf-8')
class Cliente(object):
    def estado(self,msg):
        self.est = msg
    def nombre(self,msg):
        self.nombre = msg
    def crea_socket(self):
        self.sock = socket.socket()
    def conecta(self, tupla):
        self.sock.connect(tupla)
    def envia_mensaje(self, msg):
        try:
            m = msg.encode()
            self.sock.send(m)
        except:
            print("Mensaje no valido")
    def recibe_mensaje(self):
        mensaje = str(self.sock.recv(1024)).decode('UTF-8')
        print(mensaje)
        return mensaje
    
    
        #try:
if __name__ == "__main__":
    cliente = Cliente()
    cliente.main()
