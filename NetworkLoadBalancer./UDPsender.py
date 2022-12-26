import socket
import sys

def runit():
   UDP_IP = ip
   UDP_PORT = 6380
   MESSAGE = b"Hello, UDP server!"
   
   print("UDP target IP: %s" % UDP_IP)
   print("UDP target port: %s" % UDP_PORT)
   print("message: %s" % MESSAGE)
   
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
   sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

if __name__ == '__main__':
   ip = sys.argv[1] 
   runit()
