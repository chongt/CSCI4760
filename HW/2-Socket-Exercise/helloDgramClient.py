# helloDgramClient.py
# Purpose: Client for sockets from corresponding server.

from socket import *
serverName = '172.17.149.120'
serverPort = 21801
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence to be converted into UPPERCASE: ')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()


