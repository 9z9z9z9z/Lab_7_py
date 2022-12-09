import socket
import configparser
from smtplib import SMTP


class Mail_server:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

    def send(self, description, messange):
        with SMTP("smtp.mail.ru", 465) as smtp:
            smtp.ehlo()
            smtp.starttls()
            print(f"Sending from {self.email}")
            smtp.login(self.email, self.password)
            smtp.sendmail(self.email, description, messange)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config_reader = config.read("config.ini")
    HOST = config["SERVER"]["HOST"]
    PORT = int(config["SERVER"]["PORT"])
    FREQUENCY = config["SERVER"]["FREQUENCY"]
    EMAIL = config["AUTH"]["EMAIL"]
    PASSWORD = config["AUTH"]["PASSWORD"]
    mailer = Mail_server(EMAIL, PASSWORD)
    mailer.send("qamogus@mail.ru", "Hello, billy!")
    