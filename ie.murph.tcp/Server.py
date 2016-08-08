__author__ = 'Paul'
import socket

class TcpServer():

    def Main(self):
        print("TcpServer")
        host = "127.0.0.1"
        port = 5000

        sock = socket.socket()
        sock.bind((host, port))

        sock.listen(1)
        client, addr = sock.accept()
        print("Connection from: " + str(addr))
        while True:
            data = client.recv(1024).decode('utf-8')#
            if not data:
                break
            print("From connected user: " + data) #str(data))
            data = data.upper()
            print("Sending: ", data) #str(data))
            client.send(data.encode('utf-8'))#
        client.close()


x = TcpServer()
if __name__ == "__main__":
    x.Main()