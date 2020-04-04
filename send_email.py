####   Usage Example   #########
"""
sendmail = SendEmail(
    'email address',
    'password',
)
sendmail.send_email(
    'dest email address',
    'subject',
    'body')
"""

import smtplib
from email.mime.text import MIMEText

class SendEmail:
    def __init__(self, user, password):
        self.user_account = user
        self.password = password

    def send_email(self, dest, subject, body):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()


        server.login(self.user_account, self.password)


        mesg = MIMEText(body)
        mesg['Subject'] = subject

        server.sendmail(
            'jayzou2008@gmail.com',
            dest,
            mesg.as_string()
        )
        print('Email has been sent')

        server.quit()

