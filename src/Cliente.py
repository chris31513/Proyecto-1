# -*- coding: utf-8 -*-
import socket
import threading
import sys
import pickle
import os
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
class Cliente(object):
    def __init__(self, nombre):
        self.nombre = nombre
    def crea_socket(self):
        self.sock = socket.socket()
    def conecta(self, tupla):
        self.sock.connect(tupla)
        self.sock.send(bytearray(self.nombre, "utf8"))
    def envia_mensaje(self, msg):
        try:
            m = bytearray(msg,"utf8")
        except:
            print("Mensaje no valido")
        usuario = bytearray(self.nombre, "utf8")
        self.sock.send(usuario)
        self.sock.send(m)
    def recibe_mensaje(self):
        while True:
            usuario = self.sock.recv(1024).decode('utf-8')
            mensaje = self.sock.recv(1024).decode('utf-8')
            if usuario == self.nombre:
                print("Tú has escrito" + " " + mensaje)
            print(usuario + "dice:" + " " + mensaje)
            
    
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
    try:
        print("Usuario:")
        usuario = raw_input()
        if usuario == None or usuario == "":
            raise ValueError()
        cliente = Cliente(usuario)
    except:
        print("Usuario no valido")
        sys.exit()
    try:
        cliente.crea_socket()
        cliente.conecta((ip,puerto))
    except:
        print("Conexión rechazada por el host")
        sys.exit()
    mientras = True
    while mientras:
        print("->")
        mensaje = raw_input()
        hilo_mensaje = threading.Thread(cliente.envia_mensaje(mensaje)).start()
        hilo_recibe = threading.Thread(cliente.recibe_mensaje()).start()
        if mensaje == "exit":
            hilo_mensaje.join()
            hilo_recibe.join()
            mientras = False
    sys.exit()
main()
