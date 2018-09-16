# -*- coding: utf-8 -*-
from Server import Server
from Eventos import Eventos
import threading
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
    server.conecta()
    ctrl = True
    eventos = Eventos()
    while ctrl:
        try:
            socket, ip = server.get_clientes()
            if type(server.recibe(socket,ip)) == list:
                mensaje = server.recibe(socket,ip).pop(0)
                ip = server.recibe(socket,ip).pop(0)
                nombre = server.recibe(socket,ip).pop(0)
            evento = server.recibe(socket, ip)
            if evento == eventos.IDENTIFY:
                if len(mensaje) == 0:
                    raise ValueError
                for cliente in server.clientes:
                    if ip == cliente.get_ip():
                        if cliente.get_nombre != None:
                            print("Ya alguien se llama así")
                        print(mensaje)
                        cliente.set_nombre(mensaje)
                    raise NameError
            if evento == eventos.STATUS:
                if len(mensaje) == 0:
                    raise ValueError
                for cliente in server.clientes:
                    if nombre == cliente.get_nombre():
                        cliente.set_estado(mensaje)
                    raise ValueError
            if evento == eventos.USERS:
                lista = "".join(server.clientes)
                server.envia_privado()
            if evento == eventos.MESSAGE:
                if len(mensaje) == 0:
                    raise ValueError
                m = mensaje.split(" ", 1)
                server.envia_privado(m[0], m[1], nombre)
                m.clear()
            if evento == eventos.PUBLICMESSAGE:
                if len(mensaje) == 0:
                    raise ValueError
                server.envia_publico(mensaje)
            if evento == eventos.CREATEROOM:
                if len(mensaje) == 0:
                    raise ValueError
                pass
            if evento == eventos.INVITE:
                pass
            if evento == eventos.JOINROOM:
                pass
            if evento == eventos.ROOMESSAGE:
                pass
            if evento == eventos.DISCONECT:
                hilo_conexion.join()
                ctrl == False
                server.desconecta()
        except:
            print("Evento incorrecto")
main()
