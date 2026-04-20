import socket
import sqlite3
from datetime import datetime

# =========================
# CONFIGURACIÓN GENERAL
# =========================
# Dirección y puerto donde el servidor va a escuchar conexiones
HOST = "localhost"
PORT = 5000

# Nombre de la base de datos SQLite
DB_NAME = "mensajes.db"


# =========================
# BASE DE DATOS
# =========================
def inicializar_db():
    """
    Esta función crea la base de datos y la tabla 'mensajes' si no existen.
    Se ejecuta una sola vez al iniciar el servidor.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Creamos la tabla con los campos pedidos en la consigna
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

        print("Base de datos inicializada correctamente.")

    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")
        raise


def guardar_mensaje(contenido, fecha_envio, ip_cliente):
    """
    Inserta un mensaje en la base de datos.
    Se llama cada vez que un cliente envía un mensaje.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        """, (contenido, fecha_envio, ip_cliente))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Error al guardar el mensaje en la base de datos: {e}")


# =========================
# SERVIDOR TCP
# =========================
def iniciar_servidor():
    """
    Función principal del servidor.
    - Inicializa la base de datos
    - Crea el socket
    - Escucha conexiones
    - Recibe mensajes y responde
    """
    inicializar_db()

    try:
        # Crear socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:

            # Permite reutilizar el puerto si el servidor se reinicia
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Asociar socket a dirección y puerto
            servidor.bind((HOST, PORT))

            # Poner el servidor en modo escucha
            servidor.listen(1)

            print(f"Servidor escuchando en {HOST}:{PORT}...")

            # Loop principal del servidor
            while True:
                # Espera una conexión de cliente
                conn, addr = servidor.accept()
                print(f"\nConexión aceptada desde {addr[0]}:{addr[1]}")

                # Manejo del cliente
                with conn:
                    while True:
                        datos = conn.recv(1024)

                        # Si no hay datos, el cliente se desconectó
                        if not datos:
                            print("El cliente cerró la conexión.")
                            break

                        # Decodificar mensaje
                        mensaje = datos.decode("utf-8").strip()

                        # Si el cliente quiere salir
                        if mensaje.lower() == "éxito":
                            print("El cliente solicitó salir.")
                            break

                        # Generar timestamp
                        fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        # Guardar mensaje en la base
                        guardar_mensaje(mensaje, fecha_envio, addr[0])

                        # Enviar respuesta al cliente
                        respuesta = f"Mensaje recibido: {fecha_envio}"
                        conn.sendall(respuesta.encode("utf-8"))

                        print(f"Mensaje recibido de {addr[0]}: {mensaje}")

                print("Conexión cerrada.")

    except OSError as e:
        print(f"Error del socket: {e}")
        print("Posible causa: puerto ocupado.")
    except sqlite3.Error as e:
        print(f"Error de base de datos: {e}")


# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_servidor()