from tcp_server import server
from tcp_udp_clients import tcp_client
import time

# server("google.com", 80)


time.sleep(2)
tcp_client("www.reddit.com", 80, "/r/trees.json")