from imaplib import *

email = "qamogus@mail.ru"
code = "7eZ9rsYQpth3Vyd7mDaU"

with IMAP4_SSL("imap.mail.ru", 993) as mail:
    rc, resp = mail.login(email, "PythonLab7")
    mail.select()
    typ, data = mail.search(None, 'ALL')
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
