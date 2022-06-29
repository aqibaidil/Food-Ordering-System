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

print(			"\t\t\t* *** *** *** MENU LIST *** **** *** *\t\t\t\n")

print("   ------------------------------------------------------------------------------------")
print("   | [A]  Spaghetti Aglio Olio          RM20\n")
print("   | [B]  Spaghetti Carbonara           RM16\n")
print("   | [C]  Chicken Chop                  RM20\n")
print("   | [D]  Margherita Pizza              RM25\n")
print("   | [E]  Hawaiian Chicken Pizza        RM23\n")
print("   | [F]  Tiramisu Cake                 RM10/slice)\n")
print("   | [G]  Caramel Latte                 RM8\n")
print("   | [H]  Americano                     RM6\n")
print("   | [I]  Espresso                      RM7\n")
print("   | [J]  Ice Blended Chocolate         RM8\n")
print("   | [K]  Oreo Frappucino               RM10\n")
print("   | [L]  Orange Juice                  RM9\n")
print("   ------------------------------------------------------------------------------------")
print("=========================================================================================")
