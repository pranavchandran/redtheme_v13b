# Wrapping an Exsiting file descriptor as a file object
# Open a low level file descriptor

import os
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)
# Turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print('Got connection from', addr)
    # Make text-mode file wrappers for scoket read/write
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
    # echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

import sys
# Create a binary-mode file for stdout
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()
