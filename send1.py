#!/usr/bin/python3
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
t_ip='127.0.0.1'
t_port=8888
while True:
    f=open('a','r+')
    l=f.read()
    #data=l.encode('ascii')
    s.sendto(str.encode(l),(t_ip,t_port))
    #print(s.recvfrom(1000))
    
