#!/usr/bin/python3
import socket                   

s = socket.socket()         
host = socket.gethostname()     
port = 5656                    

s.connect((host, port))


with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data=s.recv(1024)
        print('data=%s',(data))
        if not data:
            break
        
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
