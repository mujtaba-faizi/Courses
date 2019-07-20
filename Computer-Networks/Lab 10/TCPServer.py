from socket import *
import time

serverPort=15000

serverSocket=socket(AF_INET,SOCK_STREAM)

serverSocket.bind(("",serverPort))

serverSocket.listen(40)

print "Ready to serve"

while 1:
	connectionSocket,clientAddress=serverSocket.accept()
	message=connectionSocket.recv(2048)
	print clientAddress
	ctime=time.asctime(time.localtime(time.time()))
	modifiedMessage="Welcome: "+ message.split(':')[0]+ ctime

	connectionSocket.send(modifiedMessage)
	connectionSocket.close()
