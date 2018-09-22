# -*- coding: utf-8 -*-
import threading
import socket
import sys
import os
from SCliente import SCliente
from Eventos import Eventos
from ChatRoom import ChatRoom
reload(sys)
sys.setdefaultencoding('utf-8')
#----Clase del servidor
class Server(object):
    #----Prepara el servidor para aceptar clientes
    def crea_server(self, puerto):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0",puerto))
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.listen(1000)
        self.clientes = []
        self.hilos = []
        self.nombres = []
        self.cuartos = []
    #----Método que acepta clientes
    def conecta(self):
        try:
            conexion,ip = self.socket.accept()
            print("Escucchando a: " + str(ip))
            cliente = SCliente(conexion,ip)
            self.clientes.append(cliente)
            self.evento_hilo = threading.Event()
            hilo_conecta = threading.Thread(target = self.conecta).start()
            hilo_recibe = threading.Thread(target = self.recibe, args = (conexion,ip)).start()
            self.hilos.append(hilo_conecta)
            self.hilos.append(hilo_recibe)
        except KeyboardInterrupt:
            self.desconecta()
    #----Método que apaga el servidor
    def desconecta(self):
        for cliente in self.clientes:
            cliente.get_socket().close()
        for hilos in self.hilos:
            hilos.terminate()
            hilos.interupt_main()
        self.ctrl = False
        os._exit(0)
    #----Método que envia mensaje a todos los clientes
    def envia_publico(self,mensaje, ip):
        for cliente in self.clientes:
            for i in self.clientes:
                if ip == i.get_ip():
                    nombre = i.get_nombre()
            s = nombre + ": " + mensaje
            m = s.encode('UTF-8')
            cliente.get_socket().send(s.encode('UTF-8'))
    
    #----Método que envia un mensaje al cliente especificado
    def envia_privado(self,usuario,mensaje,nombre):
        for cliente in self.clientes:
            if usuario == cliente.get_nombre():
                s = nombre + ": " + mensaje
                cliente.get_socket().send(s.encode('UTF-8'))
    #----Método que busca el nombre de un cliente dada su ip
    def obtiene_nombre(self,ip):
        for cliente in self.clientes:
            if ip == cliente.get_ip():
                return cliente.get_nombre()
    #----Método usado para enviar la lista de clientes
    def envia(self,msg,cliente):
        cliente.send(msg.encode('UTF-8'))
    #----Método para enviar invitaciones al cliente especificado
    def envia_cuarto(self,msg,cliente,nombre):
        s = nombre + ": " + msg
        cliente.send(s.encode('UTF-8'))
    #----Método que regresa un socket de algún cliente
    def get_conexion(self, conexion):
        return conexion
    #----Método que regresa la lista de nombres identificados
    def get_lista(self):
        lista = []
        for cliente in self.clientes:
            lista.append(cliente.get_nombre())
        return lista
    #----Método que recibe y maneja los eventos
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
                                for r in self.clientes:
                                    if ip == r.get_ip():
                                        nombre = r.get_nombre()
                                i.joinr(nombre,cliente)
                                i.envia("Te has unido al cuarto " + nombre,cliente)
                    except ValueError:
                        self.envia("No estás invitado", cliente)
                if evento == eventos.ROOMESSAGE:
                    q = e.pop(0).rstrip().split(" ",1)
                    for i in self.clientes:
                        if ip == i.get_ip():
                            nombre = i.get_nombre()
                    for r in self.cuartos:
                        if q.pop(0) == r.get_nombre():
                            m = r.get_miembros()
                    for a in m:
                        self.envia_cuarto(q[0],a,nombre)
                    q.pop(0)
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
            except Exception as e:
                if e != KeyboardInterrupt:
                    continue
                else:
                    self.desconecta()
