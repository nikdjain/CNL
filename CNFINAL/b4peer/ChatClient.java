import java.io.*;
import java.net.*;
class ChatClient
{
public static void main(String argv[]) throws Exception
{
String sentence;
String sentenceFromServer;

Socket clientSocket = new Socket("localhost", 7021);
System.out.println("Connected to Server. Start Chatting with Server:");

BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
DataOutputStream outToServer =new DataOutputStream(clientSocket.getOutputStream());
BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

while(true)
{
sentence = inFromUser.readLine();

outToServer.writeBytes(sentence + '\n');

sentenceFromServer = inFromServer.readLine();

System.out.println("FROM SERVER: " +sentenceFromServer);

}
}
}
