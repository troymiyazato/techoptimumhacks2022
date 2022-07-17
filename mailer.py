import yagmail


class Mailer:
    def __init__(self):
        self.yag = yagmail.SMTP('codingprojectt@gmail.com','gscirgieiictonqu')

    def send_message(self, content, recipient, subject):
        self.yag.send(recipient, subject, content)