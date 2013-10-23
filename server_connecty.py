import socket, sys, select

def format(message):
    if "::" in message:
        message = message.split("::", 1)
        new_message = "[%s]" %message[0] + " " + message[1]
        return new_message
    else: 
        return message

def open_connection(my_socket):
    running = True
    while running:
        inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])
        for s in inputready:
            if s == my_socket:
                msg = s.recv(1024)
                if msg:
                    print format(msg)
                else:
                    print "Disconnected from server!"
                    running = False
            elif s == sys.stdin:
                input_from_user = sys.stdin.readline()
                my_socket.sendall(input_from_user)

def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("localhost", 5555))

    open_connection(my_socket)

    my_socket.close()

main()