from socket import *
import os
import base64

serverPort=50021
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
            fl = open(os.path.join(root, name),"rb")   #opening file for reading
            content = base64.b64encode(fl.read())     #adding content


    return result,content
def size(path):
    if os.path.isfile(path):
        file_info = os.stat(path)
        return file_info.st_size

while 1:
    dict={}
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    a,data = find_all(sentence, "F:\Downloads")
    for u in a:

        b=str(size(u))    #size of file
        b+=" bytes"
        dict[u]=b   #maintaing dictionary of path and size
        connectionSocket.send(u)   #path of file
        connectionSocket.send(b)
    connectionSocket.send(data)   #content of file to copy in client machine
    connectionSocket.close()
