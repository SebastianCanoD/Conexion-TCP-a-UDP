import socket

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65433))  # Cambia 'IP_DEL_SERVIDOR' por la dirección IP real
    server_socket.listen()

    print("Servidor TCP esperando conexiones...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recibido: {data.decode()}")
            conn.sendall(data)

if __name__ == "__main__":
    start_tcp_server()