

import socket
import error

def Socket( family, type, protocol):

    n = socket.socket(family, type, protocol)
    if ( n < 0):
        error.err_sys("socket error")
    return n

