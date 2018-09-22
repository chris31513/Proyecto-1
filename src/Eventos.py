# -*- coding: utf-8 -*-
#----Clase para definir los eventos del protocolo
class Eventos(object):
    IDENTIFY = 'IDENTIFY'
    STATUS = 'STATUS'
    USERS = 'USERS'
    MESSAGE = 'MESSAGE'
    PUBLICMESSAGE = 'PUBLICMESSAGE'
    CREATEROOM = 'CREATEROOM'
    INVITE = 'INVITE'
    JOINROOM = 'JOINROOM'
    ROOMESSAGE = 'ROOMESSAGE'
    DISCONNECT = 'DISCONNECT'
    #----Método que devuelve un evento dada una cadena
    def get_evento(self,msg):
        if msg == 'IDENTIFY':
            return self.IDENTIFY
        if msg == 'STATUS':
            return self.STATUS
        if msg == 'MESSAGE':
            return self.MESSAGE
        if msg == 'USERS':
            return self.USERS
        if msg == 'PUBLICMESSAGE':
            return self.PUBLICMESSAGE
        if msg == 'CREATEROOM':
            return self.CREATEROOM
        if msg == 'INVITE':
            return self.INVITE
        if msg == 'JOINROOM':
            return self.JOINROOM
        if msg == 'ROOMESSAGE':
            return self.ROOMESSAGE
        if msg == 'DISCONNECT':
            return self.DISCONNECT
        raise ValueError
