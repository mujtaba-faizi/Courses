from socket import *

#use the IP address of your neighbor running the server
serverName="192.168.1.112"
serverPort=51000

clientSocket = socket(AF_INET,SOCK_DGRAM)

#use your name here
message="Mr Bean"

clientSocket.sendto(message,(serverName,serverPort)) 

modifiedMessage,serverAddress=clientSocket.recvfrom(2048)

message="None of Your Business"

clientSocket.sendto(message,(serverName,serverPort))

#modifiedMessage,serverAddress=clientSocket.recvfrom(2048)

clientSocket.close()


