from tcp_server import server
from tcp_udp_clients import tcp_client
import time

server("localhost", 8000)


time.sleep(2)
tcp_client("localhost", 8000)