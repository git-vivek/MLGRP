#!/usr/bin/python3
import socket                   

port = 8888
s = socket.socket()             
host = socket.gethostname()     
s.bind((host, port))        
s.listen(5)                 

print('Server listening....')

while True:
    conn, addr = s.accept() 
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    print(conn)
    filename='mytext.txt'
    print('Hello1')
    f =  open(filename,'r')
    print ('Hello2')
    l = f.read()
    a=str.encode(l)
    print ('Hello3')
    #while (l):
    conn.send(a)
    print('Hello4')
    print('Sent ',repr(a))
      # l = f.read()
    # f.close()

    print('Done sending')
    #conn.send('Thank you for connecting')
    conn.close()
