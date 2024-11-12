# Write a python programming to get my system IP addresses using socket

import socket
# from socket import socket

# def get_ip_addresses():
    
#     # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s = socket.getaddrinfo("google.com", 80, proto=socket.IPPROTO_TCP)

#     return s

# get = get_ip_addresses()
# print(get)

domains = [
    'google.com', 
    'uniosun.edu.ng', 
    'futa.edu.ng'
]

for i in domains:
    print(i)
    s = socket.getaddrinfo(i, 80, proto=socket.IPPROTO_TCP)
    # print(s, end="\n")
    for n in s:
        print(n)
    
