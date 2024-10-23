import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Función para iniciar el cliente UDP
def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.bind(('0.0.0.0', 5001))  # Escuchar en todas las interfaces de red de la computadora
    
    while True:
        mensaje, direccion = cliente.recvfrom(1024)
        texto_chat.config(state=tk.NORMAL)
        texto_chat.insert(tk.END, f'Servidor: {mensaje.decode("utf-8")}\n')
        texto_chat.config(state=tk.DISABLED)

# Función para enviar mensajes desde el cliente al servidor
def enviar_mensaje():
    mensaje = entrada_texto.get()
    # Reemplaza '192.168.1.2' con la IP del servidor
    cliente.sendto(mensaje.encode('utf-8'), ('192.168.233.245', 5000)) 
    texto_chat.config(state=tk.NORMAL)
    texto_chat.insert(tk.END, f'Cliente: {mensaje}\n')
    texto_chat.config(state=tk.DISABLED)
    entrada_texto.delete(0, tk.END)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title('Cliente Chat')

# Cuadro de texto para mostrar el chat
texto_chat = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, width=50, height=20)
texto_chat.grid(row=0, column=0, columnspan=2)

# Cuadro de entrada para escribir mensajes
entrada_texto = tk.Entry(root, width=40)
entrada_texto.grid(row=1, column=0)

# Botón para enviar el mensaje
boton_enviar = tk.Button(root, text='Enviar', command=enviar_mensaje)
boton_enviar.grid(row=1, column=1)

# Iniciar el hilo del cliente
cliente_hilo = threading.Thread(target=iniciar_cliente)
cliente_hilo.daemon = True
cliente_hilo.start()

# Crear socket para el cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

root.mainloop()
