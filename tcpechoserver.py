#!/usr/bin/python


import sys
import socket
import os

HOST = ""       # symbolic name meaning all available interfaces
PORT = 5000     # non privileged port


def main(argv):

    print "python tcp echo server"

    sock_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_listen.bind((HOST, PORT))
    sock_listen.listen(5)

    while 1:
        sock_connected, address_client = sock_listen.accept()
        print 'Client connected via host address ', address_client

        child_pid = os.fork()
        if child_pid == 0:
            # This is the child
            sock_listen.close()      # child closes the listening socket
            while 1:
                data = sock_connected.recv(1024)
                if not data:
                    sock_connected.close()
                    exit(0)
                if data.rstrip('\r\n') == 'exit':
                    sock_connected.close()
                    print 'Client disconnect via host address ', address_client
                    exit(0)
                sock_connected.sendall(data)
        else:
            # This is the parent
            sock_connected.close()   # parent closes the connected socket, accept will be called on listen socket

    # This server runs forever. This will never be reached.
    pass

if __name__ == "__main__":
    main(sys.argv)



