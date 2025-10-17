import socket
import os

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345

filename = input("Enter file name to send: ")

if not os.path.exists(filename):
    print("File not found!")
else:
    # Send filename first
    client_socket.sendto(filename.encode(), (host, port))

    # Send file data
    with open(filename, "rb") as f:
        data = f.read(1024)
        while data:
            client_socket.sendto(data, (host, port))
            data = f.read(1024)
        client_socket.sendto(b"EOF", (host, port))
    print("File sent successfully!")

client_socket.close()
    