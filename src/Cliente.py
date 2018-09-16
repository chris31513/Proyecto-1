# -*- coding: utf-8 -*-
import socket
import threading
import sys
import pickle
import os
import codecs
from Eventos import Eventos
import time
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
            m = bytearray(msg,"utf8")
            self.sock.send(m)
        except:
            print("Mensaje no valido")
    def recibe_mensaje(self):
        mensaje = self.sock.recv(1024).decode('utf-8')
        return mensaje
    
def main():
    try:
        print("Direccion:")
        ip = raw_input()
        if ip == None or ip == "":
            raise ValueError
        print("Puerto:")
        p = raw_input()
        puerto = int(p)
    except:
        print("Estas haciendo algo mal, por favor verifica que tu dirección y tu puerto sean válidos.")
        sys.exit()
    cliente = Cliente()
    try:
        cliente.crea_socket()
        cliente.conecta((ip,puerto))
    except:
        print("Conexión rechazada por el host")
        sys.exit()
    ctrl = True
    while ctrl:
        eventos = Eventos()
        instruccion = raw_input()
        try:
            instrucciones = instruccion.split(" ", 1)
            if len(instrucciones) == 0:
                raise ValueError
            evento = eventos.get_evento(instrucciones.pop(0))
            cliente.envia_mensaje(evento)
            if evento == eventos.IDENTIFY:
                if len(instrucciones) == 0 or len(instrucciones) > 1:
                    raise ValueError
                cliente.nombre(instrucciones[0])
                cliente.envia_mensaje(instrucciones.pop(0))
            if evento == eventos.STATUS:
                if len(instrucciones) == 0 or len(instrucciones) > 1:
                    raise ValueError
                cliente.estado(instrucciones[0])
                cliente.envia_mensaje(instrucciones.pop(0))
            if evento == eventos.MESSAGE:
                if len(instrucciones) == 0:
                    raise ValueError
                nueva_ints = instrucciones.pop(0).split(" ", 1)
                s = nueva_ints[0] + " " + nueva_ints[1]
                cliente.envia_mensaje(s)
                nueva_ints.clear()
            if evento == eventos.PUBLICMESSAGE:
                if len(instrucciones) == 0:
                    raise ValueError
                cliente.envia_mensaje(instrucciones.pop(0))
            if evento == eventos.CREATEROOM:
                if len(instrucciones) == 0:
                    raise ValueError
                cliente.envia_mensaje(instrucciones.pop(0))
            if evento == eventos.INVITE:
                if len(instrucciones) == 0:
                    raise ValueError
                cuarto = instrucciones.pop(0).split(" ", 1)
                usuarios = new_inst.pop(1).split()
                for usuario in usuarios:
                    cliente.envia_mensaje(cuarto[0])
                    cliente.envia_mensaje(usuario)
                new_inst.clear()
                usuarios.clear()
            if evento == eventos.JOINROOM:
                if len(instrucciones) == 0:
                    raise ValueError
                cliente.envia_mensaje(instrucciones.pop(0))
            if evento == eventos.ROOMESSAGE:
                if len(instrucciones) == 0:
                    raise ValueError
                new_inst = instrucciones.pop(0).split(" ", 1)
                cliente.envia_mensaje(new_inst.pop(0))
                clience.envia_mensaje(new_inst.pop(0))
            if evento == eventos.DISCONECT:
                ctrl = False
                sys.exit()
                cliente.sock.close()
                
        except:
            print('Evento Incorrecto')
        try:
            instrucciones_server = cliente.recibe_mensaje().split(" ", 1)
            evento = Eventos.get_evento(instrucciones_server.pop(0))
            if evento == Eventos.USERS:
                if len(instrucciones_server) != 0:
                    raise ValueError
                print(instrucciones_server.pop(0))
                if evento == Eventos.MESSAGE:
                    print(cliente.recibe_mensaje())
                    if evento == Eventos.PUBLICMESSAGE:
                        print(cliente.recibe_mensaje())
                        if evento == Eventos.ROOMESSAGE:
                            print(cliente.recibe_mensaje())
        except:
            sys.exit()
main()
