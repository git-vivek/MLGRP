#!/usr/bin/python3
import socket
ip='0.0.0.0'
port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))

while True:
    enc=s.recvfrom(1000)
    
    #print(enc)
    #new=enc.decode()
    #f=open('new','w+')

    #f.write(enc)
    with open('file', 'w') as f:
        for item in enc:
            f.write("%s\n" % item)
    #s.sendto("file sent".encode('ascii'),enc[1])
    
