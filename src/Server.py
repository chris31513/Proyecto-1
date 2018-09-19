# -*- coding: utf-8 -*-
import threading
import socket
import sys
import time
import json
from SCliente import SCliente
from Eventos import Eventos
from ChatRoom import ChatRoom
reload(sys)
sys.setdefaultencoding('utf-8')

class Server(object):
    def crea_server(self, tupla):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(tupla)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.listen(1000)
        self.clientes = []
        self.hilos = []
        self.nombres = []
        self.cuartos = []
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

    def envia_publico(self,mensaje, ip):
        print(mensaje)
        for cliente in self.clientes:
            for i in self.clientes:
                if ip == i.get_ip():
                    nombre = i.get_nombre()
            s = nombre + ": " + mensaje
            m = s.encode('UTF-8')
            cliente.get_socket().send(s.encode('UTF-8'))

    def envia_privado(self,usuario,mensaje,nombre):
        for cliente in self.clientes:
            if usuario == cliente.get_nombre():
                s = nombre + ": " + mensaje
                cliente.get_socket().send(s.encode('UTF-8'))
    def obtiene_nombre(self,ip):
        for cliente in self.clientes:
            if ip == cliente.get_ip():
                return cliente.get_nombre()
    def envia(self,msg,cliente):
        cliente.send(msg.encode('UTF-8'))
    def get_lista(self):
        lista = []
        for cliente in self.clientes:
            lista.append(cliente.get_nombre())
        return lista
   
    def recibe(self,cliente,ip):
        eventos = Eventos()
        while True:
            try:
                r = cliente.recv(1024).encode('UTF-8')
                m = r.rstrip()
                e = m.split(" ",1)
                evento = eventos.get_evento(e.pop(0))
                print(evento)
                if evento == eventos.IDENTIFY:
                    if len(e) != 1:
                        raise ValueError
                    for i in self.clientes:
                        if ip == i.get_ip():
                            if not e[0] in self.nombres:      
                                i.set_nombre(e.pop(0))
                                self.nombres.append(i.get_nombre())
                                print(str(self.nombres))
                    try:
                        if len(self.nombres) != 0:
                            if e[0] in self.nombres:
                                self.envia("Nombre ocupdado", cliente)
                    except:
                        continue
                if evento == eventos.STATUS:
                    if len(e) != 1:
                        raise ValueError
                    for i in clientes:
                        if ip == i.get_ip():
                            i.set_estado(e.pop(0))
                if evento == eventos.MESSAGE:
                    z = e.pop(0).split(" ", 1)
                    usuario = z.pop(0)
                    mensaje = z.pop(0)
                    nombre = self.obtiene_nombre(ip)
                    self.envia_privado(usuario,mensaje,nombre)
                if evento == eventos.USERS:
                    self.envia(str(self.nombres), cliente)
                if evento == eventos.PUBLICMESSAGE:
                        print(e[0])
                        self.envia_publico(e.pop(0), ip)
                if evento == eventos.CREATEROOM:
                    for i in self.clientes:
                        if ip == i.get_ip():
                            nombre = i.get_nombre()
                    cuarto = ChatRoom(e.pop(0),nombre, cliente)
                    self.cuartos.append(cuarto)
                if evento == eventos.INVITE:
                    new_int = e.pop(0).split(" ",1)
                    cuarto = new_int.pop(0)
                    usuarios = new_int.pop(0).split()
                    for r in self.clientes:
                        if ip == r.get_ip():
                            nombre = r.get_nombre()
                    for i in self.cuartos:
                        if i.get_nombre() == cuarto: 
                            if nombre == i.get_due():
                                for usuario in usuarios:
                                    print("listo")
                                    i.invita(usuario)
                                    self.envia_privado(usuario,"Te he invitado al cuarto " + cuarto, nombre)
                                    print(i.get_invitaciones())
                if evento == eventos.JOINROOM:
                    try:
                        cuarto = e.pop(0)
                        for i in self.cuartos:
                            if cuarto == i.get_nombre():
                                for i in self.clientes:
                                    if ip == i.get_ip():
                                        nombre = i.get_nombre()
                                print("Listo")
                                i.joinr(nombre,cliente)
                    except:
                        self.envia("No estás invitado", cliente)
                if evento == eventos.DISCONNECT:
                    for i in self.clientes:
                        if i.get_ip() == ip:
                            for n in self.nombres:
                                if i.get_nombre() == n:
                                    d = self.nombres.index(n)
                                    self.nombres.pop(d)
                            t = self.clientes.index(i)
                            self.clientes.pop(t)
                            i.get_socket().close()
                            raise ValueError
            except:
                continue
