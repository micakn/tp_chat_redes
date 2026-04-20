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

## Mejora futura
Se podría implementar multihilo para múltiples clientes simultáneos.