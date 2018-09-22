# -*- coding: utf-8 -*-
from Server import Server
import sys
#----Función que ejecuta al servidor y lo hace funcionar en la terminal
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
