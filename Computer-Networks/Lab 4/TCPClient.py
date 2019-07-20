from socket import *
import base64
serverIP ='localhost'
serverPort=50021
clientSocket = socket(AF_INET, SOCK_STREAM)
sentence = raw_input ('enter the file name : ')
clientSocket.connect((serverIP,serverPort))
clientSocket.send(sentence)
print clientSocket.recv(1024)
print clientSocket.recv(1024)
print clientSocket.recv(1024)
print clientSocket.recv(1024)
content=clientSocket.recv(1024)
f=open(sentence,"wb")    #create a file
f.write(base64.b64decode(content))     #writes the content received from server into the file
clientSocket.close()
