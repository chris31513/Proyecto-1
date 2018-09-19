# -*- coding: utf-8 -*-
class ChatRoom(object):
    def __init__(self,nombre,d,cliente):
        self.nombre = nombre
        self.due = d
        self.invitaciones = []
        self.clientes = []
        self.clientes.append(cliente)
    def get_due(self):
        return self.due
    def get_miembros(self):
        return self.clientes
    def get_nombre(self):
        return self.nombre
    def get_invitaciones(self):
        return self.invitaciones
    def joinr(self, nombre, cliente):
        if nombre not in self.invitaciones:
            raise ValueError
        self.clientes.append(cliente)
    def invita(self, nombre):
        self.invitaciones.append(nombre)
