import socket
import os
import threading


class Server:
    clients = {}
    def create(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.port = 9999
        self.s.bind(('127.0.0.1',self.port))
        self.chatWindow()
        return

    def receiver(self):
        while True:
            msg,addr = self.s.recvfrom(1024)
            msg_decode = msg.decode('utf-8')
            if("xoxoxnew" in msg_decode):
                # get username and map to addr . send everyone else the new user added
                self.username = msg_decode.split('|')[1]
                self.clients[self.username] = addr
                for client in self.clients.values():
                    if client != addr:
                        self.s.sendto(bytes(f"{self.username} joined",'utf-8'),client)
            else:
                #grab the destination username from msg and then send the message to only that user
                self.username = msg_decode.split('|')[0]
                self.message = msg_decode.split('|')[1]
                #check whether user is present in the client list and also not the same username as the sender
                if self.username in self.clients and self.clients[self.username] != addr:
                    self.s.sendto(bytes(self.message,'utf-8'),self.clients[self.username])
                else:
                    self.s.sendto(bytes("user not in chat",'utf-8'),addr)


    def chatWindow(self):
        os.system("clear")
        print("Chat Server up and running")
        threadR = threading.Thread(target=self.receiver)
        threadR.start()

if __name__ == "__main__":
    server = Server()
    server.create()

