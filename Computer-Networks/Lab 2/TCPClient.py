from socket import *
import time
serverIP='10.99.15.252'
serverPort=15000   #port where server is listening
sentence=raw_input('Input lowercase sentence:')
send_time = time.time()
for i in range(15):
    clientSocket=socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((serverIP,serverPort))
    clientSocket.send(sentence)
    modifiedSentence=clientSocket.recv(1024)
receive_time = time.time()
rtt = round(receive_time - send_time, 3)
print 'From Server:',modifiedSentence

avg=rtt/15
print "Average RTT for one packet = ", avg
clientSocket.close()
