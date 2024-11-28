import socket
sock = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3306
result = sock. connect_ex(('127.0.0.1', port))
if result == 0:
print (port , "Port is open")
else:
print (port , "Port is not open")
sock. close ()
