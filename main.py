import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server = 'smtp.mail.com'
sender_email = 'senderemail@example.com'
sender_password = 'your password'
receiver_email = 'reciever_email@example.com'

text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada. Maecenas sed diam eget risus varius blandit sit amet non magna. Donec id elit non mi porta gravida at eget metus. ")

message = MIMEText(text, 'plain')
message['From'] = sender_email
message['Subject'] = 'Subject'
message['To'] = receiver_email

try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
finally:
    server.quit()