from datetime import datetime
from imaplib import IMAP4_SSL


class Collector:
    def __init__(self, email, password, freq):
        self.email = email
        self.password = password
        self.frequency = freq

    with IMAP4_SSL("imap.mail.ru", 993) as imap:
        imap.login("qamogus@mail.ru", "7eZ9rsYQpth3Vyd7mDaU")
        imap.list()
        imap.select("inbox")

    def log(self, file, msg):
        with open(file, "a") as f:
            now = datetime.now().strftime("%Y.%m.%d|%H:%M:%S")
            f.write(f"[{now}] {msg}\n")
            f.close()
