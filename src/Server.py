# -*- coding: utf-8 -*-
import threading
import socket
import sys
import time
from SCliente import SCliente
from Eventos import Eventos
reload(sys)
sys.setdefaultencoding('utf-8')

class Server(object):
    def crea_server(self, tupla):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(tupla)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.listen(1)
        self.ctrl = True
        self.clientes = []
        self.hilos = []
    def conecta(self):
        print("Todo ok")
        conexion,ip = self.socket.accept()
        print(ip)
        cliente = SCliente(conexion,ip)
        self.clientes.append(cliente)
        hilo_conecta = threading.Thread(target = self.conecta).start()
        hilo_recibe = threading.Thread(target = self.recibe, args = (conexion,ip)).start()
    def desconecta(self):
        for cliente in self.clientes:
            cliente.close()
        self.ctrl = False
        sys.exit()

    def envia_publico(self,mensaje):
        for cliente in self.clientes:
            cliente.send(bytes(mensaje).encode('UTF-8'))

    def envia_privado(self,usuario,mensaje,nombre):
        for cliente in self.clientes:
            if usuario == cliente.get_nombre:
                s = nombre + ":" + mensaje
                cliente.get_socket.send(bytes(s).encode('UTF-8'))
        raise ValueError
    def envia(self,msg,nombre):
        while True:
            for cliente in self.clientes:
                if nombre == cliente.get_ip():
                    cliente.get_socket().send(bytes(msg).encode('UTF-8'))
            pass
            
    def recibe(self,cliente,ip):
        eventos = Eventos()
        while True:
            mensaje = cliente.recv(1024).decode('UTF-8')
            try:
                evento = eventos.get_evento(mensaje)
                print(evento)
                return evento
        
            except:
                print(mensaje)
                for i in self.clientes:
                    if ip == i.get_ip():
                        nombre = i.get_nombre()
            lista = []
            lista.append(mensaje)
            lista.append(ip)
            lista.append(nombre)
            return lista
    def get_clientes(self):
        while True:
            for cliente in self.clientes:
                return cliente.get_socket(), cliente.get_ip()
