#!/usr/bin/python3
import socket
import os
ip='127.0.0.1'
port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))

for i in range(1) :
    enc=s.recvfrom(1000)
    cont=enc[0].decode()
    f=open('next','w+')
    f.write(cont)
    print("File received")
    os.system("tar -cvzf next.tar.gz next")
    print("File compressed in gzip format")
    #print(enc)
    #new=enc.decode()
    #f=open('new','w+')

    #f.write(enc)
    #with open('file', 'w') as f:
     #   for item in enc:
      #      f.write("%s\n" % item)
    #s.sendto("file sent".encode('ascii'),enc[1])
    
