
class SCliente(object):
    def __init__(self, socket, ip): 
        self.socket = socket
        self.ip = ip
        self.nombre = ""
        self.estado = ""
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_estado(self,estado):
        self.estado = estado
    def get_socket(self):
        return self.socket
    def get_nombre(self):
        return self.nombre
    def get_estado(self):
        return self.estado
    def get_ip(self):
        return self.ip
