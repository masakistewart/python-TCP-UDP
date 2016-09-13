import socket


def tcp_client(target_host, target_port, path="/"):
    # transmition control protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_host, target_port))

    request_string = "GET %s HTTP/1.1\r\nHOST: %s\r\n\r\n" % (path, target_host)

    client_socket.send(request_string)

    response = client_socket.recv(4096)

    print(response)

def udp_client(target_host, target_port, payload, path="/",):
    # user datagram protocol
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_host, target_port))

    client.sendto(payload, (target_host, target_port))

    data, addr = client.recvfrom(9096)
    client.close()
    print(data)
