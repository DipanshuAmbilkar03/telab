import socket

print("=== DNS Lookup Program ===")
print("1. Find IP from Domain Name")
print("2. Find Domain Name from IP")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    domain = input("Enter Domain Name (e.g., google.com): ")
    try:
        # ip = socket.gethostbyname(domain)
        info = socket.getaddrinfo(domain, None)
        for result in info:
            print(result[4][0])

        print(f"IP address of {domain} is: {info}")
    except socket.gaierror:
        print("Invalid domain name or DNS lookup failed!")

elif choice == "2":
    ip = input("Enter IP Address (e.g., 8.8.8.8): ")
    try:
        domain = socket.gethostbyaddr(ip)
        print(f"Domain name for {ip} is: {domain[0]}")
    except socket.herror:
        print("Reverse DNS lookup failed or invalid IP address!")

else:
    print("Invalid choice! Please enter 1 or 2.")
