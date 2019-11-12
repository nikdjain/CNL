/*
Creating a TCP client 
1.Create a socket
2.Create a hint structure for the server we're connecting with
3.Connect to the server on the socket
4.While loop:
    Enter lines of tex
    Send to server
    Wait for response
    Display response
5.Close the socket
*/


#include<iostream>
#include<sys/types.h>
#include<unistd.h>
#include<sys/socket.h>
#include<netdb.h>
#include<arpa/inet.h>
#include<string.h>
#include<string>
#include<stdio.h>
#include<fstream>

using namespace std;

int main(){
    //Create a socket
    int sock = socket(AF_INET,SOCK_STREAM,0);
    if(sock < 0){
        cerr << "Error in creating a socket!" << endl;
        return -1;
    }

    int port = 9997;
    string ipAddress = "127.0.0.1";

    sockaddr_in hint;

    hint.sin_family = AF_INET;
    hint.sin_port = htons(port);
    inet_pton(AF_INET,ipAddress.c_str(),&hint.sin_addr);


    //Connect to the server on the socket

    int connectRes = connect(sock,(sockaddr*)&hint,sizeof(hint));
    if(connectRes < 0) {
        cerr << "Could not connect!" << endl;
        return -2;
    }

    char buf[4096];
    int bytesRecv;
    ofstream file;
    file.open("hello_copy.txt");
    //Receive from server`
    while(true){
        memset(buf,0,4096);
        bytesRecv = recv(sock,buf,4096,0);
        if(bytesRecv == 0) {
            cout << "File transfer complete" << endl;
            break;
        }
        file << string(buf,0,bytesRecv) << endl; 
    }
    file.close();
    // Close the socket
    close(sock);




    return 0;
}