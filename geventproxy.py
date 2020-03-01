import gevent
from gevent.server import StreamServer

from gevent import monkey

monkey.noisy = False
monkey.patch_all()
import socket
import select
from functools import partial

BUFSIZE = 4096


def copy(srcsocket, destsocket):
    data = srcsocket.recv(BUFSIZE)
    destsocket.sendall(data)


def proxy_to(endpoint, clientsocket, address):
    destsocket = socket.create_connection(endpoint)
    while not clientsocket.closed or not destsocket.closed:
        readable, _, _ = select.select([clientsocket, destsocket], [], [], 0.1)
        for ready_to_read in readable:
            if ready_to_read == clientsocket:
                # print("Copying client to dest")
                copy(clientsocket, destsocket)
            elif ready_to_read == destsocket:
                # print("Copying dest to client")
                copy(destsocket, clientsocket)

        # print("continuing...")


def make_tcp_proxy(server_addr, dest_ddr):
    """Creates a proxy server listening on `addr` that forwards requests to server running on `toaddr`

    Arguments:
        server_addr {[tuple]} -- listening address endpoint (ip,port) e.g ("127.0.0.1", 1600)
        dest_addr {[tuple]} -- proxied server address endpoint (ip,port) e.g ("127.0.0.1", 8080)


    """
    handler = partial(proxy_to, dest_addr)
    proxy_server = StreamServer(server_addr, handler)
    return proxy_server


if __name__ == "__main__":
    listenining_addr = ("127.0.0.1", 1600)
    dest_addr = ("127.0.0.1", 8080)
    print(f"Starting proxy server on http://{listenining_addr[0]}:{listenining_addr[1]} ..")

    server = make_tcp_proxy(listenining_addr, dest_addr)
    server.serve_forever()
