# -*- coding: utf-8 -*-
import socket
import threading
import sys
import json
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
            m = msg.encode('UTF-8')
            self.sock.send(m)
        except:
            print("Mensaje no valido")
    def recibe_mensaje(self):
        mensaje = self.sock.recv(1024).decode('UTF-8')
        return mensaje
    def maneja_evento(self, mensaje):
        if mensaje == "DISCONECT":
            self.envia_mensaje(mensaje)
            sys.exit()
            self.sock.close()
        eventos= Eventos()
        try:
            if mensaje == "USERS":
                self.envia_mensaje(mensaje)
                print(self.recibe_mensaje())
            m = mensaje.split(" ",1)
            eventos.get_evento(m[0])
            self.envia_mensaje(mensaje)
        except ValueError:
            print("mensaje no valido")
