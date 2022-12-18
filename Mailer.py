from random import randint
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart


class Mailer:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.ID = 00000  # ID последнего сообщения
        self.MSG = ""  # текст последнего письма

    def send(self, dest, msg):
        self.MSG = msg

        body = MIMEMultipart()
        body['From'] = self.email
        body['To'] = dest
        body['Subject'] = f"[Ticket #{self.generate_token(msg)}] Mailer"
        body.attach(MIMEText(msg, 'plain'))

        with SMTP_SSL("smtp.mail.ru", 465) as smtp:
            smtp.login(self.email, self.password)
            text = body.as_string()
            smtp.sendmail(self.email, dest, text)
            smtp.quit()

    def generate_token(self, msg):
        self.ID = hash(msg) * randint(1, 1000)
        return self.ID
