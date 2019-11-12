import socket
import os
import threading

class Server:
    clients = []
    def create(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.port = 9999
        self.sock.bind(("localhost",self.port))
        print("Socket bound successfully")
        self.chatWindow()
        return 

    def receiver(self):
        while True:
            msg , addr = self.sock.recvfrom(1024)
            if(addr not in self.clients):
                self.clients.append(addr)
            for client in self.clients:
                if client != addr:
                    self.sock.sendto(msg,client)
            
    
    def chatWindow(self):
        self.receiver()

if __name__ == "__main__":
    server = Server()
    server.create()
