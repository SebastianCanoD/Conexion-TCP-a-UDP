import cv2
import socket
import struct
import pickle

# Configuración del socket UDP
udp_ip = "127.0.0.1"  # Dirección IP del receptor
udp_port = 5005       # Puerto del receptor

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

while True:
    # Recibir el tamaño del frame
    data, addr = sock.recvfrom(8)
    msg_size = struct.unpack("Q", data)[0]

    # Recibir el frame
    data, addr = sock.recvfrom(msg_size)
    frame = pickle.loads(data)

    # Mostrar el frame
    cv2.imshow('Receiving Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
sock.close()