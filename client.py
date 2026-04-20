import socket

# Configuración del servidor
HOST = "localhost"
PORT = 5000


def iniciar_cliente():
    """
    Cliente que:
    - Se conecta al servidor
    - Envía múltiples mensajes
    - Termina al escribir 'éxito'
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:

            # Conectar al servidor
            cliente.connect((HOST, PORT))
            print(f"Conectado al servidor {HOST}:{PORT}")

            while True:
                mensaje = input("Escribí un mensaje (o 'éxito' para salir): ").strip()

                # Enviar mensaje
                cliente.sendall(mensaje.encode("utf-8"))

                # Si el usuario quiere salir
                if mensaje.lower() == "éxito":
                    print("Saliendo del cliente...")
                    break

                # Recibir respuesta
                respuesta = cliente.recv(1024).decode("utf-8")
                print(f"Respuesta del servidor: {respuesta}")

    except ConnectionRefusedError:
        print("No se pudo conectar. Ejecutá primero el servidor.")
    except OSError as e:
        print(f"Error de conexión: {e}")


if __name__ == "__main__":
    iniciar_cliente()