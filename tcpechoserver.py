#!/usr/bin/python



import sys
import socket
import wrapsock

def main(argv):
    # My code here
    print "tcpechoserver"
    listenfd = wrapsock.Socket(socket.AF_INET, socket.SOCK_STREAM, 0);
    pass

if __name__ == "__main__":
    main(sys.argv)


'''
int listenfd, connfd;
pid_t childpid;
socklen_t clilen;
struct sockaddr_in cliaddr, servaddr;

int i = 0;

printf("waiting for debugger to attach\n");
while (i) {
sleep(1);
printf(".");
}


listenfd = Socket(AF_INET, SOCK_STREAM, 0);

bzero(&servaddr, sizeof(servaddr));
servaddr.sin_family = AF_INET;
servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
servaddr.sin_port = htons(SERV_PORT);

Bind(listenfd, (SA *) &servaddr, sizeof(servaddr));

Listen(listenfd, LISTENQ);

for ( ;  ;  ) {
clilen = sizeof(cliaddr);
connfd = Accept(listenfd, (SA *) &cliaddr, &clilen);

if ((childpid = Fork()) == 0) {
Close(listenfd);    // close listening socket
str_echo(connfd);   // process the requeest
exit(0);
}
Close(connfd);      // parent closes the connected socket
}


return 0;

'''
