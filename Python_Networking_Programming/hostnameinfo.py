# Get the hostname informations

import socket

# Interact with get* in socket 
hostname = socket.gethostname()
print(hostname)

ip = socket.gethostbyname(hostname)
print(ip)

addr = socket.gethostbyaddr(socket.gethostbyname(hostname))
print(addr)


# enter_ip = input("Enter IP address: ")
# get_info = socket.gethostbyaddr(enter_ip)
# print(get_info)

# sockaddr = ('1.1.1.1', 21)

# name_info = socket.getnameinfo(sockaddr, 0)
# print(name_info)

# result = ''

for i in range(1, 65536):
    sockaddr = '8.8.8.8', i
    name_info = socket.getnameinfo(sockaddr, 0)
    print(i, ':' , name_info[1])


    # result = f"{i}: {name_info[0]}\n"
    # print(result)

# with open('ports.txt', 'w') as f:
#     f.write(result)
# print(result)






# dism /online /add-capability /capabilityname:OpenSSH.Serverss~~~~0.0.1.0
# Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
# Start-Service sshd
# Set-Service -Name sshd -StartupType 'Automatic'
# New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Protocol TCP -Action Allow -LocalPort 22
# Get-Service sshd
