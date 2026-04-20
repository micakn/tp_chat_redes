# TP Programación sobre Redes

## Descripción
Chat cliente-servidor en Python usando sockets TCP y SQLite.

## Funcionalidad
- El cliente envía mensajes
- El servidor los guarda en una base de datos
- El servidor responde con timestamp
- El cliente finaliza con "éxito"

## Requisitos
- Python 3
- sqlite3 (incluido)

## Ejecución

1. Ejecutar servidor:
   python server.py

2. Ejecutar cliente:
   python client.py

## Base de datos
Se crea automáticamente:
mensajes.db

## Ver mensajes guardados

python -c "import sqlite3; conn=sqlite3.connect('mensajes.db'); [print(r) for r in conn.execute('SELECT * FROM mensajes')]; conn.close()"

## Pruebas realizadas
Se realizaron pruebas locales ejecutando el servidor y el cliente en terminales separadas.

Se verificó que:
- El cliente se conecta correctamente al servidor
- El servidor recibe los mensajes enviados
- Los mensajes se almacenan en la base de datos SQLite
- El servidor responde con un timestamp para cada mensaje
- El cliente finaliza correctamente al escribir "éxito"
- El mensaje "éxito" no se almacena en la base de datos, ya que se utiliza como comando de finalización

## Mejora futura
Se podría implementar multihilo para permitir múltiples clientes simultáneamente.