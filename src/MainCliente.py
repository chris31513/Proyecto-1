# -*- coding: utf-8 -*-
from Cliente import Cliente
from Eventos import Eventos
import threading
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
            try:
                instrucciones = instruccion.split(" ", 1)
                if len(instrucciones) == 0:
                    raise ValueError
                cliente.envia_mensaje(instrucciones[0])
                evento = eventos.get_evento(instrucciones.pop(0))
                if evento == eventos.IDENTIFY:
                    if len(instrucciones) == 0 or len(instrucciones) > 1:
                        raise ValueError
                    print(instrucciones[0])
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
                    cliente.envia_mensaje(new_inst.pop(0))
                if evento == eventos.DISCONECT:
                    ctrl = False
                    sys.exit()
                    cliente.sock.close()
                    
            except:
                print('Evento Incorrecto')
main()
