# geventproxy

proxy tcp traffic from 1 server to another 

```python3
    listenining_addr = ("127.0.0.1", 1600)
    dest_addr = ("127.0.0.1", 8080)
    print(f"Starting proxy server on http://{listenining_addr[0]}:{listenining_addr[1]} ..")

    server = make_tcp_proxy(listenining_addr, dest_addr)
    server.serve_forever()

```