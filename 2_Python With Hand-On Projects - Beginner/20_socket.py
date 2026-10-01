import socket

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(2)
    sock.connect(("google.com",21))
    print("Connection Successful")
except socket.error:
    print("Could not connect")
finally:
    sock.close()