import os
from _datetime import datetime
import socket
from dotenv import load_dotenv

class Server:
    def __init__(self):
        self.server = None

        self.client_socket = None
        self.address = None

        dotenv_path = os.path.join(os.path.dirname(__file__), 'config.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)

        self.HOST = os.getenv("HOST")
        self.PORT = int(os.getenv("PORT"))
        self.FREQUENCY = os.getenv("FREQUENCY")
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")

    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen(4)
        self.client_socket, self.address = self.server.accept()

    def stop(self):
        self.server.close()

    def log(self, file, msg):
        with open(file, "a") as f:
            now = datetime.now().strftime("%d.%m.%Y|%H:%M:%S")
            f.write(f"[{now}] {msg}\n")
            f.close()
