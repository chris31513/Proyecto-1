# -*- coding: utf-8 -*-
import threading
import socket
import sys
import os
import time
import codecs
from SCliente import *
import Eventos
reload(sys)
sys.setdefaultencoding('utf-8')

class Server(object):
    def crea_server(self, tupla):
        self.socket = socket.socket()
        self.socket.bind(tupla)
        self.socket.listen(10000)
        self.ctrl = True
        self.clientes = []
    def conecta(self):
        while self.ctrl:
            print("Todo ok")
            self.conexion,ip = self.socket.accept()
            print(ip)
            cliente = SCliente(self.conexion,ip)
            hilo_agrega = threading.Thread(target = self.clientes.append, args = (cliente,))
            hilo_recibe = threading.Thread(target = self.recibe)
        hilo_agrega.join()
        sys.exit()
    def desconecta(self):
        for cliente in self.clientes:
            cliente.close()
        self.ctrl = False
        sys.exit()

    def envia_publico(self,mensaje):
        for cliente in self.clientes:
            cliente.send(bytearray(mensaje, 'utf-8'))

    def envia_privado(self,usuario,mensaje,nombre):
        for cliente in self.clientes:
            if usuario == cliente.get_nombre:
                s = nombre + ":" + mensaje
                cliente.get_socket.send(bytearray(s,'utf-8'))
        raise ValueError
    def envia(self,msg,nombre):
        for cliente in self.clientes:
            if nombre == cliente.get_nombre():
                cliente.get_socket().send(bytearray(msg,'utf-8'))
        pass
            
    def recibe(self):
        for cliente in self.clientes:
            ip = cliente.get_ip()
            try:
                mensaje = cliente.get_socket().recv(1024).decode('utf-8')
                print(mensaje)
            except:
                print("Mensaje no permitido")
            nombre = cliente.get_nombre()
            try:
                evento = Eventos.get_evento(mensaje)
                return evento
            except:
                lista = []
                lista.append(mensaje)
                lista.append(ip)
                lista.append(nombre)
                return lista
    
def main():
    try:
        print("Dirección:")
        ip = raw_input()
        if ip == "" or ip == None:
            raise ValueError()
        print("Puerto:")
        p = raw_input()
        puerto = int(p)
    except:
        print("Dirección o puerto no validos")
        sys.exit()
    server = Server()
    server.crea_server((ip, puerto))
    hilo_conexion = threading.Thread(target = server.conecta())
    hilo_recibe = threading.Thread(target = server.recibe())
    ctrl = True
    while ctrl:
        try:
            if type(len(server.recibe())) == str:
                evento = server.recibe()
                server.envia(evento)
            mensaje = server.recibe().pop(0)
            ip = server.recibe.pop(0)
            nombre = server.recibe.pop(0)
            if evento == Eventos.IDENTIFY:
                if len(mensaje) == 0:
                    raise ValueError
                for cliente in server.clientes:
                    if ip == cliente.get_ip():
                        if cliente.get_nombre != None:
                            print("Ya alguien se llama así")
                        cliente.set_nombre(mensaje)
                    raise NameError
            if evento == Eventos.STATUS:
                if len(mensaje) == 0:
                    raise ValueError
                for cliente in server.clientes:
                    if nombre == cliente.get_nombre():
                        cliente.set_estado(mensaje)
                    raise ValueError
            if evento == Eventos.USERS:
                lista = "".join(server.clientes)
                server.envia_privado()
            if evento == Eventos.MESSAGE:
                if len(mensaje) == 0:
                    raise ValueError
                m = mensaje.split(" ", 1)
                server.envia_privado(m[0], m[1], nombre)
                m.clear()
            if evento == Eventos.PUBLICMESSAGE:
                if len(mensaje) == 0:
                    raise ValueError
                server.envia_publico(mensaje)
            if evento == Eventos.CREATEROOM:
                if len(mensaje) == 0:
                    raise ValueError
                pass
            if evento == Eventos.INVITE:
                pass
            if evento == Eventos.JOINROOM:
                pass
            if evento == Eventos.ROOMESSAGE:
                pass
            if evento == Eventos.DISCONECT:
                ctrl == False
                server.desconecta()
        except:
            print("Evento incorrecto")
main()
