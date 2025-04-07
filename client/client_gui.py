import logging
import socket

from tkinter import *
from tkinter import messagebox

class Window(Frame):
    def __init__(self, Master=None):
        Frame.__init__(self, Master)
        self.master = Master
        self.init_window()
        self.makeConnectionWithServer()
        
    def init_window(self):
        self.master.title("Client GUI")
        Label(self.master, text="dit is een test").pack()
        self.pack(fill=BOTH, expand=1)


    def makeConnectionWithServer(self):
        logging.info("Starting client...")

        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = socket.gethostname()
        port = 9999

        clientsocket.connect((host, port))

        msg = clientsocket.recv(1024)
        print(msg.decode('ascii'))

      
        
        
logging.basicConfig(level=logging.INFO)
root = Tk()
app = Window(root)
root.mainloop()
