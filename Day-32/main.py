import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_EMAIL = "shirgaonkarsaif2786@gmail.com"
PASSWORD = "dugmvsmzlvzajpvx"

msg = MIMEMultipart()
msg['From'] = MY_EMAIL
msg['To'] = "aameshgori2002@gmail.com"
msg['Subject'] = "Hello from Python SMTP"
body = "This is a test email sent from Python."
msg.attach(MIMEText(body, 'plain'))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.send_message(msg)
