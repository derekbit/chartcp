from chartcp.clientsocket import ClientSocket

s1 = ClientSocket("10.0.0.1", 9011)
response = s1.send("Hello")
s1.close()
