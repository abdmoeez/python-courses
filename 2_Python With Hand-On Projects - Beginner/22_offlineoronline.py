import socket

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(2)
    sock.connect(("google.com",443))
    print("You are online!")
except socket.error:
    print("You are offline!")
finally:
    sock.close()