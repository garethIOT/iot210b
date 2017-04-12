import socket
import sys

if len(sys.argv) > 1:
  UDP_IP = sys.argv[1]
else:
  UDP_IP = "::1"  # localhost IPv6 style

if len(sys.argv) > 2:
  UDP_PORT = int(sys.argv[2])
else:
  UDP_PORT = 5005

MESSAGE = "Hello IPv6 World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET6, # Internet
          socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
