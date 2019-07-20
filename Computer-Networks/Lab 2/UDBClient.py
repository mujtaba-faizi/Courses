from socket import *     # import socket module
import time
serverIP='10.99.15.252'
serverPort=15000   #port where server is listening
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input("Input lowercase sentence:")
clientSocket.sendto(message,(serverIP, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage     # print the received message
clientSocket.close()      # Close the socket
