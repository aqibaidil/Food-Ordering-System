import socket
import signal
import sys

cSocket = socket.socket()
host = '192.168.249.4'
port = 8989

print('Waiting For Connection')
try:
	cSocket.connect((host, port))
except socket.error as e:
	print(str(e))

Response = cSocket.recv(2048)
print(Response.decode("utf-8"))
