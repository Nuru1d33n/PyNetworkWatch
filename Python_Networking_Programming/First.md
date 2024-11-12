Get* in socket

# 1. To get hostname / Computer Name

1. Using command
   whoami (all OS)
2. Using Python (socket) => all OS
   socket.gethostname()

# 2. Get public network interface / localhost IP

    1. Using command
		- For windows
			ipconfig,
		- For Linux distributions
			ifconfig

    2. Using socket
		socket.gethostbyname(socket.gethostname()))



# 3. To get dns information

    Using python
	socket.getnameinfo()
