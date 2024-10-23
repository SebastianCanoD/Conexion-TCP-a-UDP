import socket

def udp_to_tcp_intermediary():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('localhost', 65432))  # Cambia 'IP_DEL_INTERMEDIARIO' por la dirección IP real

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(('localhost', 65433))  # Cambia 'IP_DEL_SERVIDOR' por la dirección IP real

    print("Intermediario UDP a TCP en funcionamiento...")

    while True:
        data, addr = udp_socket.recvfrom(1024)
        print(f"Recibido de UDP: {data.decode()}")
        tcp_socket.sendall(data)

if __name__ == "__main__":
    udp_to_tcp_intermediary()