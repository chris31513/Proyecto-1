# -*- coding: utf-8 -*-
from Server import Server
from Eventos import Eventos
import threading
import os
def main():
    try:
        try:
            print("Puerto:")
            p = raw_input()
            puerto = int(p)
        except:
            print("Puerto inválido")
            sys.exit()
        server = Server()
        server.crea_server(puerto)
        server.conecta()
        
    except KeyboardInterrupt:
        server.desconecta()
main()
