import smtplib
from email.message import EmailMessage

def alert_message(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'email.alert.python@gmail.com'
    msg['from'] = user
    password = 'wjjpzmnlyqfhpyub'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit() 

if __name__ == '__main__':
    alert_message('alert', 'hello', 'rajkulkarni123spam@gmail.com')
