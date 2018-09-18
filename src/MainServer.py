# -*- coding: utf-8 -*-
from Server import Server
from Eventos import Eventos
import threading
def main():
    try:
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
        server.conecta()
    except:
        sys.exit()
main()
