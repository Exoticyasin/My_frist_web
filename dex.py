
# Python Program to Get IP Address
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Device Name :" + hostname)
print("Your IP Address  :" + IPAddr)
