import socket
import time

HOST = '127.0.0.1'
PORT = 5000
TIMEOUT = 60

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
print(f"Servidor escuchando en {HOST}:{PORT}")
server.settimeout(TIMEOUT)

try:
    while True:
        try:
            client_socket, client_address = server.accept()
            print(f"Conexión recibida de {client_address}")
            with client_socket:
                while True:
                    data = client_socket.recv(1024).decode()
                    if not data or data == "DESCONEXION":
                        print(f"Servidor desconectado de {client_address}")
                        break
                    time.sleep(1)
                    print(f"Cliente envia: {data}")
                    client_socket.sendall(data.upper().encode())
        except socket.timeout:
            print(f"No hubo actividad durante {TIMEOUT} segundos. Cerrando el servidor.")
            break
finally:
    server.close()
    print("Servidor detenido")
        
