#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

try:
    METHOD = sys.argv[1] #Método SIP
    RECEPTOR = sys.argv[2].split(':')[0]  # Receptor@IP.
    IP = RECEPTOR.split('@')[-1] # IP.
    PORT = int(sys.argv[2].split(':')[1]) # PuertoSIP.
    
except (IndexError, ValueError):
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")


# Cliente UDP simple.

# Dirección IP del servidor.



# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((IP, PORT))


    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    try:
        print("Enviando: " + LINE)
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))
        print("EL RECEPTOR ES",RECEPTOR)
        print("EL PUERTO ES", PORT)
        print("Terminando socket...")
        print("Fin.")
    except ConnectionRefusedError:
        print("ERROR DE CONEXIÓN")
