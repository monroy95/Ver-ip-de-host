#Convertir el nombre de un host a IP
"""Este script obtiene la direccion IP de un host, de cualquier pagina"""
import socket
hostname = 'maps.google.com'
direccion = socket.gethostbyname(hostname)
print('La direcion de ',hostname, ' es ', direccion)