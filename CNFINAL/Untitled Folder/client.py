import socket
import os
import threading

class Client :
    
    def create(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.ip = "127.0.0.1"
        self.port = 9999
        #self.s.connect(('localhost',str(self.port)))
        print("Socket Created")
        self.username = input("Enter username: ")
#        self.s.sendto(bytes(f'{self.username} Conected','utf-8'),(self.ip,self.port))
        self.chatWindow()
        

    def sender(self):
        while True:
            msg = input()
            msg = bytes(f"{self.username}>" + msg,'utf-8')
            self.s.sendto(msg,(self.ip,self.port))

    def receiver(self):
        while True:
            msg,addr = self.s.recvfrom(1024)
            print(msg.decode('utf-8'))

    def chatWindow(self):
        os.system("clear")
        print("Chat Messenger Client")
        threadS = threading.Thread(target=self.sender)
        threadR = threading.Thread(target=self.receiver)
        threadS.start()
        threadR.start()

if __name__ == "__main__":
    client = Client()
    client.create()
