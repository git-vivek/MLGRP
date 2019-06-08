#!/usr/bin/python3
import socket                   

s = socket.socket()         
host = socket.gethostname()     
port = 8888                    

s.connect((host, port))


with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data=s.recv(1024)
        b=data.decode()
        print('data=%s',(b))
        
        if not data:
            break
        
        f.write(b)
        print("successful")

f.close()
#print('Successfully get the file')
s.close()
print('connection closed')
