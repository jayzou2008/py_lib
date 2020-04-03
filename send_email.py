import smtplib

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    user_account = 'jayzou2008@gmail.com'
    password = ' '

    server.login(user_account, password)

    subject = 'Price'
    body = 'check the link'

    #msg = f"Subject: {subject}\n\n{body}"
    msg = "Subject: %s\n\n%s" % (subject, body)
    #msg = "check"

    server.sendmail(
        'jayzou2008@gmail.com',
        'jay-zou2008@hotmail.com',
        msg
    )
    print('Email has been sent')

    server.quit()

if (1):
    send_email()
