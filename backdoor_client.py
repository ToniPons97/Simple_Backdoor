import socket
import argparse
import subprocess


def receiveConfig():
    parser = argparse.ArgumentParser(description="Simple TCP client.")
    parser.add_argument("-ip", "--ip_address", help="Input IP address to list.")
    parser.add_argument("-p", "--port", help="Define port to listen on.")
    return parser.parse_args()

config = receiveConfig()

if config.ip_address and config.port:
    srv_addr = config.ip_address
    srv_port = int(config.port)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((srv_addr, srv_port))
    print(f"Established connection with {config.ip_address}")
    while True:
        message = input("> ")
        s.sendall(message.encode())
except KeyboardInterrupt:
    print("\n[CONTROL + C] detected... quiting... bye bye... fuck off...")