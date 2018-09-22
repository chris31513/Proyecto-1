# -*- coding: utf-8 -*-
#----Clase para los cuartos de chat
class ChatRoom(object):
    #----Constructor del cuarto
    def __init__(self,nombre,d,cliente):
        self.nombre = nombre
        self.due = d
        self.invitaciones = []
        self.clientes = []
        self.clientes.append(cliente)
    #----Método que regresa al dueño del cuarto
    def get_due(self):
        return self.due
    #----Método que regresa la lista de miembros en el cuarto
    def get_miembros(self):
        return self.clientes
    #----Método que regresa el nombre del cuarto
    def get_nombre(self):
        return self.nombre
    #----Método que regresa la lista de invitados al cuarto
    def get_invitaciones(self):
        return self.invitaciones
    #----Método que mete a clientes a la lista de miembros
    def joinr(self, nombre, cliente):
        if nombre not in self.invitaciones:
            raise ValueError
        self.clientes.append(cliente)
    #----Método que agrega un nombre de algún cliente a la lista de invitados
    def invita(self, nombre):
        self.invitaciones.append(nombre)
