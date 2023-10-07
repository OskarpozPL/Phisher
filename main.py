import os
import platform
import socket

operating_system = platform.system()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

black   = "\033[30m"
red     = "\033[31m"
green   = "\033[32m"
yellow  = "\033[33m"
blue    = "\033[34m"
magenta = "\033[35m"
cyan    = "\033[36m"
white   = "\033[37m"
reset   = "\033[m"

def clear():
  if operating_system == "Windows":
    os.system("cls")
  if operating_system == "Linux":
    os.system("clear")
  else:
    print("{red}[-] We do not support your operating system.{reset}")
    exit()

clear()

print(" ____    _   _   ___   ____    _   _   _____   ____   Copyright (c) 2023. ")
print("|  _ \  | | | | |_ _| / ___|  | | | | | ____| |  _ \  All rights reserved.")
print("| |_) | | |_| |  | |  \___ \  | |_| | |  _|   | |_) |                     ")
print("|  __/  |  _  |  | |   ___) | |  _  | | |___  |  _ <                      ")
print("|_|     |_| |_| |___| |____/  |_| |_| |_____| |_| \_                      ")

print("\n")

print("-------------------------------------------------")

print("\n")

print(f"{blue}[*] Operating system: {operating_system}{reset}")
print(f"{blue}[*] Hostname: {hostname}{reset}")
print(f"{blue}[*] IP Address: {ip_address}{reset}")

print("\n")

print("-------------------------------------------------")

print("\n")

print("1. Search for networks in the area")
print("2. Display passwords for networks in your area")
print("3. Exit")

print("\n")

choice = input("> ")

if choice == "1":
  print("Coming soon :(")
  exit()

if choice == "2":
  print("Comming soon :(")
  exit()

if choice == "3":
  exit()
