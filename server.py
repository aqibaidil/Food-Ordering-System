import socket
import os
import sys
import json
import random
import errno
import math
from multiprocessing import Process

def process_start(s_sock):

	s_sock.send(str.encode('\n\t\t\t\t*#*#*WEST-TURN CAFE*#*#*\t\t\t'))
    	while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        #process/calculation
        try:
            menu, num , value = data.split(":")
            option = str(menu)
            quantity = int(num)
            price = float(value)

            if option[0]  == 'A':
                option = 'Spaghetti Aglio Olio'
                price = 20
                ans = quantity * (price)
            elif option[0] == 'B':
                option = 'Spaghetti Carbonara'
                price = 16
                ans = quantity * (price)
            elif option[0] == 'C':
                option = 'Chicken Chop'
                price = 20
                ans = quantity * (price)
            elif option[0] == 'D':
                option = 'Margherita Pizza'
                price = 25
                ans = quantity * (price)
            elif option[0] == 'E':
                option = 'Hawaiian Chicken Pizza'
                price = 23
                ans = quantity * (price)
            elif option[0] == 'F':
                option = 'Tiramisu Cake'
                price = 10
                ans = quantity * (price)
            elif option[0] == 'G':
                option = 'Caramel Latte'
                price = 8
                ans = quantity * (price)
            elif option[0] == 'H':
                option = 'Americano'
                price = 6
                ans = quantity * (price)
            elif option[0] == 'I':
                option = 'Espresso'
                price = 7
                ans = quantity * (price)
            elif option[0] == 'J':
                option = 'Ice Blended Chocolate'
                price = 8
                ans = quantity * (price)
            elif option[0] == 'K':
                option = 'Oreo Frappucino'
                price = 10
                ans = quantity * (price)
            elif option[0] == 'L':
                option = 'Orange Juice'
                price = 9
                ans = quantity * (price)
            else:
                answer = ('ERROR')

            sendtoCli = (str(option)+ '.... RM'+ str(price)+ ' ['+ str(quantity) + ']: RM' + str(ans))
            print(sendtoCli)
            print ('ORDER RECEIVED!!')
            #break
