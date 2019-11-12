/*Basic socket programming 
1.Create a socket
2.Bind a socket to ip/port
3.Mark the socket for listening in
4.Accept a call
5.Close the listening socket
6.While receiving display message , echo message
7.Close socket

*/



#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<sys/stat.h>
#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>
// #include<fcntl.h>
#include<iostream>
#include<netdb.h>
#include<arpa/inet.h>
#include<string.h>
#include<fstream>

using namespace std;

int main(){
    //Create a socket
    int listening_socket = socket(AF_INET,SOCK_STREAM,0);
    if(listening_socket < 0){
        cerr << "Error in creating socket";
        return -1;
    }

    // Bind socket to ip/port
    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(9997);
    inet_pton(AF_INET,"0.0.0.0",&hint.sin_addr);  //try hint.sin_addr.s_addr = INADDR_ANY; later

    if(bind(listening_socket,(sockaddr*)&hint,sizeof(hint)) < 0){
        cerr<<"Can't bind ip/socket";
        return -2;
    }

    //Mark the socket for listening in
    if(listen(listening_socket,SOMAXCONN) < 0){
        cerr << "Can't listen";
        return -3;
    }

    //Accept a call
    sockaddr_in client;
    socklen_t  clientSize = sizeof(client);
    char host[NI_MAXHOST];
    char svc[NI_MAXSERV];

    int clientSocket = accept(listening_socket,(sockaddr*)&client,&clientSize);
    if(clientSocket < 0){
        cerr << "Problem with client connecting!";
        return -4;
    }

    //close listening socket
    close(listening_socket);
    
    memset(host,0,NI_MAXHOST);
    memset(svc,0,NI_MAXSERV);

    int result = getnameinfo((sockaddr *)&client,clientSize,host,NI_MAXHOST,svc,NI_MAXSERV,0);

    if(result){
        cout << host <<" connected on :" << svc << endl;
    }else {
        inet_ntop(AF_INET,&client.sin_addr,host,NI_MAXHOST);
        cout << host << " connected on :" << ntohs(client.sin_port);
    }

    //Send data from file
    char buf[4096];
    int fd,cont;
    char fname[254];
    fstream file;
    string line;
    file.open("hello.txt",ios::in | ios::binary);
    while(file){
        getline(file,line);
        cout << line << endl;
        send(clientSocket,line.c_str(),line.size()+1,0);
    }
    file.close();
    
    //Close the client socket
    close(clientSocket);

    return 0;
}