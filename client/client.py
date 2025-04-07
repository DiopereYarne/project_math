import logging
import socket

logging.basicConfig(level=logging.INFO)
logging.info("Starting client...")

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

clientsocket.connect((host, port))

msg = clientsocket.recv(1024)
print(msg.decode('ascii'))

logging.info("Client closed connection.")
clientsocket.close()
