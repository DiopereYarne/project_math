import logging
import socket

logging.basicConfig(level=logging.DEBUG)


logging.info("Starting server...")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serversocket.bind((host, port))

serversocket.listen(5)


while True:
    logging.info("Waiting for a connection...")
    clientsocket, addr = serversocket.accept()
    logging.info(f"Got a connection from {addr}")

    message = "Thank you for connecting"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()

