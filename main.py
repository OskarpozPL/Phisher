import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("--------- DOXBIN ----------")
print("    Copyright (c) 2023.")
print("    All rights reserved.")
print("---------------------------")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
