# -*- coding: utf-8 -*-
import socket
import sys
from Eventos import Eventos
reload(sys)
sys.setdefaultencoding('utf-8')
#----Clase del cliente
class Cliente(object):
    #----Método que define el estado del cliente
    def estado(self,msg):
        self.est = msg
    #----Método que define el nombre del cliente
    def nombre(self,msg):
        self.nombre = msg
    #----Método que crea el socket que usará el cliente para conectarse
    def crea_socket(self):
        self.sock = socket.socket()
        self.sock.settimeout(1)
    #----Método que se conecta al servidor
    def conecta(self, tupla):
        self.sock.connect(tupla)
        self.conectado = True 
    #----Método que nos dice si el cliente está o no conectado
    def is_conectado(self):
        return self.conectado
    #----Método para enviar mensajes válidos al servidor
    def envia_mensaje(self, msg):
        try:
            m = msg.rstrip().encode('UTF-8')
            try:
                self.sock.send(m)
            except socket.timeout:
                self.sock.send(m)
        except:
            print("Mensaje inválido")
    #----Método que recibe los mensajes del servidor
    def recibe_mensaje(self):
        try:
            mensaje = self.sock.recv(1024).encode('UTF-8')
            return mensaje
        except socket.timeout:
            raise ValueError
    #----Método que maneja todo lo que se escribe en la interfaz y en la terminal
    def maneja_evento(self, mensaje):
        if mensaje.rstrip() == "DISCONNECT":
            self.envia_mensaje(mensaje)
            raise SystemExit
            sys.exit()
            self.sock.close()
        eventos= Eventos()
        try:
            if mensaje.rstrip() == "USERS":
                self.envia_mensaje(mensaje)
            m = mensaje.split(" ",1)
            eventos.get_evento(m[0].rstrip())
            self.envia_mensaje(mensaje)
        except ValueError:
            print("Mensaje inválido")
