import platform
import socket

operating_system = platform.system()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Operating system: {operating_system}")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
