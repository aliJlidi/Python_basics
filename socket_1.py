import socket
#inialize our socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#make a phone call to the target with the socket 
mysock.connect(('data.pr4e.org',80))
#now it wait for me to ask 
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#talk
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()