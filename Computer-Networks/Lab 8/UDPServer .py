from socket import *

#Use your own IP address here
serverIP="10.99.31.81"
serverPort=51000

serverSocket=socket(AF_INET,SOCK_DGRAM)

serverSocket.bind((serverIP,serverPort))

print "Ready to serve"

while 1:
    message,clientAddress=serverSocket.recvfrom(2048)
    modifiedMessage = "Welcome " + message + " Please enter your password:"
    serverSocket.sendto(modifiedMessage,clientAddress)
    message,clientAddress=serverSocket.recvfrom(2048)
    modifiedMessage = "That's a weird password! Anyhow how can I serve you?"
#message,clientAddress=serverSocket.recvfrom(2048)

