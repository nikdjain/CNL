import java.io.*;
import java.net.*;
class ChatServer
{
public static void main(String argv[]) throws Exception
{
String sentenceFromClient;
String sentence;

ServerSocket welcomeSocket = new ServerSocket(7021);
System.out.println("ServerSocket awaiting connections...");

Socket connectionSocket = welcomeSocket.accept();
System.out.println("Connection from " + connectionSocket);

BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());

while(true)
{
sentenceFromClient = inFromClient.readLine();

System.out.println("FROM CLIENT: " +sentenceFromClient);

sentence = inFromUser.readLine();

outToClient.writeBytes(sentence + '\n');

}
}
}
 
