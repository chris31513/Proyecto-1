# -*- coding: utf-8 -*-
from Cliente import Cliente
from Eventos import Eventos
import threading
import pickle
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
        eventos = Eventos()
        while ctrl:
            instruccion = raw_input()
            cliente.maneja_evento(instruccion)
main()
