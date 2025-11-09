import socket

print("=== DNS Lookup Program ===")
print("1. Find IP from Domain Name")
print("2. Find Domain Name from IP")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    domain = input("Enter Domain Name (e.g., google.com): ")
    try:
        info = socket.getaddrinfo(domain, None)
        print(f"\nIP addresses for {domain}:\n")
        for result in info:
            family = result[0]
            ip_addr = result[4][0]

            # Check address family and print accordingly
            if family == socket.AF_INET:
                print(f"IPv4: {ip_addr}")
            elif family == socket.AF_INET6:
                print(f"IPv6: {ip_addr}")

        print("\n DNS Lookup Successful!\n")

    except socket.gaierror:
        print("Invalid domain name or DNS lookup failed!")

elif choice == "2":
    ip = input("Enter IP Address (e.g., 8.8.8.8): ")
    try:
        domain = socket.gethostbyaddr(ip)
        print(f"\nIPv4/IPv6 Address: {ip}")
        print(f"Domain name for this IP is: {domain[0]}")
        print("\n Reverse DNS Lookup Successful!\n")
    except socket.herror:
        print("Reverse DNS lookup failed or invalid IP address!")

else:
    print("Invalid choice! Please enter 1 or 2.")
