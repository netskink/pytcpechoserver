

import socket
import error

def Socket( family, type, protocol):

    n = socket.socket(family, type, protocol)
    if ( n < 0):
        error.err_sys("socket error")
    return n

'''

int Socket(int family, int type, int protocol) {

    int n;

if ( (n= socket(family, type, protocol)) < 0) {
    err_sys("socket error");
}
return n;
}
'''