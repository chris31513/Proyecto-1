#----Clase que encapsula a los clientes
class SCliente(object):
    #----Constructor del objeto, recibe el socket del cliente y la ip
    def __init__(self, socket, ip): 
        self.socket = socket
        self.ip = ip
        self.nombre = ""
        self.estado = ""
    #----Define el nombre del cliente cuando se identifica en el servidor
    def set_nombre(self,nombre):
        self.nombre = nombre
    #----Define el estado del cliente
    def set_estado(self,estado):
        self.estado = estado
    #----Regresa el socket del cliente
    def get_socket(self):
        return self.socket
    #----Regresa el nombre del cliente
    def get_nombre(self):
        return self.nombre
    #----Regresa el estado del cliente
    def get_estado(self):
        return self.estado
    #----Regresa la direccion del cliente
    def get_ip(self):
        return self.ip
