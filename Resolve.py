import socket


class Resolver:
    def __init__(self):
        self.cache = {}

    def __call__(self, host):
        if host not in self.cache:
            self.cache[host] = socket.gethostbyname(host)
        return self.cache[host]

    def clear(self):
        self.cache.clear()

    def has_host(self, host):
        return host in self.cache
