# -*- coding: utf-8 -*-
import threading
import socket
import sys
import time
import json
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
        hilo_conecta = threading.Thread(target = self.conecta)
        hilo_conecta.setDaemon(True)
        hilo_conecta.start()
        hilo_recibe = threading.Thread(target = self.recibe, args = (conexion,ip)).start()
        self.hilos.append(hilo_conecta)
        self.hilos.append(hilo_recibe)
    def desconecta(self):
        for cliente in self.clientes:
            cliente.get_socket().close()
        for hilos in self.hilos:
            hilos.join(2)
        self.ctrl = False
        sys.exit()

    def envia_publico(self,mensaje):
        for cliente in self.clientes:
            cliente.send(bytes(mensaje).encode('UTF-8'))

    def envia_privado(self,usuario,mensaje,nombre):
        for cliente in self.clientes:
            if usuario == cliente.get_nombre():
                s = nombre + ": " + mensaje
                cliente.get_socket.send(bytes(s).encode('UTF-8'))
    def envia(self,msg,cliente):
        print(msg)
        cliente.send(bytes(msg).encode('UTF-8'))
    def get_lista(self):
        lista = []
        for cliente in self.clientes:
            lista.append(cliente.get_nombre())
        return lista
   
    def recibe(self,cliente,ip):
        eventos = Eventos()
        while True:
            try:
                m = cliente.recv(1024).encode('UTF-8')
                print(m)
                e = m.split(" ",1)
                print(e)
                evento = eventos.get_evento(e.pop(0))
                if evento == eventos.IDENTIFY:
                    if len(e) != 1:
                        raise ValueError
                    for i in self.clientes:
                        if ip == i.get_ip():
                            i.set_nombre(e.pop(0))
                            print(i.get_nombre())
                if evento == eventos.STATUS:
                    if len(e) != 1:
                        raise ValueError
                    for i in clientes:
                        if ip == i.get_ip():
                            i.set_estado(e.pop(0))
                if evento == eventos.MESSAGE:
                    if len(e) != 1:
                        raise ValueError
                    m = e.split(" ", 1)
                    usuario = m.pop(0)
                    mensaje = m.pop(0)
                    for i in self.clientes:
                        if ip == i.get_ip():
                            nombre = i.get_nombre()
                    self.envia_privado(usuario,mensaje,nombre)
                if evento == eventos.USERS:
                    s = ""
                    for i in self.clientes:
                        s = s + " " + i.get_nombre()
                    self.envia(s,cliente)
            except ValueError:
                print("ño")
