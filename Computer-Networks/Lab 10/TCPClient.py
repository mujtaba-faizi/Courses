from socket import *
import time

#change the server IP
serverIP="192.168.1.7"
serverPort=15000

clientSocket = socket(AF_INET,SOCK_STREAM)

#change to your name
your_name='Nadeem Ahmed'


clientSocket.bind(("",5555)) 
clientSocket.connect((serverIP,serverPort)) 

message=your_name + " : Whats the time?"

clientSocket.send(message) 

modifiedMessage=clientSocket.recv(2048)

print modifiedMessage

time.sleep(1)

clientSocket.close()

