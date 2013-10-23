import socket
import sys
import select

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))

running = True
while running:
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])
    if inputready == [my_socket]:
        for s in inputready:
            msg = s.recv(1024)
            if msg:
                print msg
            else:
                print "Disconnected from server!"
                running = False
    elif inputready == [sys.stdin]:
        input_from_user = sys.stdin.readline()
        my_socket.sendall(input_from_user)


# data = my_socket.recv(1024)

# print "received:\n%s" %data

# input_from_user = sys.stdin.readline()

# my_socket.sendall(input_from_user)


# data2 = my_socket.recv(1024)
# print "\n%s" %data2


my_socket.close()

