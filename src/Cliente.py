import socket

class Cliente:

    def conecta(self):
        cliente_socket = socket.socket()
        cliente_socket.connect(('localhost',8000))
        return cliente_socket

    def envia_mensaje(self):
        self.conecta().send("Hola")

    def recibido(self):
        return self.conecta().recv(1024)

    def desconecta(self):
        self.conecta().close()
