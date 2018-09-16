
class ChatRoom(object):

    def __init__(self,nombre,dueño):
        self.nombre = nombre
        self.dueño = dueño
        self.invitaciones = []
        self.clientes = []
        self.clientes.append(dueño)
    def get_dueño(self):
        return self.dueño
    def get_miembros(self):
        return self.clientes
    def joinr(self, nombre, cliente):
        if nombre not in invitaciones:
            raise ValueError
        self.clientes.append(cliente)
    def invita(self, nombre):
        self.invitaciones.append(nombre)
