import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print(f"Conectado al servidor en {HOST}:{PORT}")
    while True:
        message = input("Ingrese un mensaje (o 'DESCONEXION' para cerrar): ")
        if message == "DESCONEXION":
            break
        client.sendall(message.encode())
        response = client.recv(1024).decode()
        print(f"Servidor responde: {response}")
except ConnectionRefusedError:
    print(f"No se pudo conectar al servidor en {HOST}:{PORT}")
except KeyboardInterrupt:
    client.close()
    print("\nConexión cerrada por el usuario")
finally:
    client.close()
    print("Conexión cerrada")