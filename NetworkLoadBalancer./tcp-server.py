#!/usr/bin/env python

import socket


TCP_IP = '0.0.0.0'
TCP_PORT = 6381
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

#Socket object see https://docs.python.org/3/library/socket.html , sock stream is a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binding ip and port to a socket instance
s.bind((TCP_IP, TCP_PORT))
#listen() method puts server in a listing mode
s.listen(1)

#https://stackoverflow.com/questions/65171871/what-is-conn-addr-s-accept-in-python-socket return variable conn/addr return pair value
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print 'received data:', data
    conn.send('Returned from TCP server #1: ' + data)  # echo
conn.close()
