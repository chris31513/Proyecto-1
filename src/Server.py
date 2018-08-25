import socket

class Server:
    

    def crea_socket(self):
        s_socket = socket.socket()
        s_socket.bind(('localhost',8000))
        s_socket.listen(10000)
        return s_socket

    def conecta(self):
        while True:
            conexion,ip = self.crea_socket().accept()
            print "New Client"
            print ip
            return conexion

    def desconecta(self):
        conexion.close()

    def recibe_envia_mensaje(self):
        recibido = self.crea_socket().recv(1024)
        self.conecta().send("Hola")
        return recibido

