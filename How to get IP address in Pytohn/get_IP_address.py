import socket as SK

hostname = SK.gethostname()
ipaddress = SK.gethostbyname(hostname)

print(f"My IP Address : {ipaddress}")
