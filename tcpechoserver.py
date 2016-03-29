#!/usr/bin/python


import sys
import socket
import os
import json

HOST = ""       # symbolic name meaning all available interfaces
PORT = 5000     # non privileged port

'''
json messages look like this

request
{"msg_type": "status"}
response
{"msg_type": "status", "server_status": "ok"}

request
{"msg_type": "cmd", "cmd": "do thing 1"}
response
{"msg_type": "status", "cmd": "do thing 1", "status": "ok"}
'''

def parse_recv_msg(msg):
    try:
        parsed_json = json.loads(msg)
    except ValueError:
        # msg is not json, append <cr><lf> and exit
        # we stripped the carriage return line feed. add it back for echo
        msg += '\r\n'
        return msg

    # its json, but is it one of our message types
    if parsed_json['msg_type'] == 'status':
        msg = json.dumps({"msg_type": "status", "server_status": "ok"})
        msg += '\r\n'  # adding simply since i'm testing with telnet
        return msg

    if parsed_json['msg_type'] == 'cmd' and parsed_json['cmd'] == 'do thing 1':
        msg = json.dumps({"msg_type": "status", "cmd": "do thing 1", "status": "ok"})
        msg += '\r\n'  # adding simply since i'm testing with telnet
        return msg

    msg = "unrecognized json\r\n"
    return msg


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
                msg = data.rstrip('\r\n')
                if msg == 'exit':
                    sock_connected.close()
                    print 'Client disconnect via host address ', address_client
                    exit(0)
                # its could be json. If its json status message
                # send back server status
                msg = parse_recv_msg(msg)

                sock_connected.sendall(msg)
        else:
            # This is the parent
            sock_connected.close()   # parent closes the connected socket, accept will be called on listen socket

    # This server runs forever. This will never be reached.
    pass

if __name__ == "__main__":
    main(sys.argv)



