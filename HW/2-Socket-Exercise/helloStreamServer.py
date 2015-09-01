# TCP Hello Server
# Open a server socket, say "hello" on connection
# Adapted from www.tutorialspoint.com/sockets
#

import socket as sock
import sys

if (len(sys.argv) !=2):
        print 'Usage: python helloServer.py <port-number>'
            exit()
            server_port = sys.argv[1]
            server_sock = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            server_sock.bind(('172.17.149.120',int(server_port)))
            print 'server socket bound on port '+server_port
            server_sock.settimeout(20)
            try:
                    server_sock.listen(int(server_port))
                    #
                    # connected_sock is a connection to remote host
                    # remote_addr is address of connecting host
                    #
                        (connected_sock,remote_addr) = server_sock.accept()

                            print "Connection from "+str(remote_addr)
                                connected_sock.send("Hello Python!\n")
                                    print "Closing socket"
                                        server_sock.close()
                                        except sock.timeout:
                                                print "Timed out waiting for connection"
                                                    server_sock.close()



