import socket
import os
import threading

class Client:
    def create(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.ip = "127.0.0.1"
        self.port = 9999
        self.username = input("Enter username:")
        self.s.sendto(bytes(f"xoxoxnew|{self.username}",'utf-8'),(self.ip,self.port))
        self.chatWindow()

    def sender(self):
        flag = 0
        while True:
            #get the username to send the message to 
            if flag == 0:
                self.tosend = input("Enter the user to send the message to :")
                flag = 1
            msg = input()
            if msg == "exit":
                flag = 0
                continue
            msg = f"{self.tosend}|"+f"{self.username}>" + msg
            msg = bytes(msg,'utf-8')
            self.s.sendto(msg,(self.ip,self.port))

    def receiver(self):
        while True:
            msg , addr = self.s.recvfrom(1024)
            print(msg.decode('utf-8'))

    def chatWindow(self):
        os.system("clear")
        print("Client Chat Window")
        threadS = threading.Thread(target=self.sender)
        threadR = threading.Thread(target=self.receiver)
        threadS.start()
        threadR.start()

if __name__ == "__main__":
    client = Client()
    client.create()

