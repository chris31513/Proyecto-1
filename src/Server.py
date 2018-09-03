# -*- coding: utf-8 -*-
import threading
import socket
import sys
import os
import time
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

class Server(object):
    def crea_server(self, tupla):
        self.socket = socket.socket()
        self.socket.bind(tupla)
        self.socket.listen(10000)
        self.mientras = True
        self.clientes = []
        self.usuario = ""
        self.mensaje = ""
    def conecta(self):
        while self.mientras:
            print("Todo ok")
            conexion,ip = self.socket.accept()
            self.clientes.append(conexion)
            print "New User"
            hilo_envia = threading.Thread(self.envia_mensaje()).start()
            hilo_recibe = threading.Thread(self.recibe_mensaje()).start()
            print(self.usuario)
        hilo_envia.join()
        hilo_recibe.join()
        sys.exit()
            
    def desconecta(self):
        for cliente in self.clientes:
            cliente.close()
        mientras = False
        sys.exit()

    def envia_mensaje(self):
        for cliente in self.clientes:
            cliente.send(bytearray(self.usuario, "utf8"))
            cliente.send(bytearray(self.mensaje, "utf8"))

    def recibe_mensaje(self):
        #try:
        for cliente in self.clientes:
            self.usuario = cliente.recv(1024).decode('utf-8')
            self.mensaje = cliente.recv(1024).decode('utf-8')
        #except:
            #print("He recibido un mensaje extraño")
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
    mientras = True
    #try:
    hilo_conexion = threading.Thread(server.conecta()).start()
    #except:
        #print(" " + "Okay, bye")
        #server.desconecta()
        #hilo_conexion.join()
        #hilo_envia.join()
        #hilo_recibe.join()
        #sys.exit()
main()
