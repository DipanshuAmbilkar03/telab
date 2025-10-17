import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345
server_socket.bind((host, port))

print(f"UDP Server is running on {host}:{port}")

# Receive filename
filename, client_addr = server_socket.recvfrom(1024)
filename = filename.decode()
print(f"Receiving file: {filename} from {client_addr}")

# Receive file data
with open("received_" + filename, "wb") as f:
    while True:
        data, addr = server_socket.recvfrom(1024)
        if data == b"EOF":
            break
        f.write(data)
    print(f"File '{filename}' received successfully!")

server_socket.close()
