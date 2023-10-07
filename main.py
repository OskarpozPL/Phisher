import platform
import socket

operating_system = platform.system()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

def clear():
  if operating_system == "Windows":
    os.system("cls")
  elif operating_system == "Linux":
    os.system("clear")
  else:
    print("[-] We do not support your operating system.")
    exit()

clear()

print(" ____    _   _   ___   ____    _   _   _____   ____  ")
print("|  _ \  | | | | |_ _| / ___|  | | | | | ____| |  _ \ ")
print("| |_) | | |_| |  | |  \___ \  | |_| | |  _|   | |_) |")
print("|  __/  |  _  |  | |   ___) | |  _  | | |___  |  _ < ")
print("|_|     |_| |_| |___| |____/  |_| |_| |_____| |_| \_")

print("\n")

print("-------------------------------------------------")

print("\n")

print(f"[*] Operating system: {operating_system}")
print(f"[*] Hostname: {hostname}")
print(f"[*] IP Address: {ip_address}")

print("\n")

print("-------------------------------------------------")
