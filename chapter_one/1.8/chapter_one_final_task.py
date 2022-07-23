from typing import Dict, List, Optional


class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    __ip_incrementor: int = 1

    def __init__(self):
        self.ip = Server.__ip_incrementor
        self.buffer: List[Data] = []
        self.linked_router: Optional[Router] = None
        Server.__ip_incrementor += 1

    def send_data(self, data: Data) -> None:
        self.linked_router.buffer.append(data)

    def get_ip(self):
        return self.ip

    def get_data(self):
        receive_data = self.buffer[:]
        self.buffer.clear()
        return receive_data


class Router:
    def __init__(self):
        self.servers: Dict[int, Server] = {}
        self.buffer: List[Data] = []

    def link(self, server: Server) -> None:
        self.servers[server.ip] = server
        server.linked_router = self

    def unlink(self, server: Server) -> None:
        self.servers.pop(server.ip)
        server.linked_router = None

    def send_data(self) -> None:
        for data in self.buffer:
            try:
                self.servers[data.ip].buffer.append(data)
            except KeyError:
                pass
        self.buffer.clear()
