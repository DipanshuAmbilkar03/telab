import socket

# create a socket
client_socket = socket.socket()
host = socket.gethostname()
port = 12345
client_socket.connect((host, port))

# hello
client_socket.send("Hello from Client!".encode())
msg = client_socket.recv(1024).decode()
print("Server:", msg)

# send a file
filename = "sample.txt"   
with open(filename, "rb") as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)
print("File sent successfully!")

client_socket.close()