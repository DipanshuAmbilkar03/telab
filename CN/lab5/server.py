import socket

# Step 1: Create socket
server_socket = socket.socket()
host = socket.gethostname()
port = 12345
server_socket.bind((host, port))

# Step 2: Listen for connection
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connected with {addr}")

# Step 3: Say Hello
msg = conn.recv(1024).decode()
print("Client:", msg)
conn.send("Hello from Server!".encode())

# Step 4: Receive file
filename = "received_file.txt"
with open(filename, "wb") as f:
    print("Receiving file...")
    data = conn.recv(1024)
    while data:
        f.write(data)
        data = conn.recv(1024)
    print("File received successfully!")

conn.close()
