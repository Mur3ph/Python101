__author__ = 'Paul'
import socket

class TcpClient():

    def Main(self):
        print("TcpClient")
        host = "127.0.0.1"
        port = 5000

        sock = socket.socket()
        sock.connect((host, port))

        message = input("->")
        while message != "q":
            sock.send(message.encode('utf-8')) #
            data = sock.recv(1024).decode('utf-8') #
            print("Received from server: ", data) #str(data))
            message = input("->")
        sock.close()


x = TcpClient()
if __name__ == "__main__":
    x.Main()